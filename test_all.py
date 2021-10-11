#!/usr/bin/env python3

# Copyright © 2021 Helmholtz Centre Potsdam GFZ German Research Centre for Geosciences, Potsdam, Germany
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at
# 
# https://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

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
            'Torres_Corredor_et_al_2017',
            'Medina_2019',
        ]

        self.assertTrue(supported_schemas)

        self.assertEqual(len(assumed_schemas), len(supported_schemas))

        for schema in assumed_schemas:
            self.assertIn(schema, supported_schemas)


if __name__ == '__main__':
    unittest.main()
