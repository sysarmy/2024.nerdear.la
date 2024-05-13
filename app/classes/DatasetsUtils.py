import json
import csv


class DatasetError(Exception):
    pass


class DatasetsUtils:
    @staticmethod
    def remove_trailing_whitespace(dictionary_list):
        """
        Removes initial and final trailing whitespaces from keys and values of each dictionary in a list.

        Args:
            dictionary_list (list): List of dictionaries.

        Returns:
            list: List of dictionaries with updated keys and values.

        Raises:
            DatasetError: If there is an error processing the dictionary list.
        """
        try:
            processed_list = []

            if not isinstance(dictionary_list, list):
                raise TypeError("Invalid input. Expected a list of dictionaries.")

            for dictionary in dictionary_list:
                processed_dict = {}
                for key, value in dictionary.items():
                    # Remove trailing whitespaces from the key
                    processed_key = key.strip()
                    processed_value = value.strip() if isinstance(value, str) else value
                    processed_dict[processed_key] = processed_value

                processed_list.append(processed_dict)

            return processed_list
        except Exception as e:
            raise DatasetError(f"An error occurred while processing the dictionary list: {e}")

    @staticmethod
    def convert_key_values_to_lowercase(dictionary_list, key):
        """
        Convert the values of a specified key in a list of dictionaries to lowercase.

        Args:
            dictionary_list (list): A list of dictionaries.
            key (str): The key whose values need to be converted to lowercase.

        Raises:
            DatasetError: If there is an error converting the key values to lowercase.
        """
        try:
            for item in dictionary_list:
                if not isinstance(item, dict):
                    raise TypeError("Invalid dictionary encountered in the list.")

                if key not in item:
                    raise KeyError(f"Key '{key}' not found in dictionary.")

                value = item[key]
                if not isinstance(value, str):
                    raise TypeError(f"Value for key '{key}' is not a string.")
                item[key] = value.lower()
        except Exception as e:
            raise DatasetError(f"An error occurred while converting key values to lowercase: {e}")

    @staticmethod
    def csv_to_list_of_dicts(csv_file_path):
        """
        Read a CSV file and convert its contents into a list of dictionaries.

        Args:
            csv_file_path (str): The path to the CSV file.

        Raises:
            DatasetError: If there is an error reading or parsing the CSV file.

        Returns:
            list: A list of dictionaries representing the CSV data. Each dictionary corresponds to a row in the CSV file,
                with column names as keys and cell values as values.
        """
        data = []
        try:
            with open(csv_file_path, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    data.append(row)
            return data
        except FileNotFoundError as e:
            raise DatasetError(f"File not found: {csv_file_path}")
        except IsADirectoryError as e:
            raise DatasetError(f"Expected a file, but got a directory: {csv_file_path}")
        except PermissionError as e:
            raise DatasetError(f"Permission denied to access file: {csv_file_path}")
        except csv.Error as e:
            raise DatasetError(f"Error parsing CSV file: {e}")

    @staticmethod
    def read_json_file(json_file_path):
        """
        Read a JSON file and load its contents into a dictionary.

        Args:
            json_file_path (str): The path to the JSON file.

        Raises:
            DatasetError: If there is an error reading or parsing the JSON file.

        Returns:
            dict: A dictionary representing the JSON data loaded from the file.
        """
        try:
            with open(json_file_path, "r") as json_file:
                data = json.load(json_file)
            return data
        except FileNotFoundError as e:
            raise DatasetError(f"File not found: {json_file_path}")
        except IsADirectoryError as e:
            raise DatasetError(f"Expected a file, but got a directory: {json_file_path}")
        except PermissionError as e:
            raise DatasetError(f"Permission denied to access file: {json_file_path}")
        except json.JSONDecodeError as e:
            raise DatasetError(f"Error parsing JSON file: {e}")
        except Exception as e:
            raise DatasetError(f"An error occurred: {e}")
