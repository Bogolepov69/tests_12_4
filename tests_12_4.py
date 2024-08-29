import unittest
import logging
from homeworks.module12.homework_3 import Runner

logging.basicConfig(
    level=logging.INFO,
    filemode='w',
    filename='runner_tests.log',
    encoding='utf-8',
    format='%(asctime)s : %(levelname)s : %(message)s'
)

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner = Runner('Тест', -5)
        except:
            logging.warning("Неверная скорость для Runner: %s", e)
            self.assertEqual(str(e), "Скорость не может быть отрицательной, сейчас -5")
        else:
            logging.info('"test_walk" выполнен успешно')


    def test_run(self):
        try:
            runner = Runner(123, 10)
        except:
            logging.warning("Неверный тип данных для объекта Runner: %s", e)
            self.assertEqual(str(e), "Имя может быть только строкой, передано int")
        else:
            logging.info('"test_run" выполнен успешно')

if __name__ == "__main__":
    unittest.main()