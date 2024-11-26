import unittest
from kernel.modules.logic_gate_interface import LogicGateInterface

class TestLogicGateInterface(unittest.TestCase):

    def setUp(self):
        self.logic_gate = LogicGateInterface()

    def test_create_logic_gate(self):
        gate_data = {
            "gate_type": "AND",
            "inputs": ["input1", "input2"],
            "output": "output1"
        }
        result = self.logic_gate.create_gate(gate_data["gate_type"], gate_data["inputs"], gate_data["output"])
        self.assertEqual(result, "Logic gate created successfully")

    def test_update_logic_gate(self):
        gate_data = {
            "gate_type": "AND",
            "inputs": ["input1", "input2"],
            "output": "output1"
        }
        self.logic_gate.create_gate(gate_data["gate_type"], gate_data["inputs"], gate_data["output"])
        updated_gate_data = {
            "gate_type": "OR",
            "inputs": ["input1", "input2"],
            "output": "output2"
        }
        result = self.logic_gate.update_gate(gate_data["output"], updated_gate_data["gate_type"], updated_gate_data["inputs"], updated_gate_data["output"])
        self.assertEqual(result, "Logic gate updated successfully")

    def test_delete_logic_gate(self):
        gate_data = {
            "gate_type": "AND",
            "inputs": ["input1", "input2"],
            "output": "output1"
        }
        self.logic_gate.create_gate(gate_data["gate_type"], gate_data["inputs"], gate_data["output"])
        result = self.logic_gate.delete_gate(gate_data["output"])
        self.assertEqual(result, "Logic gate deleted successfully")

    def test_get_logic_gate(self):
        gate_data = {
            "gate_type": "AND",
            "inputs": ["input1", "input2"],
            "output": "output1"
        }
        self.logic_gate.create_gate(gate_data["gate_type"], gate_data["inputs"], gate_data["output"])
        result = self.logic_gate.get_gate(gate_data["output"])
        self.assertEqual(result, gate_data)

    def test_logic_gate_not_found(self):
        with self.assertRaises(ValueError):
            self.logic_gate.get_gate("non_existent_gate")

if __name__ == "__main__":
    unittest.main()

