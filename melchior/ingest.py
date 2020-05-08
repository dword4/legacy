#!/usr/bin/env python3

""" ingest.py: class containing ingestion related code """

__author__ = "Drew Hynes"
__copyright__ = "Copyright 2018"
__credits__ = ["Drew Hynes"]
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = "Drew Hynes"
__email__ = "drew.hynes@gmail.com"
__status__ = "In Development"

import os
import logging

logging.basicConfig(filename='run.log',format='%(asctime)s %(message)s',level=logging.DEBUG) # make config driven later

from configparser import ConfigParser

config = ConfigParser()
config.read('melchior.conf')

class Ingest(object):

    module_name = '[Ingest]'

    # ingest a raw file from disk
    def File(self,filename):
        if os.path.isfile(filename) == False:
            # cannot find the file
            # need to handle errors better, since this is not a try/catch exceptions
            # dont want to raise cleanly
            logging.error('Failed to find file: '+filename)
            print("Failed to find the file:"+filename)

        else:
            # file is there, proceed
            fileSize = os.path.getsize(filename)
            maxFileSize = int(config.get('global','max_filesize'))
            if fileSize > maxFileSize:
                logging.info('File '+filename+' is too large to load, check max_filesize value in melchior.conf')
                print("File is too large!")
                return
            else:
                # file is ok, continue
                file = open(filename, "r")
                fh = file.read()
                file.close()
                self.data = fh
                logging.info('File '+filename+' successfully ingested')
                return

        return

