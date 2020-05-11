#!/usr/bin/env python3

""" search.py: class containing search related code """

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

class Search(object):

    module_name = '[melchior.search]'

    def simpleSearch(self, criteria, body):
        """ 
        this needs a lot of polishing up, should ideally return a true/false for hit
        and if a hit is found then a line number or other identifier for where it occured
        """
        if (body.find(criteria) != -1):
            print("hit: %s" % criteria)
            return True
        else:
            print("failed on %s" % criteria)
            return False
