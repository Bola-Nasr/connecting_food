# CSV File Splitter

This script allows you to split a CSV file based on date and country code. It reads a CSV file, filters the rows based on specific criteria, and splits the data into multiple smaller CSV files, each containing a subset of the original data based on the date and country code.

## Prerequisites
- Python 3.x
- Required Python packages: urllib, os, sys, csv, pycountry

## Installation

- Clone the repository or download the script file to your local machine.

- Install the required Python packages by running the following command:

```
pip install pycountry
```

## Usage

1- Open a terminal or command prompt.

2- Navigate to the directory where the script is located.

3- Run the script with the following command:


```
python csv_file_splitter.py <input_arg>
```

Replace <input_arg> with one of the following options: large, medium, or small. This argument specifies the size of the input file and the maximum number of lines allowed in each output file.

For example, to split a large CSV file, run:

```
python csv_file_splitter.py large
```

4- The script will download the input file from the specified URL and save it locally.

5- It will then split the file based on date and country code, creating separate output files for each combination. The output files will be saved in a directory named <input_file>_output, where <input_file> is the name of the input file without the file extension.

## Run test
```
cd connecting_food && pytest
```

## Customization

You can customize the behavior of the script by modifying the following constants in the constants/constants.py file:

- URL: The base URL from which the input files will be downloaded.

- LARGE, MEDIUM, SMALL: Constants representing the input file names and corresponding maximum line counts for each file size.

- DATA: A dictionary mapping the file sizes (large, medium, small) to their respective maximum line counts.

