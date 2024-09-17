# genestack-dashboard
# Genestack Dashboard

A Python dashboard for performing and visualizing bulk RNA-Seq, single-cell RNA-Seq, and single nucleus RNA-Seq analyses using Genestack ODM.

## Features

- **Data Integration**: Seamless access to Genestack ODM data.
- **Analysis Tools**:
  - Bulk RNA-Seq analysis (differential expression, co-expression, pathway analysis).
  - Single-cell and single nucleus RNA-Seq analysis (clustering, classification, differential expression).
- **Visualization**:
  - Interactive plots (heatmaps, scatter plots, PCA, t-SNE/UMAP).
  - Gene expression visualization across samples/conditions.
  - Cell type composition and distribution.
- **Statistical Analysis**:
  - Built-in statistical tests (t-tests, ANOVA).
  - Multiple testing correction (Benjamini-Hochberg).

## Installation

Instructions on how to set up the project locally.

## Usage

Instructions on how to use the dashboard.

## License

This project is licensed under the MIT License.

## Branching Strategy
Use Git branches to manage development:

-main: Stable, production-ready code.
-develop: Latest development code.
-feature/*: Individual features or modules.

## Documentation
Update the docs/ directory with detailed installation and usage instructions as you develop the project.

## Testing
Implement unit tests in the tests/ directory and run them regularly to ensure code quality. 


## Formatting 
- Write docstrings in the [numpy style ](https://peps.python.org/pep-0008/) 
- Format with [black](https://black.readthedocs.io/en/stable/index.html)
- Sort imports with [isort](https://pypi.org/project/isort/)
- add type annotations and check with [pright](https://github.com/microsoft/pyright)


