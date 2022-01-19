#!/usr/bin/env python3

# Copyright © 2021 Helmholtz Centre Potsdam GFZ German Research Centre for Geosciences, Potsdam, Germany
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

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
        schema = "Torres_Corredor_et_al_2017"

        current_dir = os.path.dirname(os.path.abspath(__file__))
        path_modelprop = os.path.join(current_dir, "modelprop.py")

        subprocess.run(
            ["python3", path_modelprop, schema, "buildings", "structural"],
            check=True,
        )
        output_file = os.path.join(current_dir, "output", "query_output.json")

        with open(output_file, "rt") as fh:
            output_data = json.load(fh)

        self.assertEqual(schema, output_data["meta"]["id"])


class TestMavrouli(unittest.TestCase):
    """
    Test class to query the modelprop for mavrouli.
    """

    def test_full(self):
        """
        Runs the program and tests the output.
        """
        schema = "Mavrouli_et_al_2014"

        current_dir = os.path.dirname(os.path.abspath(__file__))
        path_modelprop = os.path.join(current_dir, "modelprop.py")

        subprocess.run(
            ["python3", path_modelprop, schema, "buildings", "structural"],
            check=True,
        )
        output_file = os.path.join(current_dir, "output", "query_output.json")

        with open(output_file, "rt") as fh:
            output_data = json.load(fh)

        self.assertEqual(schema, output_data["meta"]["id"])


class TestSuppasri(unittest.TestCase):
    """
    Test class to query the modelprop for suppasri.
    """

    def test_full(self):
        """
        Runs the program and tests the output.
        """
        schema = "SUPPASRI2013_v2.0"

        current_dir = os.path.dirname(os.path.abspath(__file__))
        path_modelprop = os.path.join(current_dir, "modelprop.py")

        subprocess.run(
            ["python3", path_modelprop, schema, "buildings", "structural"],
            check=True,
        )
        output_file = os.path.join(current_dir, "output", "query_output.json")

        with open(output_file, "rt") as fh:
            output_data = json.load(fh)

        self.assertEqual(schema, output_data["meta"]["id"])


class TestSara(unittest.TestCase):
    """
    Test class to query the modelprop for sara.
    """

    def test_full(self):
        """
        Runs the program and tests the output.
        """
        schema = "SARA_v1.0"

        current_dir = os.path.dirname(os.path.abspath(__file__))
        path_modelprop = os.path.join(current_dir, "modelprop.py")

        subprocess.run(
            ["python3", path_modelprop, schema, "buildings", "structural"],
            check=True,
        )
        output_file = os.path.join(current_dir, "output", "query_output.json")

        with open(output_file, "rt") as fh:
            output_data = json.load(fh)

        self.assertEqual(schema, output_data["meta"]["id"])


class TestMedina(unittest.TestCase):
    """
    Test class to query the modelprop for medina.
    """

    def test_full(self):
        """
        Runs the program and tests the output.
        """
        schema = "Medina_2019"

        current_dir = os.path.dirname(os.path.abspath(__file__))
        path_modelprop = os.path.join(current_dir, "modelprop.py")

        subprocess.run(
            ["python3", path_modelprop, schema, "buildings", "structural"],
            check=True,
        )
        output_file = os.path.join(current_dir, "output", "query_output.json")

        with open(output_file, "rt") as fh:
            output_data = json.load(fh)

        self.assertEqual(schema, output_data["meta"]["id"])


if __name__ == "__main__":
    unittest.main()
