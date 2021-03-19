import json
import sys

with open('RomeoAndJuliet.json') as f, open("result.json", 'w') as sys.stdout:
    data = json.load(f)
    for acts in data['acts']:
        for scenes in acts['scenes']:
            characters = []
            for actions in scenes['action']:
                if (actions['character']) not in characters:
                    characters.append(actions['character'])
            print(characters)


