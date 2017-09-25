import argparse
import json
import os
import tempfile

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--key')
    parser.add_argument('--value')
    arguments = parser.parse_args()
    return arguments.key, arguments.value

def create_storage(file):
    try:
        with open(file, 'r') as f:
            f.close()
    except:
        with open(file, 'w') as f:
            print('Создан файл-хранилище')

def write_arguments(arguments, file):
    key_name, value_name = arguments
    if key_name != None and value_name != None:
        with open(file, 'a') as f:
            json.dump(arguments,f)
        return print('В файл добавлены значения key: {} и value: {}'.format(key_name, value_name))
    else:
        return print('Считываем значения...')

def read_values(arguments, file):
    key_name, value_name = arguments
    print(key_name, value_name)
    if key_name != None and value_name == None:
        with open(file, 'r') as f:
            values = json.load(f)
            values.get(key_name, list())
        return print('В файл добавлены значения key: {} и value: {}'.format(key_name, value_name))
    else:
        return print('Значения с ')

arguments = get_arguments()
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
create_storage(storage_path)
write_arguments(arguments, storage_path)
read_values(arguments, storage_path)