import unittest
from app.models import Headlines

class HeadlinesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Headlines class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_headlines = Headlines('Naila-Jean Meyers and Scott Cacciola','In the 30th professional match between the sisters, Serena defeated Venus in the third round. Rafael Nadal, Juan Martin del Potro and Sloane Stephens also won Friday.','2019-11-171T05:22:26Z','https://www.nytimes.com/2019/11/17/sports/tennis/us-open-results.html','https://static01.nyt.com/images/2018/09/01/sports/01openlive7/01openlive7-facebookJumbo.jpg','US Open 2018 Results')

    def test_instance(self):
        '''
        Test to check creation of new headline instance
        '''

        self.assertTrue(isinstance(self.new_headlines,Headlines))