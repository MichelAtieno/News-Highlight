import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behavior of the News class
    '''
    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.new_news = News('USA Today','Cydney Henderson','Kanye West "properly" apologizes for slavery comment, answers Kimmel question about Trump','Kanye West got emotional while apologizing for his controversial slavery comments and also gave a long-awaited answer to Jimmy Kimmels question.','https://www.usatoday.com/story/life/people/2018/08/29/kanye-west-apologizes-slavery-remark-answers-kimmel-question/1139792002/','https://www.gannett-cdn.com/-mm-/b2b05a4ab25f4fca0316459e1c7404c537a89702/c=0-0-1365-768/local/-/media/2018/08/01/USATODAY/usatsports/247WallSt.com-247WS-483194-imageforentry482.jpg?width=3200&height=1680&fit=crop','2018-08-30T02:38:00Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))

if __name__ == '__main__':
    unittest.main()
    