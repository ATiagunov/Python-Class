import collections as c
import json

with open('/home/alexander/PycharmProjects/python_practice/JSON/RomeoAndJuliet.json') as f:
    data = json.load(f)
    d = c.defaultdict(list)
    speech_cnt = c.Counter()
    for acts in data['acts']:
        for scenes in acts['scenes']:
            for actions in scenes['action']:
                k = actions['character']
                v = actions['says']
                d[k].append(v)
                speech_cnt[k] += 1

    print(speech_cnt)
