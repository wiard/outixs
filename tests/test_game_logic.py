import unittest
from src.game_logic import GameLogic

class TestGameLogic(unittest.TestCase):
    def setUp(self):
        self.game_logic = GameLogic()

    def test_initial_game_state(self):
        state = self.game_logic.get_game_state()
        self.assertIsNotNone(state)
        self.assertIn('players', state)
        self.assertIn('levels', state)

    def test_add_player(self):
        player_id = "player1"
        self.game_logic.add_player(player_id)
        state = self.game_logic.get_game_state()
        self.assertIn(player_id, state['players'])

    def test_update_score(self):
        player_id = "player1"
        self.game_logic.add_player(player_id)
        self.game_logic.update_score(player_id, 10)
        state = self.game_logic.get_game_state()
        self.assertEqual(state['players'][player_id]['score'], 10)

if __name__ == "__main__":
    unittest.main()

