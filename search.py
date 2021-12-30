#!/usr/bin/env python3

import json

def search(data, search_str):
    results = []
    root = False
    if type(data) == list:
        for i,v in enumerate(data):
            json_data = json.dumps(v, separators=(',',':'))
            if search_str in json_data: 
                results.append((i,v))
    elif type(data) == dict:
        for k in data.keys():
            v = data.get(k)
            if search_str == k:
                root = True
                results.append((k,v))
            json_data = json.dumps(v, separators=(',',':'))
            if search_str in json_data:
                results.append((k,v))
    return results, root
                
def path_builder(path):
    path_list_strings = []
    for i in path:
        i = str(i)
        if i.isdigit():
            path_list_strings.append(f'[{i}]')
        else:
            path_list_strings.append(f'''['{i}']''')
    format_path = ''.join(path_list_strings)
    return format_path

def handler(raw_data, search_str):
    path = []
    data = json.loads(raw_data)
    limit = 100
    while search_str in json.dumps(data, separators=(',',':')):
        limit -= 1
        results, root = search(data, search_str)
        #print(f'results: {results}')
        if root:
            break
        if len(results) > 1:
            break
        if not len(results):
            results = data
            break
        path.append(results[0][0])
        data = results[0][1]
        if limit < 0:
            break
    path = path_builder(path)
    return path



if __name__ == "__main__":

    import sys

    input_file = sys.argv[1]
    search_string = sys.argv[2]

    with open(input_file) as f:
        raw_json_data = f.read()

    #print(raw_json_data)
    dict_data = json.loads(raw_json_data)
    #print(data_dict)

    path = handler(raw_json_data, search_string)

    print(f'search for: \'{search_string}\'')
    print(f'path: {path}')
    print(f'test: eval(data{path})')
    val = json.dumps(eval(f'{dict_data}{path}'), separators=(',',':'))
    print(f'results: {val}')
