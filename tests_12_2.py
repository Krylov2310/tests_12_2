import time
import unittest as un
from tqdm import tqdm
import runner_and_tournament as rat

print('\033[30m\033[47mДомашнее задание по теме "Методы Юнит-тестирования"\033[0m')
print('\033[30m\033[47mЦель: освоить методы, которые содержит класс TestCase.\033[0m')
print('\033[30m\033[47mСтудент Крылов Эдуард Васильевич\033[0m')
print('\033[30m\033[47mДата: 09.10.2024г.\033[0m')
print()
thanks = '\033[0m\n\033[30m\033[47mБлагодарю за внимание :-)\033[0m'


class TournamentTest(un.TestCase):

    def setUp(self):
        self.runner1 = rat.Runner('Усейн', 10)
        self.runner2 = rat.Runner('Андрей', 9)
        self.runner3 = rat.Runner('Ник', 3)
        self.runner4 = rat.Runner('Эдисон', 15)

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def tearDown(self):
        self.runner_name = []
        self.place = 0
        self.check_results = {}
        full_speed = [runner.speed for runner in self.results.values()]
        for runners in tqdm(self.results.values()):
            print(' Сейчас бежит:', runners)
            self.runner_name.append(runners)
            for speed in full_speed:
                if runners.speed >= speed:
                    self.runner_name += runners.name
                    time.sleep(0.5)
            self.place += 1
            self.check_results[self.place] = runners.name
        self.assertEqual(self.check_results, self.results, False)
        self.assertTrue(self.check_results == self.results, True)
        self.assertEqual(self.check_results, self.results)
        self.all_results.update(self.check_results)
        print('Результат забега:', self.all_results)
        time.sleep(1)

    def test_run1(self):
        print('\033[31m1 забег:\033[0m')
        self.tournament = rat.Tournament(90, self.runner1, self.runner3)
        self.results = self.tournament.start()

    def test_run2(self):
        print('\033[33m2 забег:\033[0m')
        tournament = rat.Tournament(90, self.runner3, self.runner2)
        self.results = tournament.start()

    def test_run3(self):
        print('\033[32m3 забег:\033[0m')
        tournament = rat.Tournament(90, self.runner1, self.runner2, self.runner3)
        self.results = tournament.start()

    def test_run4(self):
        print('\033[35m4 забег:\033[0m')
        tournament = rat.Tournament(90, self.runner1, self.runner2, self.runner3, self.runner4)
        self.results = tournament.start()

    @classmethod
    def tearDownClass(cls):
        print(thanks)

if __name__ == '__main__':
    un.main()
