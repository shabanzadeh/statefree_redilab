

# Setting up Virtual Environment
To set up a virtual environment for this application, follow these steps:

1. Open a command prompt at the root of the application's folder (REDLAB).
2. Create a directory named venv:

    `mkdir venv`
3. Navigate into 'venv

    `cd venv`

4. create a virtual enviroment named 'redilab' using Python's 'venv' module: 

    ` python -m venv redilab`

5. activate the virtual enviroment 

on Windows:

    `cd venv/Scripts/activate`

on macOS/Linux

    `cd venv/bin/activate`
# Managing the Stack(Backend)
## Install Dependencies

1. Install the backend dependencies

    `pip install -r requirements.txt`

2. Additionally, install FastAPI, MongoDB and Uvicorn

    `pip install fastapi mongodb uvicorn`

## Run the Application

    `Run: uvicorn main:app --reload`
