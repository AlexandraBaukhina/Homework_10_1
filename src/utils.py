import json


def read_transactions_from_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []
    except FileNotFoundError:
        print("File not found")
        return []
    except json.JSONDecodeError:
        print("Invalid JSON file")
        return []
