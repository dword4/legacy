#from context import search
from melchior.search import Search
import pytest


corpus = 'The quick brown fox jumped over the lazy dog'
corpus_complex = '''
When in the Course of human events, it becomes necessary for one people to dissolve the political bands which have connected them with another, and to assume among the powers of the earth, the separate and equal station to which the Laws of Nature and of Nature\'s God entitle them, a decent respect to the opinions of mankind requires that they should declare the causes which impel them to the separation
'''

s = Search()

class TestClass:
    def test_simpleSearch(self):
        result = s.simpleSearch('brown', corpus)
        assert result == True 

