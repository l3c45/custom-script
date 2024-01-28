import json

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

# Path to the original JSON file and the updated file
original_json_file = "app.json"
updated_json_file = "updated.json"

# Value to replace and new value
value_to_replace = "909090"
new_value = "2222222"

# Open the original JSON file in read mode
with open(original_json_file, "r") as f:
    # Load the JSON content
    data = json.load(f)

    # Perform recursive replacement
    replace_value(data, value_to_replace, new_value)

# Write the modified data to a new JSON file
with open(original_json_file, "w") as f:
    # Write the modified data to the new file
    json.dump(data, f, indent=2)
