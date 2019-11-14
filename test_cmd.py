#!/usr/bin/env python3

"""
Unittests to query to modelprop data.
"""

import json
import os
import subprocess
import unittest


class TestTorres(unittest.TestCase):
    """
    Test class to query the modelprop with torres.
    """

    def test_full(self):
        """
        Runs the program and tests the output.
        """
        schema = 'Torres_Corredor_et_al_2017'

        current_dir = os.path.dirname(os.path.abspath(__file__))
        path_modelprop = os.path.join(
            current_dir,
            'modelprop.py'
        )

        subprocess.run(
            [
                'python3',
                path_modelprop,
                schema,
                'buildings',
                'structural'
            ],
            check=True

        )
        output_file = os.path.join(
            current_dir,
            'output',
            'query_output.json'
        )

        with open(output_file, 'rt') as fh:
            output_data = json.load(fh)

        self.assertEqual(schema, output_data['meta']['id'])


class TestMavrouli(unittest.TestCase):
    """
    Test class to query the modelprop for mavrouli.
    """

    def test_full(self):
        """
        Runs the program and tests the output.
        """
        schema = 'Mavrouli_et_al_2014'

        current_dir = os.path.dirname(os.path.abspath(__file__))
        path_modelprop = os.path.join(
            current_dir,
            'modelprop.py'
        )

        subprocess.run(
            [
                'python3',
                path_modelprop,
                schema,
                'buildings',
                'structural'
            ],
            check=True

        )
        output_file = os.path.join(
            current_dir,
            'output',
            'query_output.json'
        )

        with open(output_file, 'rt') as fh:
            output_data = json.load(fh)

        self.assertEqual(schema, output_data['meta']['id'])


class TestSuppasri(unittest.TestCase):
    """
    Test class to query the modelprop for suppasri.
    """

    def test_full(self):
        """
        Runs the program and tests the output.
        """
        schema = 'SUPPASRI2013_v2.0'

        current_dir = os.path.dirname(os.path.abspath(__file__))
        path_modelprop = os.path.join(
            current_dir,
            'modelprop.py'
        )

        subprocess.run(
            [
                'python3',
                path_modelprop,
                schema,
                'buildings',
                'structural'
            ],
            check=True

        )
        output_file = os.path.join(
            current_dir,
            'output',
            'query_output.json'
        )

        with open(output_file, 'rt') as fh:
            output_data = json.load(fh)

        self.assertEqual(schema, output_data['meta']['id'])


class TestSara(unittest.TestCase):
    """
    Test class to query the modelprop for sara.
    """

    def test_full(self):
        """
        Runs the program and tests the output.
        """
        schema = 'SARA_v1.0'

        current_dir = os.path.dirname(os.path.abspath(__file__))
        path_modelprop = os.path.join(
            current_dir,
            'modelprop.py'
        )

        subprocess.run(
            [
                'python3',
                path_modelprop,
                schema,
                'buildings',
                'structural'
            ],
            check=True

        )
        output_file = os.path.join(
            current_dir,
            'output',
            'query_output.json'
        )

        with open(output_file, 'rt') as fh:
            output_data = json.load(fh)

        self.assertEqual(schema, output_data['meta']['id'])


if __name__ == '__main__':
    unittest.main()
