import os
import unittest
from urllib.error import URLError
import csv
import connecting_food as csv_download_split


def test_download_file():
    """
    test download file
    """
    url = "https://github.com/Connecting-Food/technical-test/raw/master/small.csv"
    filename = "test_download.csv"
    csv_download_split.download_file(url, filename)
    unittest.TestCase.assertTrue(os.path.exists(filename), True)
    os.remove(filename)

    # Test invalid URL
    invalid_url = "https://invalidurl.com/nonexistent.csv"
    with unittest.TestCase.assertRaises(URLError, BaseException):
        csv_download_split.download_file(invalid_url, filename)


def test_split_file():
    """
    test splitting file
    """
    input_file = "test_input.csv"
    output_directory = "test_output"
    max_lines = 2

    # Create a test input file
    with open(input_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                "producer_id",
                "producer_name",
                "product_id",
                "product_name",
                "product_unit",
                "quantity",
                "specifications_id",
                "delivery_datetime",
                "destination_country_code",
            ]
        )
        writer.writerow(
            [
                "1",
                "Producer 1",
                "10001",
                "Product 1",
                "kg",
                "10",
                "123",
                "2021-01-01 10:00:00",
                "US",
            ]
        )
        writer.writerow(
            [
                "2",
                "Producer 2",
                "10001",
                "Product 2",
                "kg",
                "20",
                "456",
                "2021-01-01 12:00:00",
                "FR",
            ]
        )
        writer.writerow(
            [
                "3",
                "Producer 3",
                "10002",
                "Product 3",
                "kg",
                "30",
                "789",
                "2021-01-02 10:00:00",
                "US",
            ]
        )

    # Perform the file splitting
    csv_download_split.split_file(input_file, output_directory, max_lines)

    # Check the generated output files
    expected_output_files = [
        "20210101_US.csv",
        "20210101_FR.csv",
    ]

    unittest.TestCase.assertTrue(os.path.exists(output_directory), True)
    for output_file in expected_output_files:
        unittest.TestCase.assertTrue(
            os.path.exists(os.path.join(output_directory, output_file)), True
        )

    # Clean up the test files and directory
    os.remove(input_file)
    for output_file in expected_output_files:
        os.remove(os.path.join(output_directory, output_file))
    os.rmdir(output_directory)
