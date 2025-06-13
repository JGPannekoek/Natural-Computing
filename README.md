# Slime Mold Foraging Simulation & Dutch Rail Network Analysis

This repository contains code and data for simulating slime mold-inspired network formation and comparing it to the Dutch railway network. The project uses JAX for simulation, NetworkX for graph analysis, and various Python tools for data processing and visualization.

---

## Project Structure

```
.
├── experiment_pipeline.ipynb
├── noise_custom.py
├── distance-calculations/
│   ├── map.ipynb
│   ├── output.json
│   ├── outline.png
│   ├── nodes.csv
│   ├── edges.csv
│   ├── stations_of_interest.csv
│   └── ... (other geo/data files)
├── experiment_outputs_different_starts/
├── experiment_outputs_same_starts/
├── results/
│   ├── analysis.ipynb
│   ├── process_experiments.ipynb
│   ├── plot_networks.ipynb
│   └── ... (plots, CSVs)
├── gifs/
├── imgs/
└── Swarm_Urbanism/
```

---

## Main Components

### 1. **experiment_pipeline.ipynb**
- **Purpose:** The core simulation pipeline. Runs the JAX-based slime mold foraging simulation, generating agent trajectories as they explore a grid with station targets.
- **Key Features:**
  - Loads the simulation grid from `distance-calculations/output.json`.
  - Uses Perlin noise (from `noise_custom.py`) for stochastic agent movement.
  - Runs multiple experiments with both fixed and random starting positions.
  - Saves results (agent trails, nuclei, etc.) as `.npz` files in `experiment_outputs_same_starts/` and `experiment_outputs_different_starts/`.

### 2. **noise_custom.py**
- **Purpose:** Custom Perlin noise generator for agent movement.
- **Key Features:** Implements a Perlin noise class and a multi-octave noise function for smooth, reproducible random walks.

### 3. **distance-calculations/**
- **Purpose:** Contains all data and code for generating the simulation grid and mapping real-world coordinates to the simulation space.
- **Key Files:**
  - `map.ipynb`: Generates the simulation grid, overlays stations, and saves the grid as `output.json`.
  - `output.json`: The grid used by the simulation, encoding land, water, and station locations.
  - `nodes.csv`, `edges.csv`: Data for the Dutch railway network.
  - `outline.png`: Image used for grid generation.
  - `map.html`: Interactive map visualization.

### 4. **experiment_outputs_same_starts/** & **experiment_outputs_different_starts/**
- **Purpose:** Store simulation results.
- **Contents:** Each `.npz` file contains the agent trajectories, nuclei positions, station locations, and other metadata for a single experiment. Associated `.distances.json` and `.weighted.edgelist` files store computed network properties for further analysis.

### 5. **results/**
- **Purpose:** Analysis and visualization of simulation and real-world networks.
- **Key Notebooks:**
  - `process_experiments.ipynb`: Processes simulation outputs, builds graphs, computes network metrics (cost, travel time, vulnerability), and saves summary CSVs.
  - `analysis.ipynb`: Loads processed results, normalizes metrics, and generates comparative plots between simulation and Dutch railway networks.
  - `plot_networks.ipynb`: Visualizes the generated networks and overlays them on the simulation grid.
- **Other Files:** Plots and CSVs summarizing results.

### 6. **gifs/**, **imgs/**, **Swarm_Urbanism/**
- **Purpose:** Store generated images, animations, and possibly additional project materials or references.

---

## Workflow Overview

1. **Grid Generation:**  
   Use [`distance-calculations/map.ipynb`](distance-calculations/map.ipynb) to generate the simulation grid (`output.json`) and map station locations. Note that this step includes a manual photoshop step.

2. **Simulation:**  
   Run [`experiment_pipeline.ipynb`](experiment_pipeline.ipynb) to simulate slime mold foraging, saving results in the appropriate output folder.

3. **Network Processing:**  
   Use [`results/process_experiments.ipynb`](results/process_experiments.ipynb) to build graphs from simulation outputs and compute network metrics.

4. **Analysis & Visualization:**  
   Use [`results/analysis.ipynb`](results/analysis.ipynb) for statistical analysis and plotting.  
   Use [`results/plot_networks.ipynb`](results/plot_networks.ipynb) for visualizing the networks.

---

## Data Files

- **distance-calculations/nodes.csv, edges.csv, stations_of_interest.csv:**  
  Dutch railway network data and station locations.
- **distance-calculations/output.json:**  
  Simulation grid (land, water, stations).

---

## Notes

- All simulation and analysis code is in Python (JAX, NumPy, NetworkX, Pandas, Matplotlib, Plotnine, etc.).
- The project is modular: grid generation, simulation, and analysis are separated for clarity and reproducibility.
- Results are saved in a structured format for easy downstream analysis.

---

## Getting Started

1. Generate the grid using `distance-calculations/map.ipynb`.
2. Run simulations with `experiment_pipeline.ipynb`.
3. Process and analyze results using the notebooks in `results/`.

---

## Contact

For questions, please contact the repository author.
