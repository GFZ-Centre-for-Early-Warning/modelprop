#!/usr/bin/env python3

'''
Unit tests for modelprop.
'''

import unittest

import modelprop


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

        assumed_schemas = ['HAZUS_v1.0', 'SARA_v1.0', 'SUPPASRI2013_v2.0']

        self.assertTrue(supported_schemas)

        self.assertEqual(len(assumed_schemas), len(supported_schemas))

        for schema in assumed_schemas:
            self.assertIn(schema, supported_schemas)


if __name__ == '__main__':
    unittest.main()
