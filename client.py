import requests
import json
from pprint import pprint

RESCUEGROUPS_KEY = 'y9CJUD8A'

def get_adoptable(location):
    payload = {
        'apikey': RESCUEGROUPS_KEY,
        'objectType': 'animals',
        'objectAction': 'publicSearch',
        'search': {
            'resultStart': 0,
            'resultSort': 'animalID',
            'resultOrder': 'asc',
            'filters': [
                {
                    'fieldName': 'animalStatus',
                    'operation': 'equal',
                    'criteria': 'Available',
                },
                {
                    'fieldName': 'animalSpecies',
                    'operation': 'equal',
                    'criteria': 'Dog',
                },
                {
                    'fieldName': 'animalLocationCitystate',
                    'operation': 'contains',
                    'criteria': location
                }
            ], 
            'fields': [
                'animalID',
                'animalOrgID',
                'animalLocationCitystate',
                'animalName',
                'animalBreed',
                'animalDescriptionPlain',
                'animalPictures'
            ]
        }
    }
    response = requests.post('https://api.rescuegroups.org/http/v2.json', data=json.dumps(payload))
    content = response.text
    
    return json.loads(content)['data']