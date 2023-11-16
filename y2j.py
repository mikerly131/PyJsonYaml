import yaml
import json

# Function to take contents of YAML file and dump into JSON file of same name, in JSON format
def convert_file_to_json(yaml_to_convert: str, json_file_name: str):

    with open(yaml_to_convert, 'r') as input_file:
        configuration = yaml.safe_load(input_file)

    with open(json_file_name, 'w') as output_file:
        json.dump(configuration, output_file)

    input_file.close()
    output_file.close()


# Function to get the YAML file name to name the JSON the same thing
def get_json_file_name(yaml_to_convert: str):
    split_files_path = yaml_to_convert.split('/')
    last_chunk_of_path = split_files_path[-1]
    remove_extension = last_chunk_of_path.split('.')
    json_file_temp = remove_extension[0]
    json_file_name = f'{json_file_temp}.json'
    return json_file_name


# Control Flow
if __name__ == '__main__':

    # Get the YAML file to convert from the user ( Get it working, worry about error handling later)
    yaml_to_convert = input('Enter relative path to YAML file in current directory or absolute path to YAML file elsewhere: ')

    # Name the json file after the yaml file
    json_file_name = get_json_file_name(yaml_to_convert)

    # Take the contents of the yaml file and dump it into the json file
    convert_file_to_json(yaml_to_convert, json_file_name)

    # Tell the user the converted file name
    print(f'Converted to {json_file_name}')



