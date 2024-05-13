

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

`venv/Scripts/activate`

on macOS/Linux

`venv/bin/activate`

# Managing the Stack(Backend)
## Install Dependencies

1. Install the backend dependencies

    `pip install -r requirements.txt`


## Stack management

1. Open a command prompt at the root of the application's folder.

2. add a new .env file and then the codes in the env.simple in . env
3. Run: `docker-compose up -d --build`
3. View Container: `docker ps`

4. Go inside a Container: `docker exec -it <nodeContainerID> sh` (replace <nodeContainerID>)
5. Stop containers : `docker-compose down`
6. Stop all running Containers: `docker stop $(docker ps -aq)`
7. remove all Containers: `docker rm $(docker ps -aq)`

## Run the Application

    docker-compose up --build
