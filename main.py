# pip install fastapi
# pip install uvicorn
from fastapi import FastAPI
import json
from turing import TuringMachine
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

    simulationResult, isAccepted = turing_machine.simulate(cadena)

    return {"resultado": simulationResult, "aceptado": isAccepted}
