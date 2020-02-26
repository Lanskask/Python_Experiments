import json


def write_data_to_json(data, json_file_name):
    with open(json_file_name, 'w') as outfile:
        json.dump(data, outfile)


def read_from_json_file(json_file_name):
    with open(json_file_name) as json_file:
        return json.load(json_file)


if __name__ == '__main__':
    data = [
        [1, 2,3],
        ['a', 'b', 'c'],
        ['aa', 'ab', 'ac']
    ]

    file_name = "exp_data_1.json"

    write_data_to_json(data, file_name)

    less_i, less_t, less_u = read_from_json_file(file_name)

    print('res', less_i, less_t, less_u)
