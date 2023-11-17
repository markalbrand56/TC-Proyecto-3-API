import json


class TuringMachine:
    def __init__(self, symbols, states, initial_state, final_states, blank_symbol, transitions, tape=None):
        self.symbols = symbols  # Alfabeto
        self.states = states  # Estados
        self.initial_state = initial_state  # Estado inicial
        self.final_states = final_states  # Estados finales
        self.blank_symbol = blank_symbol  # Símbolo blanco
        self.transitions = transitions  # Transiciones
        self.tape = tape  # Cinta

    def reset_tape(self, input_string: str) -> None:
        """Reinicia la cinta con la cadena de entrada y el símbolo en blanco"""
        self.tape = list(input_string)
        self.tape.append(self.blank_symbol)

    def simulate(self, input_string: str) -> tuple[list[str], bool]:
        """
        Simula la máquina de Turing con la cadena de entrada dada.
        Los movimientos son: R (derecha), L (izquierda). Los demás serán ignorados.
        :param input_string: Cadena de entrada
        :return: Una tupla con la lista de pasos de la simulación y un booleano que indica si la cadena fue aceptada
        """
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
            # tape_position += 1 if action[2] == "R" else -1
            if action[2] == "R":
                tape_position += 1
            elif action[2] == "L":
                tape_position -= 1

            # Record the step in the derivation process
            tape_view = ''.join(self.tape)
            step_info = f"State: {current_state}, Tape: {tape_view}, Head Position: {tape_position}"
            derivation_process.append(step_info)

        is_accepted = current_state in self.final_states
        return derivation_process, is_accepted


if __name__ == "__main__":
    # TEST
    with open("turing.json") as config_file:
        config = json.load(config_file)

    turing_machine = TuringMachine(**config)  # Leer el archivo json y crear una instancia de la máquina de Turing

    input_string = "100000100"
    simulation_result, was_accepted = turing_machine.simulate(input_string)

    print(was_accepted)
    for step in simulation_result:
        print(step)
