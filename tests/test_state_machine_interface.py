import unittest
from kernel.modules.state_machine_interface import StateMachineInterface

class TestStateMachineInterface(unittest.TestCase):

    def setUp(self):
        self.state_machine = StateMachineInterface()

    def test_create_machine(self):
        result = self.state_machine.create_machine("TestMachine")
        self.assertEqual(result, "State machine created successfully")

    def test_add_state(self):
        self.state_machine.create_machine("TestMachine")
        result = self.state_machine.add_state("TestMachine", "State1")
        self.assertEqual(result, "State added successfully")

    def test_add_transition(self):
        self.state_machine.create_machine("TestMachine")
        self.state_machine.add_state("TestMachine", "State1")
        self.state_machine.add_state("TestMachine", "State2")
        result = self.state_machine.add_transition("TestMachine", "State1", "State2", "Event")
        self.assertEqual(result, "Transition added successfully")

    def test_get_machine(self):
        self.state_machine.create_machine("TestMachine")
        self.state_machine.add_state("TestMachine", "State1")
        result = self.state_machine.get_gate("TestMachine")
        self.assertIn("State1", result["states"])

    def test_state_machine_not_found(self):
        with self.assertRaises(ValueError) as context:
            self.state_machine.get_gate("NonExistentMachine")
        self.assertEqual(str(context.exception), "Gate with ID NonExistentMachine not found.")

if __name__ == "__main__":
    unittest.main()

