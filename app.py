from sys import argv
from flask import Flask
from flask import render_template
import client

application = Flask(__name__)

def parse_description(description):
    # I know this is messy but I couldn't think of another way to get rid of the annoying HTML symbols :(
    description = description.replace('&nbsp;', ' ')
    description = description.replace('&amp;', '&')
    description = description.replace('&rsquo;', '\'')
    description = description.replace('&#39;', '\'')
    return description

def parse_search(search_results):
    adoptable_dogs = []
    for _, result in search_results.items():
        breed = result['animalBreed'].lower()
        id = result['animalID']
        org_id = result['animalOrgID']
        location = result['animalLocationCitystate']
        name = result['animalName']
        pic = result['animalPictures'][0]['large']['url']
        description = result['animalDescriptionPlain']

        description = parse_description(description)
        breed = breed.replace('/', 'and')
        adoptable_dogs.append({
            'id': id, 
            'org_id': org_id,
            'breed': breed, 
            'name': name, 
            'location': location, 
            'pic': pic, 
            'description': description
        })

    return adoptable_dogs

def get_adoptable_dogs(location):
    search_results = client.get_adoptable(location)
    p_search_results = parse_search(search_results)
    return p_search_results

@application.route('/')
def homepage():
    page = 'page.html'
    object_list = get_adoptable_dogs(location)
    return render_template(page, object_list=object_list)

if __name__ == '__main__':
    
    if len(argv) < 2:
        print("Need to pass in a name of a location as an argument")
    else:
        location = argv[1]
        application.run(debug=True, use_reloader=True)
