# pip install fastapi
# pip install uvicorn
from fastapi import FastAPI

app = FastAPI()


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

    return {"Resultado: ": simulationResult, "esAceptado": isAccepted}
