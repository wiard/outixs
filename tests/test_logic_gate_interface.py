import unittest
from kernel.modules.logic_gate_interface import LogicGateInterface

class TestLogicGateInterface(unittest.TestCase):

    def setUp(self):
        self.logic_gate = LogicGateInterface()
        self.gate_data = {
            "gate_id": "AND1",
            "gate_type": "AND",
            "inputs": [1, 1],
            "output": 1
        }

    def test_create_logic_gate(self):
        result = self.logic_gate.create_gate(
            self.gate_data["gate_id"], 
            self.gate_data["gate_type"], 
            self.gate_data["inputs"], 
            self.gate_data["output"]
        )
        self.assertEqual(result, "Logic gate AND1 created successfully.")

    def test_get_logic_gate(self):
        self.logic_gate.create_gate(
            self.gate_data["gate_id"], 
            self.gate_data["gate_type"], 
            self.gate_data["inputs"], 
            self.gate_data["output"]
        )
        result = self.logic_gate.get_gate("AND1")
        self.assertEqual(result["gate_type"], "AND")
        self.assertEqual(result["inputs"], [1, 1])
        self.assertEqual(result["output"], 1)

    def test_update_logic_gate(self):
        self.logic_gate.create_gate(
            self.gate_data["gate_id"], 
            self.gate_data["gate_type"], 
            self.gate_data["inputs"], 
            self.gate_data["output"]
        )
        updated_data = {
            "gate_type": "OR",
            "inputs": [0, 1],
            "output": 1
        }
        result = self.logic_gate.update_gate(
            "AND1", 
            updated_data["gate_type"], 
            updated_data["inputs"], 
            updated_data["output"]
        )
        self.assertEqual(result, "Logic gate AND1 updated successfully.")
        updated_gate = self.logic_gate.get_gate("AND1")
        self.assertEqual(updated_gate["gate_type"], "OR")
        self.assertEqual(updated_gate["inputs"], [0, 1])
        self.assertEqual(updated_gate["output"], 1)

    def test_delete_logic_gate(self):
        self.logic_gate.create_gate(
            self.gate_data["gate_id"], 
            self.gate_data["gate_type"], 
            self.gate_data["inputs"], 
            self.gate_data["output"]
        )
        result = self.logic_gate.delete_gate("AND1")
        self.assertEqual(result, "Logic gate AND1 deleted successfully.")

    def test_logic_gate_not_found(self):
        with self.assertRaises(ValueError) as context:
            self.logic_gate.get_gate("non_existent_gate")
        self.assertEqual(str(context.exception), "Logic gate not found")

if __name__ == "__main__":
    unittest.main()

