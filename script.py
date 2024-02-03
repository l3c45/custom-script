import json
import sys

def replace_value(json_data, value_to_replace, new_value):
    if isinstance(json_data, dict):
        for key, value in json_data.items():
            if isinstance(value, (dict, list)):
                replace_value(value, value_to_replace, new_value)
            elif value == value_to_replace:
                json_data[key] = new_value
    elif isinstance(json_data, list):
        for item in json_data:
            if isinstance(item, (dict, list)):
                replace_value(item, value_to_replace, new_value)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <original_json_file> <value_to_replace> <new_value>")
        sys.exit(1)

    # Path to the original JSON file
    original_json_file = sys.argv[1]

    # Value to replace and new value
    value_to_replace = sys.argv[2]
    new_value = sys.argv[3]

    # Open the original JSON file in read mode
    with open(original_json_file, "r") as f:
        # Load the JSON content
        data = json.load(f)

        # Perform recursive replacement
        replace_value(data, value_to_replace, new_value)

    # Write the modified data to the same JSON file
    with open(original_json_file, "w") as f:
        # Write the modified data to the file
        json.dump(data, f, indent=2)
