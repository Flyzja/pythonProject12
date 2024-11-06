import module_12_1 as r
import unittest

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        runner1 = r.Runner('Иван')
        for walk in range(10):
            runner1.walk()
        self.assertEqual(runner1.distance, 50)


    def test_run(self):
        runner2 = r.Runner('Андрей')
        for run in range(10):
            runner2.run()
        self.assertEqual(runner2.distance, 100)


    def test_challenge(self):
        runner3 = r.Runner('Иван')
        runner4 = r.Runner('Александр')
        for run in range(10):
            runner3.run()
            runner4.run()
        for walk in range(10):
            runner3.walk()
            runner4.walk()

        self.assertNotEqual(runner3, runner4, 'Тест провален')

if __name__ == "__main__":
    unittest.main()
