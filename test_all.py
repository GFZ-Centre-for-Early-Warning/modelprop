#!/usr/bin/env python3

'''
Unit tests for modelprop.
'''

import unittest

import modelprop

from test_cmd import *


class TestAll(unittest.TestCase):
    '''
    Unit test class.
    '''

    def test_get_supported_schemas(self):
        '''
        Extracts which schemas are supported.
        :return: None
        '''
        supported_schemas = modelprop.get_supported_schemas()

        assumed_schemas = [
            'HAZUS_v1.0',
            'SARA_v1.0',
            'SUPPASRI2013_v2.0',
            'Mavrouli_et_al_2014',
            'Torres_Corredor_et_al_2017'
        ]

        self.assertTrue(supported_schemas)

        self.assertEqual(len(assumed_schemas), len(supported_schemas))

        for schema in assumed_schemas:
            self.assertIn(schema, supported_schemas)


if __name__ == '__main__':
    unittest.main()
