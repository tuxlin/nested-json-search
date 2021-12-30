# nested json search
python script for finding parent path for deeply nested strings in json data

## examples

### looking for nested value 'w' in alphabet.json
```
$ python search.py alphabet.json w
search for: 'w'
path: ['j']['k']['l']['m']['n'][3]['v']
test: eval(data['j']['k']['l']['m']['n'][3]['v'])
results: "w"
```

### looking for root key 'a' in alphabet.json
```
$ python search.py alphabet.json a
search for: 'a'
path: 
test: eval(data)
results: {"a":{"b":["c","d","e",{"f":"g","h":"i"}]},"j":{"k":{"l":{"m":{"n":["o","p","q",{"r":"s","t":"u","v":"w","x":["y","z"]}]}}}}}
```

### looking for unique nested value in random.json
```
$ python search.py random.json '-1802407040'
search for: '-1802407040'
path: ['flag']['missing'][1]['feed']['useful'][0][2]['mad'][1][3]['offer'][2]['widely'][6]['worried'][0]['country'][1]['treated']['ancient']['use'][2][1]['adjective'][1]['cookies'][3]['pine'][3]['cage']['brown']
test: eval(data['flag']['missing'][1]['feed']['useful'][0][2]['mad'][1][3]['offer'][2]['widely'][6]['worried'][0]['country'][1]['treated']['ancient']['use'][2][1]['adjective'][1]['cookies'][3]['pine'][3]['cage']['brown'])
results: -1802407040
```

### looking for unique partial string of nested value
```
$ python search.py random.json '024070'
search for: '024070'
path: ['flag']['missing'][1]['feed']['useful'][0][2]['mad'][1][3]['offer'][2]['widely'][6]['worried'][0]['country'][1]['treated']['ancient']['use'][2][1]['adjective'][1]['cookies'][3]['pine'][3]['cage']['brown']
test: eval(data['flag']['missing'][1]['feed']['useful'][0][2]['mad'][1][3]['offer'][2]['widely'][6]['worried'][0]['country'][1]['treated']['ancient']['use'][2][1]['adjective'][1]['cookies'][3]['pine'][3]['cage']['brown'])
results: -1802407040
```
