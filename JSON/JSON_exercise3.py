import json


counts = {}

with open('../Collections/RomeoAndJuliet.json') as f:
    data = json.load(f)
for acts in data['acts']:
    for scenes in acts['scenes']:
        for actions in scenes['action']:
            if actions['character'] not in counts:
                counts[actions['character']] = 1
            counts[actions['character']] += 1

print(max(counts, key=counts.get))
