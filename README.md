# Altlinux Package Comparison CLI

This is a CLI utility to compare binary packages between two branches of the Altlinux database. It fetches package lists from the public REST API and performs a comparison based on architecture and version.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/danilash/altlinux-compare.git
   cd altlinux-compare

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt

3. Install the CLI utility:
    ```bash
    pip install .

## Usage

1. Compare Packages Between Two Branches:
To compare packages between two branches (e.g., sisyphus and p10), run:
    ```bash
    altlinux-compare sisyphus p10

2. Save Results to a File:
You can save the comparison results to a file (e.g., test.json):
    ```bash
    altlinux-compare sisyphus p10 test.json

3. Limit the Number of Packages:
You can limit the number of packages displayed in the output:
    ```bash
    altlinux-compare sisyphus p10 10 test.json