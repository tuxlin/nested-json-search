#!/usr/bin/env python3

import json

def search(data, search_str):
    results = []
    root = False
    if type(data) == list:
        for i,v in enumerate(data):
            json_data = json.dumps(v)
            if search_str in json_data: 
                results.append((i,v))
    elif type(data) == dict:
        for k in data.keys():
            v = data.get(k)
            if search_str in k:
                root = True
                results.append((k,v))
            json_data = json.dumps(v)
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
    while search_str in json.dumps(data):
        limit -= 1
        results, root = search(data, search_str)
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

    dict_data = {
      "a": {
        "b": [
          "c",
          "d",
          "e",
          {
            "f": "g",
            "h": "i"
          }
        ]
      },
      "j": {
        "k": {
          "l": {
            "m": {
              "n": [
                "o",
                "p",
                "q",
                {
                  "r": "s",
                  "t": "u",
                  "v": "w",
                  "x": [
                    "y",
                    "z"
                  ]
                }
              ]
            }
          }
        }
      }
    }

    raw_json_data = json.dumps(dict_data)
    
    search_string = 'w'

    path = handler(raw_json_data, search_string)

    print(f'search for: {search_string}')
    print(f'path: {path}')
    print(f'test: eval(data{path})')
    val = eval(f'{dict_data}{path}')
    print(f'results: {val}')
