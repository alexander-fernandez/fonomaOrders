# fonomaOrders

    $ python -m venv .venv
    $ python -m pip install --upgrade pip
    # Windows
    $ .\.venv\Scripts\activate.ps1
    # Linux 
    $ source env/bin/activate
    ...Or just select the virtual environment right in your favorite IDE. Then...
    $ pip install -r requirements.txt
    $ pytest -v
    $ uvicorn main:app --host 0.0.0.0 --port 8080 --reload