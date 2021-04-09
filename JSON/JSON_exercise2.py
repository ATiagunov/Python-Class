import json

with open('../Collections/RomeoAndJuliet.json') as f, open("result.json", 'w') as res:
    data = json.load(f)
    for acts in data['acts']:
        for scenes in acts['scenes']:
            characters = []
            for actions in scenes['action']:
                if (actions['character']) not in characters:
                    characters.append(actions['character'])
            res.write(json.dumps(characters) + '\n')


