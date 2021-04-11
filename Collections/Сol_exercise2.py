import collections as c
import json

with open('RomeoAndJuliet.json') as f, open("result.json", 'w') as res:
    data = json.load(f)
    d = c.defaultdict(list)
    for acts in data['acts']:
        for scenes in acts['scenes']:
            for actions in scenes['action']:
                k = actions['character']
                v = actions['says']
                d[k].append(v)
    json.dump(d, res)
