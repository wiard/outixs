echo "# State Machine Interface" > interfaces/state_machine_interface.py
echo "class FiniteStateMachineInterface:" >> 
interfaces/state_machine_interface.py
echo "    def __init__(self, initial_state):" >> 
interfaces/state_machine_interface.py
echo "        self.current_state = initial_state" >> 
interfaces/state_machine_interface.py
echo "    def transition(self, input_data):" >> 
interfaces/state_machine_interface.py
echo "        raise NotImplementedError('Must implement transition 
method')" >> interfaces/state_machine_interface.py

