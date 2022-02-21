# Simple request app with Flask

## HOW TO USE THIS CODE

1) Create a new virtual environment: `python -m venv .venv`
2) Activate the virtual environment:

In powershell:

```powershell
.\.venv\Scripts\activate
```

In bash

```bash
source .venv/Scripts/activate
```

In Mac OS / Linux:

```bash
source .venv/bin/activate
```

In CMD

```cmd
.venv\Scripts\activate
```

3) Install the dependencies with the command:

```
pip install -r requirements.txt
```

4) Verify that the file `.flaskenv` is in the top directory and that it contains the environment variable `FLASK_APP=src.app`.

5) Run the app

```
flask run
```

6) Visit http://127.0.0.1:5000/ to see the recovered data.