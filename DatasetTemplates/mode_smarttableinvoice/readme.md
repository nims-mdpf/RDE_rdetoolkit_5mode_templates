readme

[project]

name = "RDE_StartupTemplate_smarttableinvoice"

version = "1.0"


## How to run

1. requirement python>=3.13
2. pip install -r requirements.txt
3. run : python main.py


## How to run used Dcoker container

1. docker build -t 5mode_operatoin_python13:latest .
2. run : docker run -it --rm  -v "$(pwd)/data":/app/data 5mode_operatoin_python13:latest python /app/main.py


## cleanup for rerun

1. bash cleanup.sh in container/
2. cp ../input/invoice/invoice.json data/invoice/. in container/


Try it!