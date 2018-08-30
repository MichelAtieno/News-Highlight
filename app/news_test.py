import unittest
from .models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behavior of the News class
    '''
    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.new_news = News('usa-today','USA Today','Former Balch Springs Officer Roy Oliver, 38, was convicted of fatally shooting Jordan Edwards, 15, after responding to the party.','https://www.usatoday.com/story/news/nation-now/2018/08/29/dallas-area-cop-sentenced-15-years-fatal-shooting-black-teen/1141400002/','general', 'us')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))

if __name__ == '__main__':
    unittest.main()
