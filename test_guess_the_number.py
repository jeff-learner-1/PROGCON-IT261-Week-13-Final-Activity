import importlib.util
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import unittest
from unittest.mock import patch


modulePath = Path(__file__).with_name("GUESS THE NUMBER.py")
spec = importlib.util.spec_from_file_location("guess_the_number", modulePath)
game = importlib.util.module_from_spec(spec)
spec.loader.exec_module(game)


class GuessTheNumberTests(unittest.TestCase):
    def run_game(self, secret, guesses):
        output = StringIO()
        with patch("builtins.input", side_effect=guesses) as mock_input:
            with redirect_stdout(output):
                game.playGame(secret)
        return output.getvalue(), mock_input

    def test_secret_number_is_between_one_and_ten(self):
        with patch.object(game.random, "random", side_effect=[0.0, 0.999999]):
            self.assertEqual(game.getSecretNumber(), 1)
            self.assertEqual(game.getSecretNumber(), 10)

    def test_correct_first_guess_wins(self):
        output, mock_input = self.run_game(7, ["7"])
        self.assertIn("You win!", output)
        self.assertNotIn("Game Over!", output)
        mock_input.assert_called_once()

    def test_low_guess_shows_hint_then_can_win(self):
        output, _ = self.run_game(5, ["2", "5"])
        self.assertIn("Too low! Try again.", output)
        self.assertIn("You win!", output)

    def test_high_guess_shows_hint_then_can_win(self):
        output, _ = self.run_game(5, ["8", "5"])
        self.assertIn("Too high! Try again.", output)
        self.assertIn("You win!", output)

    def test_three_wrong_guesses_end_game(self):
        output, mock_input = self.run_game(5, ["1", "2", "3"])
        self.assertIn("Game Over! The secret number was: 5", output)
        self.assertEqual(output.count("Too low! Try again."), 3)
        self.assertEqual(mock_input.call_count, 3)


if __name__ == "__main__":
    unittest.main()