#!/usr/bin/env python3

import json
import yaml


def js_ya():
    with open('./tests/fixtures/structured_file2.json', 'r') as json_in, open('./tests/fixtures/structured_file2.yaml', 'w') as yaml_out:
        json_load = json.load(json_in)
        yaml.dump(json_load, yaml_out, sort_keys=False)
    print('hey')


js_ya()
