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

def init_storage(file):
    with open(file, 'a+') as f:
        f.close()

def get_dict_from_storage(file):
    try:
        with open(file, 'r') as f:
            dic = json.load(f)
    except:
        dic = dict()
    return dic

def add_to_storage(key_name, value_name, file):
    dict = get_dict_from_storage(file)
    dict.setdefault(key_name, list()).append(value_name)
    save_to_storage(dict, file)
    return True

def save_to_storage(dict, file):
    with open(file, 'w') as f:
        json.dump(dict, f)
    return True

def load_from_storage(key_name, file):
    dict = get_dict_from_storage(file)
    return dict.get(key_name, list())

arguments = get_arguments()
key_name, value_name = arguments
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
init_storage(storage_path)
if value_name != None:
    add_to_storage(key_name, value_name, storage_path)
elif key_name != None:
    print('Для ключа {} хранятся следующие значения: {}'.format(key_name, load_from_storage(key_name, storage_path)))
else:
    print('Значения для ключа {} не найдены или не задан ключ'.format(key_name))
