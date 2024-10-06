from runner_and_tournament import Runner, Tournament
from runner import Runner
import unittest



class RunnerTest(unittest.TestCase):
    is_frozen = False
    """Логика использования модуля random, в лекции преподаватель пытался так сделать"""
    # import random
    # bool_test = random.randint(0, 3)
    # if bool_test == 3:
    #     is_frozen = True
    # else:
    #     is_frozen = False

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner = Runner('runner')
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner = Runner("runner2")
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner1 = Runner('runner3')
        runner2 = Runner('runner4')
        for i in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance, True)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner('Усейн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        self.result = tournament.start()
        result_name = []
        place = 0
        self.expected_result = {}

        for runner in self.result.values():
            result_name.append(runner)

            place += 1
            self.expected_result[place] = runner.name

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        self.assertEqual(self.expected_result, self.result)
        """Можно было конечно перебрать все значения в словаре и с помощью метода __str__
        из класса Runner заменить их на читаемые, но получается громоздкий код, да и лишняя
        работа ни к чему"""
        self.all_results.update(self.expected_result)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_inequality(self):
        self.assertEqual(self.expected_result, self.result, False)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_equality(self):
        self.assertTrue(self.expected_result == self.result, True)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_finishers(self):
        self.assertEqual(len(self.result.values()), len((self.expected_result.values())))

    @classmethod
    def tearDownClass(cls):
        print(cls.all_results)


if __name__ == '__main__':
    unittest.main()
