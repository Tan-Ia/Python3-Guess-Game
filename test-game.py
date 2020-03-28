
import unittest
from game import guessinggame

class TestGuess(unittest.TestCase):
    def test_game(self):
        res = guessinggame()
        self.assertIsNone(res, msg="Run Successful")
    def test_game_value(self):
        with self.assertRaises(ValueError):
            guessinggame()
     
    
  


if __name__ == "__main__":
    unittest.main()