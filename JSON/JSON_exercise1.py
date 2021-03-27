import json


with open('wikidata_1000.json') as f, open("dict.json", 'w') as d:
    for i in f:
        word = (json.loads(i))
        if 'description' in word.keys():
            json.dump({word["label"]['value']: word["description"]['value']}, d, indent=2, sort_keys=True,ensure_ascii=False)

        else:
            json.dump({word["label"]['value']: None}, d, indent=2, sort_keys=True, ensure_ascii=False)
