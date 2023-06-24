# Analyze Radius Query Performance Benchmarking Results

The purpose of this repository is to provide the scripts used to create the boxplots and compute the confidence intervals for the Radius Query Performance Benchmarking.

## Prerequisites

- Python 3
- pip3
- unzip

### Getting Started

- #### Clone Repository

  `git clone https://github.com/Radius-Query-Performance-Benchmarking/Analyze_Results.git`

- #### Change Directory

  `cd ./Analyze_Results`

- #### Download Load Testing Results

  `curl -o Results.zip "https://zenodo.org/record/8077663/files/Results.zip?download=1"`

- #### Unzip Results.zip

  `unzip Results.zip && rm Results.zip`

- #### Install Dependencies (venv is suggested)

  `pip install -r requirements.txt`

- #### Grant Execute Permission

  `chmod +x ./execute_script_vus.sh`

- #### Analyze Load Testing Results based on the number of virtual users

  `./execute_script_vus.sh`

- #### Grant Execute Permission

  `chmod +x ./execute_script_records.sh`

- #### Analyze Load Testing Results based on the number of records

  `./execute_script_records.sh`

## Boxplot Graphs & Confidence Intervals

After the [execute_script_vus.sh](./execute_script_vus.sh) & [execute_script_records.sh](./execute_script_records.sh) scripts have been executed, the boxplot graphs & the confidence intervals would be located in the appropriate directories under the `./Plots` directory.

## Author

- Ioannis Papadatos (t8190314@aueb.gr)
