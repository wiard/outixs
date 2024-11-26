class LogicGateInterface:
    def __init__(self):
        self.gates = {}

    def create_gate(self, gate_type, inputs, output):
        self.gates[output] = {"gate_type": gate_type, "inputs": inputs, "output": output}
        return "Logic gate created successfully"

    def update_gate(self, output, gate_type, inputs, new_output):
        if output in self.gates:
            self.gates[output] = {"gate_type": gate_type, "inputs": inputs, "output": new_output}
            return "Logic gate updated successfully"
        return "Logic gate not found"

    def delete_gate(self, output):
        if output in self.gates:
            del self.gates[output]
            return "Logic gate deleted successfully"
        return "Logic gate not found"

    def get_gate(self, output):
        if output in self.gates:
            return self.gates[output]
        raise ValueError(f"Gate with ID {output} not found.")

