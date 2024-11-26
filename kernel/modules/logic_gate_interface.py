class LogicGateInterface:
    def __init__(self):
        self.gates = {}

    def create_gate(self, gate_id, gate_type, inputs, output):
        if gate_id in self.gates:
            raise ValueError(f"Gate with ID {gate_id} already exists.")
        self.gates[gate_id] = {
            "gate_type": gate_type,
            "inputs": inputs,
            "output": output
        }
        return f"Logic gate {gate_id} created successfully."

    def get_gate(self, gate_id):
        gate = self.gates.get(gate_id)
        if not gate:
            raise ValueError(f"Logic gate not found")
        return gate

    def update_gate(self, gate_id, gate_type=None, inputs=None, output=None):
        if gate_id not in self.gates:
            raise ValueError(f"Logic gate not found")
        
        if gate_type:
            self.gates[gate_id]["gate_type"] = gate_type
        if inputs:
            self.gates[gate_id]["inputs"] = inputs
        if output:
            self.gates[gate_id]["output"] = output
        return f"Logic gate {gate_id} updated successfully."

    def delete_gate(self, gate_id):
        if gate_id not in self.gates:
            raise ValueError(f"Logic gate not found")
        del self.gates[gate_id]
        return f"Logic gate {gate_id} deleted successfully."

