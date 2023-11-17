# pip install fastapi
# pip install uvicorn
from fastapi import FastAPI
import json
from fastapi.middleware.cors import CORSMiddleware
from turing import TuringMachine

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/turingMachine/{cadena}")
async def turning_machine(cadena: str):
    """
    Simula la máquina de Turing con la cadena de entrada dada en el parámetro
    :param cadena: Cadena de entrada
    :return: El resultado de la simulación de la máquina de Turing
    """
    with open("turing.json") as config_file:  # Leer el archivo json
        config = json.load(config_file)

    turing_machine = TuringMachine(**config)  # Crear una instancia de la máquina de Turing

    simulation_result, is_accepted = turing_machine.simulate(cadena)  # Simular la máquina de Turing

    return {"resultado": simulation_result, "aceptado": is_accepted}


@app.get("/json")
async def get_json():
    """
    Obtiene la configuración de la máquina de Turing desde el archivo json
    :return: La configuración de la máquina de Turing, en formato json
    """
    with open("turing.json") as config_file:  # Leer el archivo json
        config = json.load(config_file)

    turing_machine = TuringMachine(**config)  # Crear una instancia de la máquina de Turing

    states_string = ", ".join(turing_machine.states)  # Convertir la lista de estados a una cadena separada por comas
    symbols_string = ", ".join(turing_machine.symbols)
    final_states_string = ", ".join(turing_machine.final_states)
    transitions_string = ", ".join(
        [f"{state}: {transition}" for state, transition in turing_machine.transitions.items()])

    # Regresar la configuración de la máquina de Turing
    return {
        "symbols": symbols_string,
        "states": states_string,
        "initial_state": turing_machine.initial_state,
        "final_states": final_states_string,
        "blank_symbol": turing_machine.blank_symbol,
        "transitions": transitions_string,
    }

