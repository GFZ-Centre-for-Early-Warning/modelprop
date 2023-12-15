#!/usr/bin/env python3

# Copyright © 2021 Helmholtz Centre Potsdam GFZ German Research Centre for Geosciences, Potsdam, Germany
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

"""
This script checks the json files
for modelprop.

At the moment it checks, if the files is
a valid json file
and if the all the names in the taxonomies
list are the same as in the
data list.
"""

import argparse
import json
import pprint


def get_taxonomies_by_meta(data):
    """
    Reads from the dict via
    meta -> taxonomies
    """
    return data["meta"]["taxonomies"]


def get_taxonomies_by_data_list(data):
    """
    Reads from the dict via
    data -> list -> taxonomy
    """
    tax_list_with_data = data["data"]
    return [x["taxonomy"] for x in tax_list_with_data]


def set_empty(data):
    """
    Tests if the set is empty.
    """
    return not data


def main():
    """
    Runs the program, tries to open a json file and
    does some checks.
    """
    arg_parser = argparse.ArgumentParser("Tests a mopelprop json file.")
    arg_parser.add_argument("jsonfile", help="The json file to test.")
    args = arg_parser.parse_args()

    with open(args.jsonfile, "rt") as input_file:
        data = json.load(input_file)

    taxonomies = set(get_taxonomies_by_meta(data))
    taxonomies_by_data = set(get_taxonomies_by_data_list(data))

    not_in_data = taxonomies - taxonomies_by_data
    not_in_meta = taxonomies_by_data - taxonomies

    if not_in_data:
        print("Error: The following taxonomies are not in the data")
        pprint.pprint(not_in_data)

    if not_in_meta:
        print("Error: The following taxonomies are not in the meta section")
        pprint.pprint(not_in_meta)

    if set_empty(not_in_meta) and set_empty(not_in_data):
        print("Ok")


if __name__ == "__main__":
    main()
