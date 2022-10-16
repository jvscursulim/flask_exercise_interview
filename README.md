# Flask job application exercise

## Problem description and instructions:

Nork-Town is a weird place. Crows cawk the misty morning while old men squint. It's a small town, so the mayor had a bright idea to limit the number of cars a person may possess. One person may have up to 3 vehicles. The vehicle, registered to a person, may have one color, 'yellow', 'blue' or 'gray'. And one of three models, 'hatch', 'sedan' or convertible. Carford car shop want a system where they can add car owners and cars. Car owners may not have cars yet, they need to be marked as a sale opportunity. Cars cannot exist in the system without owners.

## Requirements

* Setup the dev environment with docker.
* Using docker-compose with as many volumes as it takes
* Use Python's Flask framework and any other library
* Use any SQL database
* Secure routes
* Write tests

## How to run

### Docker

1. Clonning GitHub repository
```bash
git clone https://github.com/jvscursulim/flask_exercise_job_application
```
2. Accessing the folder with `docker-compose.yml` file
```bash
cd flask_exercise_job_application
```
3. Docker command
```bash
docker-compose up
```
4. To access the web application you need to go to your web browser and write: `localhost:4242` and press enter.

### Local

1. Clonning GitHub repository
```bash
git clone https://github.com/jvscursulim/flask_exercise_job_application
```
2. Accessing project folder
```bash
cd flask_exercise_job_application/flask
```

3. Creating a virtual environment
```bash
python -m venv env
```

4. Activating the virtual environment
* Linux
```bash
source env/bin/activate
```
* Windows
```bash
env/Scripts/Acitave.ps1
```

5. Installing pipenv
```bash
pip install pipenv
```

6. Installing packages with pipenv
```bash
pipenv install
```

7. Running the web app
```bash
python run.py
```

8. To access the web application you need to go to your web browser and write: `localhost:4242` and press enter.

### Tests

1. Clonning GitHub repository
```bash
git clone https://github.com/jvscursulim/flask_exercise_job_application
```
2. Accessing project folder
```bash
cd flask_exercise_job_application/flask
```

3. Creating a virtual environment
```bash
python -m venv env
```

4. Activating the virtual environment
* Linux
```bash
source env/bin/activate
```
* Windows
```bash
env/Scripts/Acitave.ps1
```

5. Installing pipenv
```bash
pip install pipenv
```

6. Installing packages with pipenv
```bash
pipenv install
```

7. Run nox
```bash
nox
```

## References:

1. Grinberg, Miguel. Flask web development: developing web applications with python. " O'Reilly Media, Inc.", 2018.


