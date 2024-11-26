class StateMachineInterface:
    def __init__(self):
        self.states = {}
        self.transitions = {}

    def add_state(self, state_name):
        if state_name not in self.states:
            self.states[state_name] = state_name
            return "State added successfully"
        return "State already exists"

    def add_transition(self, from_state, to_state, event):
        if from_state not in self.states or to_state not in self.states:
            return f"State {to_state} does not exist."
        if from_state not in self.transitions:
            self.transitions[from_state] = []
        self.transitions[from_state].append((event, to_state))
        return "Transition added successfully"

    def get_state(self, state_name):
        return self.states.get(state_name, None)

    def process_event(self, current_state, event):
        if current_state not in self.transitions:
            return "No transitions available for this state"
        for transition_event, to_state in self.transitions[current_state]:
            if transition_event == event:
                return f"Transition successful: {current_state} -> {to_state}"
        return "Event not valid for current state"

if __name__ == "__main__":
    sm = StateMachineInterface()
    sm.add_state("State1")
    sm.add_state("State2")
    sm.add_transition("State1", "State2", "Event1")
    print(sm.process_event("State1", "Event1"))

