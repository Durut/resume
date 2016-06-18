#!/usr/bin/env python
import json
from os.path import exists
import re
import sys
import yaml

def check_overwrite(path):
    prompt = '{} exists. Overwrite [y/N]? '.format(path)
    if not exists(path):
        return True

    elif input(prompt).lower()[:1] == 'y':
        print('Overwriting...')
        return True

    return False

def json_to_yaml(path):
    with open(path) as f:
        data = json.load(f)

    path_ = re.sub('.json$', '.yaml', path, count=1, flags=re.IGNORECASE)

    if not check_overwrite(path_):
        return

    with open(path_, 'w') as g:
        yaml.dump(data, g, indent=2)

def yaml_to_json(path):
    with open(path) as f:
        data = yaml.load(f)

    path_ = re.sub('.yaml$', '.json', path, count=1, flags=re.IGNORECASE)

    if not check_overwrite(path_):
        return

    with open(path_, 'w') as g:
        json.dump(data, g, indent=2)

def main(args):
    usage = 'Usage: {} /path/to/resume.{{json|yaml}}'.format(args[0])
    if len(args) != 2:
        sys.exit(usage)

    path = args[1]
    if path.endswith('.json'):
        json_to_yaml(path)

    elif path.endswith('.yaml'):
        yaml_to_json(path)

    else:
        sys.exit(usage)

if __name__ == '__main__':
    main(sys.argv)
