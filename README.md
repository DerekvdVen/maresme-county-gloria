# maresme-county-gloria

Welcome to my repository for the technical exercise at Earthpulse. This repository contains a flood analysis using radar data and includes an API to retrieve the results of the analysis. Below are the key components of the project:
- app/ - The api and processing code
- tests/ - unit tests for the app
- presentation/ - pwpt and pdf presentation of the process
- data/ - data utilized in the project
- get_data/ - scripts that were used to retrieve data
- analysis.ipynb - notebook with visualisation

## Getting Started

To get started, install uv for fast environment building:
https://docs.astral.sh/uv/getting-started/installation/

### To see the results of the analysis:

Open `analysis.ipynb` in your favorite IDE or view a powerpoint presentation or pdf in presentation/

### To access results through the api:

```
uv run uvicorn app.main:app
```
Visit http://127.0.0.1:8000/docs for the FastAPI interface: 

See the tests for an example on how to use the api.

### Tests

To run the tests simply call:
```commandline
uv run pytest tests
```

### Downloading the data

For simplicity’s sake the data is stored in the repository.
In the data folder you will find:
- Before and after VV satellite data + geometry extent
  - The satellite data pre-processing script is accessible here (https://code.earthengine.google.com/16895a51f272ea72bf87a3fd4ffff81b?accept_repo=users%2Fderekvdven%2Fgloria
) or you can see it in `get_data/get_VV_radar_before_and_after_flood.js`
- Population data Spain 2020
  - Downloaded from https://data.humdata.org/dataset/worldpop-population-density-for-spain



