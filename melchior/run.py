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

igf = IngestFile()

print(igf.loadFile('somefile.txt'))
