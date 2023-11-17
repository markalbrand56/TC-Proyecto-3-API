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


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/turingMachine/{cadena}")
async def turning_machine(cadena: str):
    # Define the Turing Machine configuration based on the provided JSON
    with open("turing.json") as config_file:
        config = json.load(config_file)

    # Create an instance of the Turing Machine
    turing_machine = TuringMachine(**config)

    simulation_result, is_accepted = turing_machine.simulate(cadena)

    return {"resultado": simulation_result, "aceptado": is_accepted}


@app.get("/json")
async def get_json():
    with open("turing.json") as config_file:
        config = json.load(config_file)

    # Create an instance of the Turing Machine
    turing_machine = TuringMachine(**config)

    return {
        "symbols": turing_machine.symbols,
        "states": turing_machine.states,
        "initial_state": turing_machine.initial_state,
        "final_states": turing_machine.final_states,
        "blank_symbol": turing_machine.blank_symbol,
        "tape": turing_machine.tape,
        "transitions": turing_machine.transitions,
    }

