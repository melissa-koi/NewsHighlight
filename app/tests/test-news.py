import unittest
from ..models import News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News('id','name','description','news_url','category')
    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))