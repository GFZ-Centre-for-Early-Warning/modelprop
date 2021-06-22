# modelprop


[![Docker Cloud Build Status](https://img.shields.io/docker/cloud/build/gfzriesgos/modelprop)](https://hub.docker.com/r/gfzriesgos/modelprop)
[![Build Status](https://travis-ci.com/gfzriesgos/modelprop.svg?branch=master)](https://travis-ci.com/gfzriesgos/modelprop)

## Purpose
Program to serve a fragility / vulnerability model
according to a given schema - RIESGOS Project

## Citation

Pittore, M., Gomez-Zapata, J. C., Brinckmann, N., Rüster, M. (2021): Assetmaster and Modelprop: web services to serve building exposure models and fragility functions for physical vulnerability to natural-hazards. V. 1.0. GFZ Data Services. https://doi.org/10.5880/riesgos.2021.005

## Setup

We use a virtual environment, so you can need to create it and
install the pacakges from pip:

```shell
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Example run
After that you can run modelprop as in the following example:

```shell
python3 modelprop.py SARA-v1.0 buildings structural
```

What are the parameters:

| Parameter      | Example    | Purpose                                                                                            |
|----------------|------------|----------------------------------------------------------------------------------------------------|
| schema         | SARA-v1.0  | This is the schema for the taxonomy.                                                               |
| asset category | buildings  | In this case we are only interested in buildings, and not in other infrastructure.                 |
| loss category  | structural | In this case we care about physical damage on the structure of the buildings.                      |
| taxonomy       |            | You can use this to just query a subset of the schema giving a taxonomy. This is empty by default. |

## Supported schemas

At the moment we support the following schemas:
* HAZUS-v1.0
* SARA-v1.0
* SUPPASRI2013-v2.0
* Mavrouli et al. 2014
* Torres Corredor et al. 2017

You can get a up to date list of the supported schemas by running the following commands
in a python shell from within this folder:

```python
import modelprop
modelprop.get_supported_schemas()
```


## Supported asset categories

At the moment only buildings are supported.

## Supported loss categories

At the moment we only support structural as loss category.

## How to add new schemas

### Naming and paths

The very first part is to check that the name of your schema file has the name `<your_schema_name>_struct.json` and
that this will be inserted in the folder `<your_schema_name>` in the schema subfolder.

### Data
It is important to have a meta block, with an id and the list of taxonomies and a data list with the
fragility function data for your taxonomy.

Every taxonomy that is listed in the data list must also be in the meta section and vice versa.

You can test it with the `assistance/check_modelprop_json_file.py` file.

## Copyright & License
Copyright © 2021 Helmholtz Centre Potsdam GFZ German Research Centre for Geosciences, Potsdam, Germany

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

## Project

Deus was developed in the scope of the RIESGOS project:
Multi-Risk Analysis and Information System Components for the Andes Region (https://www.riesgos.de/en)

