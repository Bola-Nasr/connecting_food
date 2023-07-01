import csv
import urllib.request
import os
import sys
from constants.constants import *
import pycountry


def download_file(url, filename):
    """
    """
    urllib.request.urlretrieve(url, filename)

def is_valid(row, headers):
    """
    """
    if len(row) != len(headers):
        return False  # Skip rows with incorrect number of columns

    try:
        product_id = int(row[2])
        if not pycountry.countries.get(alpha_2=row[8].strip()):
            return False  # ISO code is invalid
    except (ValueError, IndexError):
        return False # Skip rows with invalid product_id or destination_country_code

    if product_id != 10001:
        return False  # Skip rows with product_id other than 10001

    return True

def split_file(input_file, output_directory, max_lines):
    """
    """
    with open(input_file, "r", newline="") as file:
        reader = csv.reader(file, delimiter=",")
        headers = next(reader)  # Skip the header line

        data = {}

        for row in reader:
            if not is_valid(row,headers):
                continue
            
            destination_country_code = row[8].strip()
            data_date = row[7].split(" ")[0]
            if data_date not in data:
                data[data_date] = {}
            if destination_country_code not in data[data_date]:
                data[data_date][destination_country_code] = []
            data[data_date][destination_country_code].append(row)

    os.makedirs(output_directory, exist_ok=True)

    for date, countries in data.items():
        for country_code, rows in countries.items():
            output_file = os.path.join(
                output_directory, f'{date.replace("-", "")}_{country_code}.csv'
            )
            with open(output_file, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(headers)
                writer.writerows(rows[:max_lines])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError(
            "Wrong number of arguments. Should be one of: large, medium, small"
        )

    input_arg = sys.argv[1]
    input_arg = input_arg.lower()

    if input_arg == "large":
        url = f"{URL}{LARGE}.csv"
        max_lines = DATA[LARGE]
    elif input_arg == "medium":
        url = f"{URL}{MEDIUM}.csv"
        max_lines = DATA[MEDIUM]
    elif input_arg == "small":
        url = f"{URL}{SMALL}.csv"
        max_lines = DATA[SMALL]
    else:
        raise ValueError("Wrong argument. Should be one of: large, medium, small")

    input_file = url.split("/")[-1]
    output_directory = f'{input_file.split(".")[0]}_output'

    # Download the file
    download_file(url, input_file)

    # Split the file by date and country code
    split_file(input_file, output_directory, max_lines)
