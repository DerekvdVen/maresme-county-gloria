# maresme-county-gloria
Welcome to my repository for the technical interview at Earthpulse. Here I will show:
- A flood analysis using radar data. 
- An API to retrieve the results from the analysis.

## Getting Started
To get started, install uv for fast environment building:
https://docs.astral.sh/uv/getting-started/installation/

### To see the results of the analysis:
```
uv run notebook.ipynb
```

### To access results through the api:
```
uv run uvicorn app.main:app
```

Visit for the FastAPI interface: http://127.0.0.1:8000/docs


### Downloading the data
For simplicity’s sake the data is stored in the repository. # move todo add download script

### The pre-processing script is accessible here
https://code.earthengine.google.com/?accept_repo=users/derekvdven/gloria
