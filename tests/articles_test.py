import unittest
from app.models import Articles

class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behavior of the Articles class
    '''
    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.new_articles = Articles('cbs-news','CBS News','CBS/AP','Russia says it will hold war games in Mediterranean this week','Moscow blames U.S. for forcing its "powerful" military build-up in the Med as West and Moscow trade warnings over looming Syria offensive','https://www.cbsnews.com/news/russia-military-naval-presence-mediterranean-us-vladimir-putin-syria-offensive/','https://cbsnews3.cbsistatic.com/hub/i/r/2018/08/30/5b0ddcdb-81b7-4972-9388-8267aa67acc8/thumbnail/1200x630/7a17fc2a252a0bdee4bf710b06846abe/russia-navy-mediterranean.jpg', '2018-08-30T10:09:31Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_articles,Articles))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_articles.id,'cbs-news')
        self.assertEquals(self.new_articles.name,'CBS News')
        self.assertEquals(self.new_articles.author,'CBS/AP')
        self.assertEquals(self.new_articles.title,'Russia says it will hold war games in Mediterranean this week')
        self.assertEquals(self.new_articles.description,'Moscow blames U.S. for forcing its "powerful" military build-up in the Med as West and Moscow trade warnings over looming Syria offensive')
        self.assertEquals(self.new_articles.url,'https://www.cbsnews.com/news/russia-military-naval-presence-mediterranean-us-vladimir-putin-syria-offensive/')
        self.assertEquals(self.new_articles.urlToImage,'https://cbsnews3.cbsistatic.com/hub/i/r/2018/08/30/5b0ddcdb-81b7-4972-9388-8267aa67acc8/thumbnail/1200x630/7a17fc2a252a0bdee4bf710b06846abe/russia-navy-mediterranean.jpg')
        self.assertEquals(self.new_articles.publishedAt,'2018-08-30T10:09:31Z')
