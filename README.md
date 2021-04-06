# python-algorand-vanity
Python script to generate Algorand vanity addresses.

Original source code: [https://github.com/PureStake/api-examples/blob/master/python-examples/algo_vanity.py](https://github.com/PureStake/api-examples/blob/master/python-examples/algo_vanity.py)

## Prerequisites
* `python3.6`
* `pip3`
* `virtualenv`

## Installing
1. You need to create a `virtualenv`. From a terminal inside the project root directory type the following:
```shell
virtualenv --python=python3.6 venv
```
2. Install the package dependencies (`py-algorand-sdk`):
```shell
venv/bin/pip install -r requirements.txt
```
3. Activate your `venv`:
```shell
source venv/bin/activate
```

## Usage

### Vanity Address
* To generate an Algorand vanity address that starts with a given pattern (for instance `ASDF`), run the `generate_vanity.py` script as follows:
```shell
python generate_vanity.py ASDF
```
* The output of the script should be something similar to this:
```text
Detected 4 cpu(s)
Found a match for ASDF after 1403857 tries in 45.72 seconds

Algorand Address: ASDF5O4QQ2Z6B7NE7NX22FLBNATXYLZLFDDZREFX34HYS64REOSDC5DLTY
Private Key: /yvxhaPJQtX7gPQtRUsteQN5IQm2G1CD4ptnkIaVDRMEhl67kIaz4P2k+2+tFWFoJ3wvKyjHmJC33w+Je5EjpA==
Mnemonic:
lend seven seed olive machine vocal amazing virus pizza code note daring velvet embark raccoon brick head meat social all artwork grace observe abandon throw
```

### Random Address
* To generate a random Algorand address, run the ``generate_random.py`` script:
```shell
python generate_random.py
```
* The output should be something similar to this:
```text
Algorand Address: CR2KSOBXCC5UFDS6GQCOYRE73BM65HFV7GIRGGDFUXCGAJMJT7UP276BKQ
Private Key: uLAlr9+Xsx2r5gskg5rsyEfAUDV5BWn53ttZ0HefBlYUdKk4NxC7Qo5eNATsRJ/YWe6ctfmRExhlpcRgJYmf6A==
Mnemonic:
blade nothing stuff law grunt shuffle crystal armor goose head iron lady letter feature situate air coffee know unknown airport use pond rabbit able edge
```