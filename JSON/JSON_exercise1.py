import json


with open('wikidata_1000.json') as f, open("dict.json", 'w') as d:
    dict = {}
    for i in f:
        word = json.loads(i)
        if 'description' in word.keys():
            dict.update({word["label"]['value']: word["description"]['value']})

        else:
            dict.update({word["label"]['value']: None})
    json.dump(dict, d)
