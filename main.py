import json


def extract_values_from_json(file_path):
    values = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if "relationships_following" in data:
                data = data["relationships_following"]
            for item in data:
                if 'string_list_data' in item and len(item['string_list_data']) > 0:
                    value = item['string_list_data'][0].get('value')
                    if value:
                        values.append(value)
    except FileNotFoundError:
        print(f"The file {file_path} wasn't found.")
    except json.JSONDecodeError:
        print(f"The file {file_path} wasn't decoded.")
    return values

# Especifica las rutas de los archivos JSON
file_path_1 = './followers_and_following/followers_1.json'
file_path_2 = './followers_and_following/following.json'

# Extrae los valores de cada JSON
values_from_json_1 = extract_values_from_json(file_path_1)
values_from_json_2 = extract_values_from_json(file_path_2)

unique_to_json_2 = set(values_from_json_2) - set(values_from_json_1)

# Imprime los resultados
print(f"People that you are currently following but not follows you instead ({len(unique_to_json_2)}):")
for value in unique_to_json_2:
    print(value)