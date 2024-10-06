import unittest
import tests12_3


test1ST = unittest.TestSuite()
test1ST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests12_3.TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
test2ST = unittest.TestSuite()
test2ST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests12_3.RunnerTest))
runner2 = unittest.TextTestRunner(verbosity=2)
runner.run(test1ST)
runner2.run(test2ST)
