import json
from json import JSONDecodeError


# build a function that return a json file given the route.
# This function will be called by the main.py file
def get_json(route):
    with open(route) as config_file:
        config = json.load(config_file)
    return config


class TuringMachine():

    def __init__(self, symbols, states, initial_state, final_states, blank_symbol, transitions, tape=None):
        self.symbols = symbols
        self.states = states
        self.initial_state = initial_state
        self.final_states = final_states
        self.blank_symbol = blank_symbol
        self.transitions = transitions
        self.tape = tape

    def reset_tape(self, input_string):
        self.tape = list(input_string)
        self.tape.append(self.blank_symbol)

    def simulate(self, input_string):
        self.reset_tape(input_string)
        current_state = self.initial_state
        tape_position = 0
        derivation_process = []

        while current_state not in self.final_states and tape_position < len(self.tape):
            current_symbol = self.tape[tape_position]
            action = self.transitions[current_state][current_symbol]

            # Update the tape, state, and tape position
            self.tape[tape_position] = action[1]
            current_state = action[0]
            tape_position += 1 if action[2] == "R" else -1

            # Record the step in the derivation process
            tape_view = ''.join(self.tape)
            step_info = f"State: {current_state}, Tape: {tape_view}, Head Position: {tape_position}"
            derivation_process.append(step_info)

        is_accepted = current_state in self.final_states
        return derivation_process, is_accepted



if __name__ == "__main__":
    # Define the Turing Machine configuration based on the provided JSON
    with open("turing.json") as config_file:
        config = json.load(config_file)

    # Create an instance of the Turing Machine
    turing_machine = TuringMachine(**config)

    # Test the Turing Machine simulation with an example input string
    input_string = "1001"
    simulation_result, was_accepted = turing_machine.simulate(input_string)

    print(was_accepted)
    for step in simulation_result:
        print(step)

