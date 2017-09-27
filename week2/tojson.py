def to_json(func):

    import json

    def wrapper(*args, **kwargs):
        with open("decorator.values",'w') as f:
            return json.dump(func(*args, **kwargs), f)
    return wrapper

@to_json
# Вставь сюда свою функцию
def get_arguments():

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--key')
    parser.add_argument('--value')
    arguments = parser.parse_args()
#    return None
#    return True
    return arguments.key, arguments.value
#-----------------------------------------
# Вызови здесь свою функцию в качестве параметра
func_json = to_json(get_arguments())