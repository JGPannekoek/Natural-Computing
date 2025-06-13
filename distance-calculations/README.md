# Creation of discretized version of the railway system of the Netherlands

The `map.ipynb` contains the main code that performs the discretization.

- `nodes.csv` and `edges.csv` are from the public public Kaggle [NS: Dutch Railways](https://www.kaggle.com/datasets/jacekpardyak/ns-nederlandse-spoorwegen) repository.
- `script.R` performs the initial pruning of the stations to 34 stations.
- `provincie_2025.geojson` contains geospatial data from [PDOK](https://www.pdok.nl/introductie/-/article/bestuurlijke-gebieden) used to render the topology of the Netherlands.
- `cities.csv` is a manually adapted version containing information on the 53 largest cities in the Netherlands from [here](https://wikikids.nl/Lijst_van_grote_Nederlandse_steden).
- `outline.png` is a manually labelled discretization from the map produced by `map.ipynb`. Green pixels are valid land tiles, and red pixels are station tiles.
- `outline_figure.png` is an altered representation of `outline.png` more suited for presentation in the report.\
- `output.json` contains the discretized representation as a matrix where each cell contains a class index. Here, 0 = invalid, 1 = valid, and 2 = station tile.
- `stations_in_output_json.csv` is a handmade lookup table linking stations to coordinates in image space.
- `stations_of_interest.csv` is produced by `script.R` and contains the information of all stations that were selected for our study.