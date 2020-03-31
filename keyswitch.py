import json
import os
import sys
import re

config = {}
CONFIG_PATH = '/Users/mark/.config/karabiner/karabiner.json'

def list():
    with open('{}'.format(CONFIG_PATH)) as json_data:
        data = json.load(json_data)
        for profile in data['profiles']:
            print(profile['name'] + ': ' + str(profile['selected']))

def set(chosen_file):
    with open('{}'.format(CONFIG_PATH)) as conf_file:
        config = json.load(conf_file)
        for profile in config['profiles']:
            profile['selected'] = (re.search(chosen_file.lower(), profile['name'].lower()) is not None)

    with open('{}'.format(CONFIG_PATH), 'w') as conf_file:
        conf_file.write(json.dumps(config, indent=4, separators=(',', ': ')))
