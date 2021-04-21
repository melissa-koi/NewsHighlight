import unittest
from app.models import Articles

class Article(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Articles class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles('id','name','title','description','article_url','image','date')
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))