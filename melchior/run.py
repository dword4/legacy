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

igf = IngestFile()
isf = Search()

igf.loadFile('somefile.txt')
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

#print(igf.data)
print(isf.searchJoint(igf.data, 'Project','Gutenberg','1',5))
