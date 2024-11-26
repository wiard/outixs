import unittest
from kernel.modules.state_machine_interface import StateMachineInterface

class TestStateMachineInterface(unittest.TestCase):

    def setUp(self):
        self.state_machine = StateMachineInterface()
        self.state_machine.add_state("State1")
        self.state_machine.add_state("State2")
        self.state_machine.add_transition("State1", "State2", "Event")

    def test_add_state(self):
        result = self.state_machine.add_state("State3")
        self.assertEqual(result, "State added successfully")

    def test_add_transition(self):
        result = self.state_machine.add_transition("State1", "State2", "Event")
        self.assertEqual(result, "Transition added successfully")

    def test_add_invalid_transition(self):
        result = self.state_machine.add_transition("State1", "NonExistentState", "Event")
        self.assertEqual(result, "State NonExistentState does not exist.")

    def test_get_state(self):
        state = self.state_machine.get_state("State1")
        self.assertEqual(state, "State1")

    def test_get_invalid_state(self):
        state = self.state_machine.get_state("NonExistentState")
        self.assertEqual(state, None)

    def test_process_event(self):
        result = self.state_machine.process_event("State1", "Event")
        self.assertEqual(result, "Transition successful: State1 -> State2")

if __name__ == "__main__":
    unittest.main()

