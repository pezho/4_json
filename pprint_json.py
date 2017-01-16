import json
import os.path


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, encoding='utf-8') as f:
        return json.load(f)


def pretty_print_json(data):
    print(json.dumps(data, indent=4, sort_keys=True))


if __name__ == '__main__':
    filepath = input('Enter path to your json file: ')
    if not filepath.endswith('.json'):
        print('Type of file most be json.')
    else:
        json_data = load_data(filepath)
        pretty_print_json(json_data) if json_data else print('File empty')
        
