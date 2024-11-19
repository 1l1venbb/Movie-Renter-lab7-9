from utils.randomClient import RandomClient

class TestRandomClient:

    def run_all_tests(self):
        """
        Run all tests
        """
        self.test_generateRandomID()
        self.test_generateRandomCNP()


    def test_generateRandomID(self):
        random = RandomClient()
        id = random.generateRandomID()
        assert 1 <= len(str(id)) <= 7

    def test_generateRandomCNP(self):
        random = RandomClient()
        cnp = random.generateRandomCNP()
        assert 13 == len(cnp)

        try:
            int(cnp)
            assert True
        except ValueError:
            assert False
