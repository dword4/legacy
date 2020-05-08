#!/usr/bin/env python3

from melchior.ingest import *
from melchior.search import *
import logging
import arrow

ts = arrow.utcnow()
logging.basicConfig(filename='run.log',format='%(asctime)s %(message)s',level=logging.DEBUG) # make config driven later
logging.info('[START]')

if __name__ == '__main__':
    n = Ingest()
    n.File('target.txt')
    print(type(n.data))
    print("melchior online")
    logging.info('[END]')
