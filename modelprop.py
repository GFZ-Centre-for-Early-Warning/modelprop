#!/usr/bin/env/python

'''
ModelProp
-----------------
Command line program to query fragility/vulnerability data from a database/file
according to a given schema and (optinally) for a set of taxonomies
Author: Massimiliano Pittore, GFZ-Potsdam
'''

import argparse
import os
import pandas as pd
import json

class Main():
    '''
    Main class to execute
    '''
    def __init__(self, args):
        self.folder = os.path.dirname('__file__')

        self.data = None
        self.metadata = None
        self.taxonomies = None

        # command line arguments
        self.assetcategory = args.assetcategory
        self.schema = args.schema
        self.selectedtaxonomies = None
        if args.taxonomies:
            try:
                self.selectedtaxonomies = json.loads(args.taxonomies)
            except json.decoder.JSONDecodeError:
                print("Error Decoding Taxonomy list. Using 'None'.")
                pass
        
        #i/o settings
        self.path_infile = self.folder
        self.in_file = self.folder
        self.path_outfile = os.path.join(self.folder,"output")
        self.out_file_xml = "query_output.nrml"
        self.out_file_geojson = 'query_output.json'
        
        #list of supported schemas. 
        #TODO: automatically parse them from a given folder
        self.supported_schemas = ['SARA_v1.0']

        # results
        self.query_result_data = None
        self.query_result_metadata = None

    def _check_schema(self):
        return(set([self.schema]) <= set(self.supported_schemas))
     
    def _check_taxonomies(self,selected):
        '''
        check if the taxonomies in the list "selected" are 
        contained in the metadata
        '''
        if (self.metadata):
            return(set(selected) <= set(self.metadata['taxonomies']))
        else:
            print("_check_taxonomies: metadata are not defined.")
            return(False)
    
    def _read_schema(self, input_file):
        '''
        read fragility/vulnerability model from a json file.
        the file contains two dictionaries: 
        1) 'meta' includes information (metadata) on the schema, the list of taxonomies and
           damage states
        2) 'data' provides the mean and log. std deviation of the lognormal
           distribution encoding the fragility / vulnerability descriptions
        the function returns a dictionary with metadata and a pandas dataframe
        '''
        with open(input_file,'r') as f:
            parsed = json.load(f)
        
        self.metadata = parsed['meta']
        self.data = pd.DataFrame(parsed['data'])
        return(0)

    def _write_schema(self, metadata, data, output_file):
        '''
        write fragility/vulnerability schema to a json file.
        the file contains two dictionaries: 
        1) 'meta' includes information (metadata) on the schema, the list of taxonomies and
           damage states
        2) 'data' provides the mean and log. std deviation of the lognormal
           distribution encoding the fragility / vulnerability descriptions
        the function accepts a dictionary with metadata and a pandas dataframe
        '''
        if ((metadata is not None) and (data is not None)):
            modict = {}
            modict['meta'] = metadata
            #data should be a pandas dataframe
            modict['data'] = data.to_dict(orient='records')
            with open(output_file,'w') as f:
                json.dump(modict,f, indent=4)
            return (0)
        else:
            print ("_write_schema: metadata or data are missing.")
            return(1)
        
    
    def _queryModel(self):
        '''
        extract a part of the model by doing a query on the 
        selected taxonomies (selectedtaxonomies)
        '''
        if (self.selectedtaxonomies):
            if (self._check_taxonomies(self.selectedtaxonomies)):
                self.query_result_metadata = self.metadata.copy()
                self.query_result_metadata['taxonomies']=self.selectedtaxonomies
                self.query_result_data = self.data.set_index('taxonomy').loc[self.selectedtaxonomies].reset_index()
        else:
            self.query_result_data = self.data
            self.query_result_metadata = self.metadata
        
        return(0)
    
    def _exportGeoJson(self, dataframe, filename):
        '''
        Export geopandas dataframe as GeoJson file
        '''
        # file has to be first deleted
        # because driver does not support overwrite ! 
        try: 
            os.remove(filename)
        except OSError:
            pass
        dataframe.to_file(filename, driver='GeoJSON')
        return (0)

    def _exportNrml05(self, dataframe, filename, metadata, dicts,taxonomies):
        '''
        Export geopandas dataframe as nrml file
        '''
        xml_string = nrml.write_nrml05_expo(dataframe,metadata,dicts,taxonomies,filename)
        return (0)

    def _write_outputs(self):
        '''
        Export query result as nrml and geojson files
        '''
        output_geojson = os.path.join(self.path_outfile,self.out_file_geojson)
        self._write_schema(self.query_result_metadata, self.query_result_data,output_geojson)
        #output_xml = os.path.join(self.path_outfile,self.out_file_xml)
        #self._exportNrml05(self.query_result, output_xml, self.metadata, 
        #                   self.dicts,self.taxonomies)
    
    def run(self):
        '''
        Method to:
        - load the fragility model from a file (json)
        - query the model based on a list of taxonomies
        - write the output(s)
        '''
        if (self._check_schema()):
            foldername = os.path.join(self.folder,"schemas/{}".format(self.schema))
            self.path_infile = foldername
            self.in_file = "{}_struct.json".format(self.schema)
        else:
            raise Exception ("schema {} not supported".format(self.schema))

        #read model from file 
        in_file = os.path.join(self.path_infile,self.in_file)
        self._read_schema(in_file)

        #query
        self._queryModel()

        #write outputs
        self._write_outputs()
        return (0)


    @classmethod
    def create_with_arg_parser(cls):
        '''
        Creates an arg parser and uses that to create the Main class
        '''
        arg_parser = argparse.ArgumentParser(
            description='''Program to query a fragility/vulnerability
            model from a database/file'''
        )
        arg_parser.add_argument(
            'schema',
            help='Exposure/Vulnerability Schema',
            type=str,
            default="SARA_v1.0")
        arg_parser.add_argument(
            'assetcategory',
            help='Type of exposed assets',
            type=str,
            default='buildings')
        arg_parser.add_argument(
            'losscategory',
            help='damage or loss computation',
            type=str,
            default='structural')
        arg_parser.add_argument( 
            '-taxonomies',
            #narg='?',
            help='selected taxonomies',
            type=str)

        args = arg_parser.parse_args()
        return cls(args)

if __name__ == '__main__':
    Main.create_with_arg_parser().run()