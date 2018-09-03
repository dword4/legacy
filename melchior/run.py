#!/usr/bin/env python3

""" run.py: Runs the various components that comprise the Melchior tool """

__author__ = "Drew Hynes"
__copyright__ = "Copyright 2018"
__credits__ = ["Drew Hynes"]
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = "Drew Hynes"
__email__ = "drew.hynes@gmail.com"
__status__ = "In Development"

from ingest import IngestFile
from search import Search
from configparser import ConfigParser

import logging

logging.basicConfig(filename='run.log',level=logging.DEBUG) # make config driven later
logging.info('---Start Run---')
config = ConfigParser()
config.read('melchior.conf')

igf = IngestFile()
isf = Search()

filename = 'somefile.txt' # temporary for testing purposes
try:
    logging.info('Trying to load file:'+filename)
    igf.loadFile(filename)
    logging.info('Successfully loaded file:'+filename)
except my:
    print("failed to load file")
"""
wordset = ['goat','success','Please','smite','Conan','how']

score = 0
wt = 1 # this is temporary

for word in wordset:
    result = isf.searchSimple(igf.loadFile('somefile.txt'), word )
    if result == True:
        score += 1
    else:
        # no change to score
        pass

print("Score: "+str(score))
"""

print(isf.searchJoint(igf.data, 'Project','Gutenberg','1',5))
