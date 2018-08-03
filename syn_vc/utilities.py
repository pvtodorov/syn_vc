import hashlib
import importlib
import json
import os
import subprocess
import uuid
from collections import defaultdict
import morph


def recursivedict():
    """ Creates a dict of dicts as deep as needed.
    """
    return defaultdict(recursivedict)


def check_or_create_dir(path):
    """ Check if a folder exists. If it doesn't create it.
    """
    if not os.path.exists(path):
        os.makedirs(path)


def calc_content_md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(2 ** 20), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def get_settings_md5(settings):
    """Produces an md5 hash of the settings dict"""
    flat_settings = flatten_settings(settings)
    settings_str = json.dumps(flat_settings, allow_nan=False, sort_keys=True)
    h = hashlib.md5()
    h.update(settings_str.encode())
    return h.hexdigest()


def flatten_settings(settings, prefix=''):
    flat_settings = morph.flatten(settings)
    flat_settings = {prefix + k: v for k, v in flat_settings.items()}
    return flat_settings


def get_settings_annotations(settings):
    annotations = {}
    annotations.update(flatten_settings(settings, 'settings.'))
    annotations.update({'settings_md5': get_settings_md5(settings)})
    return annotations


def load_json(path):
    with open(path) as f:
        return json.load(f)


def save_json(d, path):
    with open(path, 'w') as outfile:
        json.dump(d, outfile, allow_nan=False, sort_keys=True)
