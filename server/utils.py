#!/usr/bin/env python3

import json
import logging
import os
import zipfile

def open_logger(logfile, level):
    logger = logging.getLogger('myapp')
    fh = logging.FileHandler(logfile)
    fh.setLevel(level)
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    ch = logging.StreamHandler()
    ch.setLevel(level)
    logger.addHandler(ch)
    logger.setLevel(level)
    return logger

def make_dir(dirname):
    if not os.path.isdir(dirname):
        os.mkdir(dirname)

def extract_zipfile(filename, dirname):
    with zipfile.ZipFile(filename, 'r') as zip_ref:
        zip_ref.extractall(dirname)

def add_bool_arg(parser, name, default=False):
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument('--' + name, dest=name, action='store_true')
    group.add_argument('--no-' + name, dest=name, action='store_false')
    parser.set_defaults(**{name:default})

def load_json(pth):
    with open(pth, 'r') as fh:
        obj = json.load(fh)
    return obj

def save_json(obj, pth):
    with open(pth, 'w') as fh:
        json.dump(obj, fh)
