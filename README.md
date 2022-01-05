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
$ python search.py random_with_arrays.json '-1802407040'
search for: '-1802407040'
path: ['flag']['missing'][1]['feed']['useful'][0][2]['mad'][1][3]['offer'][2]['widely'][6]['worried'][0]['country'][1]['treated']['ancient']['use'][2][1]['adjective'][1]['cookies'][3]['pine'][3]['cage']['brown']
test: eval(data['flag']['missing'][1]['feed']['useful'][0][2]['mad'][1][3]['offer'][2]['widely'][6]['worried'][0]['country'][1]['treated']['ancient']['use'][2][1]['adjective'][1]['cookies'][3]['pine'][3]['cage']['brown'])
results: -1802407040

python search.py random.json milk
search for: 'milk'
path: ['tonight']['southern']['size']['shut']['nature']['alone']['language']['share']['molecular']['like']['western']['command']['eventually']['tank']['kill']['himself']['danger']['border']['hand']['easier']['food']['door']['attached']['thee']['surface']['unit']['large']['produce']['loose']['mine']['trade']['question']['me']['two']['week']['nobody']['wood']['dried']['local']['view']['reader']['fox']['carbon']
test: eval(data['tonight']['southern']['size']['shut']['nature']['alone']['language']['share']['molecular']['like']['western']['command']['eventually']['tank']['kill']['himself']['danger']['border']['hand']['easier']['food']['door']['attached']['thee']['surface']['unit']['large']['produce']['loose']['mine']['trade']['question']['me']['two']['week']['nobody']['wood']['dried']['local']['view']['reader']['fox']['carbon'])
results: "milk"
```

### looking for unique partial string of nested value
```
$ python search.py random_with_arrays.json '024070'
search for: '024070'
path: ['flag']['missing'][1]['feed']['useful'][0][2]['mad'][1][3]['offer'][2]['widely'][6]['worried'][0]['country'][1]['treated']['ancient']['use'][2][1]['adjective'][1]['cookies'][3]['pine'][3]['cage']['brown']
test: eval(data['flag']['missing'][1]['feed']['useful'][0][2]['mad'][1][3]['offer'][2]['widely'][6]['worried'][0]['country'][1]['treated']['ancient']['use'][2][1]['adjective'][1]['cookies'][3]['pine'][3]['cage']['brown'])
results: -1802407040
```
### looking for unique json snippet of nested key value pair
```
$ python search.py random_with_arrays.json 'describe":false'
search for: 'describe":false'
path: ['flag']['missing'][1]['feed']['useful'][0][2]['mad'][1][3]['offer'][2]['widely'][6]['worried'][0]['country'][1]['treated']['ancient']['use'][2][1]['adjective'][1]['cookies'][3]['pine'][3]['cage']['electric'][1][3]['sleep'][0][6]['speak'][1]['unusual'][1][2][0]['call'][2]['standard'][3]['character'][0][1][0][0][2][0][0]['leaving']
test: eval(data['flag']['missing'][1]['feed']['useful'][0][2]['mad'][1][3]['offer'][2]['widely'][6]['worried'][0]['country'][1]['treated']['ancient']['use'][2][1]['adjective'][1]['cookies'][3]['pine'][3]['cage']['electric'][1][3]['sleep'][0][6]['speak'][1]['unusual'][1][2][0]['call'][2]['standard'][3]['character'][0][1][0][0][2][0][0]['leaving'])
results: {"describe":false,"slipped":"building","youth":{"anywhere":"job","horn":"football","straw":{"contain":{"may":-1533795553,"doing":{"every":-1848240256,"village":"football","wall":"safe","wrapped":true,"twenty":true,"adventure":true,"lamp":true,"upward":true,"summer":"carried","pilot":612043998.6392999},"wear":true,"mad":-779925876.646755,"donkey":"excited","growth":"flat","explore":"cream","throughout":false,"flame":"material","position":"leaf"},"function":-1185763982,"silver":"made","independent":-2144472501.2513127,"nor":false,"settlers":"wooden","signal":600681625,"garden":2104249424,"stronger":-1605066211,"line":false},"satisfied":"history","both":-34816053,"leg":"labor","act":"nodded","dangerous":"tonight","matter":"therefore","yet":648005295.1524227},"crop":2113432219.7696257,"smaller":true,"union":"explain","tonight":-1667947886,"stepped":61332406.91567421,"blanket":-712194171,"program":true}
```
