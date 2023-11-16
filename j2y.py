import yaml
import json

# Function to take contents of JSON file and dump into YAML file of same name, in YAML format
def convert_file_to_yaml(json_to_convert: str, yaml_file_name: str):

    with open(json_to_convert, 'r') as input_file:
        configuration = json.load(input_file)

    with open(yaml_file_name, 'w') as output_file:
        yaml.dump(configuration, output_file)

    input_file.close()
    output_file.close()


# Function to get the JSON file name for the converted file
def get_yaml_file_name(json_to_convert: str):
    split_files_path = json_to_convert.split('/')
    last_chunk_of_path = split_files_path[-1]
    remove_extension = last_chunk_of_path.split('.')
    yaml_file_temp = remove_extension[0]
    yaml_file_name = f'{yaml_file_temp}.yaml'
    return yaml_file_name


# Control Flow
if __name__ == '__main__':

    # Get the YAML file to convert from the user ( Get it working, worry about error handling later)
    json_to_convert = input('Enter relative path to YAML file in current directory or absolute path to YAML file elsewhere: ')

    # Name the json file after the yaml file
    yaml_file_name = get_yaml_file_name(json_to_convert)

    # Take the contents of the yaml file and dump it into the json file
    convert_file_to_yaml(json_to_convert, yaml_file_name)

    # Tell the user the converted file name
    print(f'Converted to {yaml_file_name}')
