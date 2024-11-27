import unittest

from runner import Runner


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        runner = Runner("TesterWalk")
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner("TesterRun")
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challehge(self):
        runner1 = Runner("TesterChall1")
        runner2 = Runner("TesterChall2")
        for i in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == '__main__':
    unittest.main()
