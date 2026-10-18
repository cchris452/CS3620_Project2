# CS3620 Project 2: Mad Libs

A Django word game. Fill in seven prompts to generate a random story, then browse saved stories.

## Run locally

From the workspace root, install Django if needed and start the development server:

```powershell
python -m pip install Django
python CS3620_Project2/cs3620project2/manage.py migrate
python CS3620_Project2/cs3620project2/manage.py runserver
```

Open `http://127.0.0.1:8000/` in a browser. Run the app checks and tests with:

```powershell
python CS3620_Project2/cs3620project2/manage.py check
python CS3620_Project2/cs3620project2/manage.py test madlibs
```
