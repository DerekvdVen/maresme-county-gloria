# maresme-county-gloria

Welcome to my repository for the technical interview at Earthpulse. Here I will show:

- A flood analysis using radar data.
- An API to retrieve the results from the analysis.

## Getting Started

To get started, install uv for fast environment building:
https://docs.astral.sh/uv/getting-started/installation/

### To see the results of the analysis:

Open app/analysis.ipynb in your favorite IDE

### To access results through the api:

```
uv run uvicorn app.main:app
```

Visit for the FastAPI interface: http://127.0.0.1:8000/docs

### Downloading the data

For simplicity’s sake the data is stored in the repository.
In the data folder you will find:
- Before and after VV satellite data + geometry extent
  - The satellite data pre-processing script is accessible here or you can see it in `get_data/get_VV_radar_before_and_after_flood.js`
- Population data Spain 2020
  - Downloaded from https://data.humdata.org/dataset/worldpop-population-density-for-spain
- 

https://code.earthengine.google.com/16895a51f272ea72bf87a3fd4ffff81b?accept_repo=users%2Fderekvdven%2Fgloria
