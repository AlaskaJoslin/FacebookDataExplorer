#!/usr/bin/env python3

import argparse
import logging
import os

from server import utils

if __name__== "__main__":
    #Parse args
    parser = argparse.ArgumentParser(description='Analyze a facebook data dump for a user.')
    parser.add_argument('--zipfile', help='The zipfile to extract from')
    parser.add_argument('--extraction_dir', default="extracted_data", help='Where to extract the zip file to')
    utils.add_bool_arg(parser, 'extract')
    args = parser.parse_args()

    #Create logger
    log_dir = "logs"
    utils.make_dir(log_dir)
    logger = utils.open_logger("{}/log".format(log_dir), logging.INFO)
    utils.make_dir(args.extraction_dir)

    #First we should extract a ZIP file to a specified dir
    if args.extract:
        if args.zipfile is None or args.extraction_dir is None:
            raise Exception("Please pass in the zipfile or extraction directory to extract")
        else:
            #Check to see if it's empty
            for data_category in os.listdir(args.extraction_dir):
                raise Exception("Already extracted to this directory please use a new directory")
            utils.extract_zipfile(args.zipfile, args.extraction_dir)

    all_extensions = set()
    def recurse_through_dirs(root_dir):
        data = {}
        for listing in os.listdir(root_dir):
            if "." in listing:
                extension = listing.split(".")[-1]
                if extension not in all_extensions:
                    logger.info("{}/{}".format(root_dir, listing))
                all_extensions.add(extension)
            if os.path.exists("{}/{}/no-data.txt".format(root_dir, listing)):
                data[listing] = {}
                continue
            # logger.info(listing)
            if os.path.isdir("{}/{}".format(root_dir, listing)):
                data[listing] = recurse_through_dirs("{}/{}".format(root_dir, listing))
            else:
                if listing.endswith(".json"):
                    # logger.info(listing)
                    obj = utils.load_json("{}/{}".format(root_dir, listing))
                    data[listing.replace(".json", "")] = obj
        return data

    all_data = recurse_through_dirs(args.extraction_dir)
    logger.info(all_extensions)
    utils.save_json(all_data, "all_data.json")
