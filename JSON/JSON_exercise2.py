import json

with open('RomeoAndJuliet.json') as f, open("result.json", 'w') as res:
    data = json.load(f)
    for acts in data['acts']:
        for scenes in acts['scenes']:
            characters = []
            for actions in scenes['action']:
                if (actions['character']) not in characters:
                    characters.append(actions['character'])
            json.dump(characters, res)
            res.write('\n')
#Я не понимаю, как записать файл методом json.dumps...

