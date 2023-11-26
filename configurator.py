"""
Poor Man's Configurator. Probably a terrible idea. Example usage:
$ python train.py config/override_file.py --batch_size=32
this will first run config/override_file.py, then override batch_size to 32

The code in this file will be run as follows from e.g. train.py:
>>> exec(open('configurator.py').read())

So it's not a Python module, it's just shuttling this code away from train.py
The code in this script then overrides the globals()

I know people are not going to love this, I just really dislike configuration
complexity and having to prepend config. to every single variable. If someone
comes up with a better simple Python solution I am all ears.
"""

import json
import sys
from ast import literal_eval

def load_config_from_json(json_file):
    with open(json_file, 'r') as f:
        config = json.load(f)
    return config

def update_config_with_args(config, args):
    for arg in args:
        if '=' in arg:
            assert arg.startswith('--')
            key, val = arg.split('=')
            key = key[2:]
            if key in config:
                try:
                    # attempt to eval it it (e.g. if bool, number, or etc)
                    attempt = literal_eval(val)
                except (SyntaxError, ValueError):
                    # if that goes wrong, just use the string
                    attempt = val
                # ensure the types match ok
                assert type(attempt) == type(config[key])
                print(f"Overriding: {key} = {attempt}")
                config[key] = attempt
            else:
                raise ValueError(f"Unknown config key: {key}")
    return config
