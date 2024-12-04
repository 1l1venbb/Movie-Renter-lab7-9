import unittest
from testing import test_client
from testing import test_movie
from testing import test_rent
from testing import test_utils


def assemble_and_run_tests():
    # Creating a test suite
    suite = unittest.TestSuite()

    # Adding test classes to the suite
    # Assuming you have test cases with `unittest.TestCase` in individual modules
    suite.addTests(unittest.defaultTestLoader.loadTestsFromModule(test_client))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromModule(test_movie))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromModule(test_rent))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromModule(test_utils))

    # Running the test suite
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    assemble_and_run_tests()
