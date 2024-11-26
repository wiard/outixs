class StateMachineInterface:
    def __init__(self):
        self.machines = {}

    def create_machine(self, machine_name):
        if machine_name in self.machines:
            raise ValueError(f"Machine {machine_name} already exists.")
        self.machines[machine_name] = {"states": [], "transitions": []}
        return "State machine created successfully"

    def add_state(self, machine_name, state_name):
        if machine_name not in self.machines:
            raise ValueError(f"Machine {machine_name} does not exist.")
        self.machines[machine_name]["states"].append(state_name)
        return "State added successfully"

    def add_transition(self, machine_name, from_state, to_state, event):
        if machine_name not in self.machines:
            raise ValueError(f"Machine {machine_name} does not exist.")
        if from_state not in self.machines[machine_name]["states"]:
            raise ValueError(f"State {from_state} does not exist.")
        if to_state not in self.machines[machine_name]["states"]:
            raise ValueError(f"State {to_state} does not exist.")
        self.machines[machine_name]["transitions"].append(
            {"from": from_state, "to": to_state, "event": event}
        )
        return "Transition added successfully"

    def get_gate(self, gate_id):
        if gate_id not in self.machines:
            raise ValueError(f"Gate with ID {gate_id} not found.")
        return self.machines[gate_id]

