import unittest
from app.models import Article

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article('Naila-Jean Meyers and Scott Cacciola','In the 30th professional match between the sisters, Serena defeated Venus in the third round. Rafael Nadal, Juan Martin del Potro and Sloane Stephens also won Friday.','2019-11-17T05:22:26Z','https://www.nytimes.com/2019/11/17/sports/tennis/us-open-results.html','https://static01.nyt.com/images/2019/11/17/sports/01openlive7/01openlive7-facebookJumbo.jpg','US Open 2019 Results')

    def test_instance(self):
        
        self.assertTrue(isinstance(self.new_article,Article))

