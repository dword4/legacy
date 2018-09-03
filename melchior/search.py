#!/usr/bin/env python3

""" search.py: class for search functionaltiy """

__author__ = "Drew Hynes"
__copyright__ = "Copyright 2018"
__credits__ = ["Drew Hynes"]
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = "Drew Hynes"
__email__ = "drew.hynes@gmail.com"
__status__ = "In Development"

import re
import logging

class Search(object):

    def searchSimple(self, corpus, word):
        logging.info('begin: searchSimple ->',word)
        result = corpus.find(word)
        # again this will need cleanup to use a logging method

        if result == -1:
            # logging here: failure
            return False
        else:
            # logging here: success
            return True

    def searchJoint(self, corpus, word1, word2, feature, weight):
        """
        feature can be 1 (single direction) or 2 (either direction)
        so with 1 set you can find 'word1' 'word2' or if you set 2
        then you can find 'word2' 'word1' as well
        """
        # note to self - feature is being passed as a string for now
        # but it needs to be passed as an integer for readability
        score = 0
        words = corpus.split()
        if feature == '1':
            logging.debug('beging searchJoint, uni-directional-> %s %s' % (word1, word2))
            # foward search only
            ret = "forward only"

            # check number of occurances first
            wordcount = corpus.split().count(word1)
            if wordcount == 1:
                # single occurance
                word1_position = words.index(word1)
                if words[word1_position + 1] == word2:
                    score = weight
            elif wordcount >= 2:
                # more than 1 occurance
                locations = [i for i,x in enumerate(words) if x == word1]

                for location in locations:
                    if words[location+1] == word2:
                        logging.debug('searchJoint HIT %s %s, weight: %s, direction: foward' % (word1, word2, weight))
                        score = score + int(weight)
                    else:
                        pass
            else:
                # no results!
                pass


        elif feature == '2':
            logging.debug('beging searchJoint, bi-directional-> %s %s' % (word1, word2))
            # bi-directional search, forward then reverse

            # forward search
            locations = [i for i,x in enumerate(words) if x == word1]

            for location in locations:
                if words[location+1] == word2:
                    #print("FOUND")
                    logging.debug('searchJoint HIT %s %s, weight: %s, direction: foward' % (word1, word2, weight))
                    score = score + int(weight)
                else:
                    pass

            # reverse search
            for location in locations:
                if words[location-1] == word2:
                    #print("FOUND")
                    logging.debug('searchJoint HIT %s %s, weight: %s, direction: reverse' % (word2, word1, weight))
                    score = score + int(weight)
                else:
                    pass
        else:
            # time for another one of those nice error messages
            ret = "ERROR"
        return score
