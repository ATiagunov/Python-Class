import json


with open('wikidata_1000.json') as f:
    wordsList = []
    for i in f:
        wordsDict = json.loads(i)
        wordsList.append(wordsDict)


    for word in wordsList:
        if 'description' in word.keys():
            print(json.dumps({word["label"]['value']: word["description"]['value']}, sort_keys=True,ensure_ascii=False))

        else:
            print(json.dumps({word["label"]['value']: 'None'}, sort_keys=True, ensure_ascii=False))
