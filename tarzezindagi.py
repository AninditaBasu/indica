from flask import Flask, render_template, request
import json
import requests
import random

app = Flask(__name__)

base_URL_rv = 'https://sheetlabs.com/IND/rv'
base_URL_vs = 'https://sheetlabs.com/IND/vs'
wiki_en_URL = 'https://en.wikisource.org/wiki/The_Rig_Veda/'

@app.route('/')
def first_page():
    return render_template('getName.html')

@app.route('/getname', methods = ['POST'])
def getname():
    nameinput = request.form['nameinput']

    r = requests.get(base_URL_vs)
    json_data_vs = json.loads(json.dumps(r.json()))

    r = requests.get(base_URL_rv)
    json_data_rv = json.loads(json.dumps(r.json()))

    occupation_list = []
    course_list = []
    animal_list = []
    food_list = []
    ornament_list = []
    relative_list = []
    disease_list = []
    for entry in json_data_vs:
        #print(entry)
        if entry['category'] == 'occupation':
            occupation_list.append(entry.get('nagari'))
        if entry['category'] == 'subject':
            course_list.append(entry.get('nagari'))
        if entry['category'] == 'animal':
                animal_list.append(entry.get('nagari'))
        if entry['category'] == 'food':
                food_list.append(entry.get('nagari'))
        if entry['category'] == 'ornament':
                ornament_list.append(entry.get('nagari'))
        if entry['category'] == 'family':
                relative_list.append(entry.get('nagari'))
        if entry['category'] == 'disease':
                disease_list.append(entry.get('nagari'))

    random_year = random.randint(5, 25)

    x = random.randint(0, (len(occupation_list))-1)
    print(x)
    print(occupation_list[x])
    for entry in json_data_vs:
        if entry['nagari'] == occupation_list[x]:
            occupation = occupation_list[x]
            occupation_en = entry.get('word')
            occupation_desc = entry.get('description')
    print(occupation, occupation_en, occupation_desc)

    x = random.randint(0, (len(course_list))-1)
    y = random.randint(0, (len(course_list))-1)
    print(x, y)
    print(course_list[x], course_list[y])
    for entry in json_data_vs:
        if entry['nagari'] == course_list[x]:
            course_1 = course_list[x]
            course_1_en = entry.get('word')
            course_1_desc = entry.get('description')
        if entry['nagari'] == course_list[y]:
            course_2 = course_list[y]
            course_2_en = entry.get('word')
            course_2_desc = entry.get('description')
    print(course_1, course_1_en, course_1_desc)
    print(course_2, course_2_en, course_2_desc)

    x = random.randint(0, (len(animal_list))-1)
    print(x)
    print(animal_list[x])
    for entry in json_data_vs:
        if entry['nagari'] == animal_list[x]:
            animal = animal_list[x]
            animal_en = entry.get('word')
            animal_desc = entry.get('description')
    print(animal, animal_en, animal_desc)

    x = random.randint(0, (len(food_list))-1)
    print(x)
    print(food_list[x])
    for entry in json_data_vs:
        if entry['nagari'] == food_list[x]:
            food = food_list[x]
            food_en = entry.get('word')
            food_desc = entry.get('description')
    print(food, food_en, food_desc)

    x = random.randint(0, (len(ornament_list))-1)
    print(x)
    print(ornament_list[x])
    for entry in json_data_vs:
        if entry['nagari'] == ornament_list[x]:
            ornament = ornament_list[x]
            ornament_en = entry.get('word')
            ornament_desc = entry.get('description')
    print(ornament, ornament_en, ornament_desc)

    x = random.randint(0, (len(relative_list))-1)
    print(x)
    print(relative_list[x])
    for entry in json_data_vs:
        if entry['nagari'] == relative_list[x]:
            relative = relative_list[x]
            relative_en = entry.get('word')
            relative_desc = entry.get('description')
    print(relative, relative_en, relative_desc)

    x = random.randint(0, (len(disease_list))-1)
    y = random.randint(0, (len(disease_list))-1)
    print(x)
    print(disease_list[x], disease_list[y])
    for entry in json_data_vs:
        if entry['nagari'] == disease_list[x]:
            disease_1 = disease_list[x]
            disease_1_en = entry.get('word')
            disease_1_desc = entry.get('description')
        if entry['nagari'] == disease_list[y]:
            disease_2 = disease_list[y]
            disease_2_en = entry.get('word')
            disease_2_desc = entry.get('description')
    print(disease_1, disease_1_en, disease_1_desc)
    print(disease_2, disease_2_en, disease_2_desc)

    x = random.randint(0, (len(json_data_rv))-1)
    y = random.randint(0, (len(json_data_rv))-1)
    rishi_1 = json_data_rv[x].get('sungby')
    rishi_2 = json_data_rv[y].get('sungby')
    print(rishi_1, rishi_2)

    x = random.randint(0, (len(json_data_rv))-1)
    god = json_data_rv[x].get('sungfor')
    god_verse_mandal = json_data_rv[x].get('mandal')
    god_verse_sukta = json_data_rv[x].get('sukta')
    god_verse = wiki_en_URL + 'Mandala_' + str(god_verse_mandal) + '/Hymn_' + str(god_verse_sukta)

    return render_template('postAdvice.html', nameinput=nameinput, random_year=random_year, occupation=occupation, occupation_en=occupation_en, occupation_desc=occupation_desc, course_1=course_1, course_1_en=course_1_en, course_1_desc=course_1_desc, course_2=course_2, course_2_en=course_2_en, course_2_desc=course_2_desc, animal=animal, animal_en=animal_en, animal_desc=animal_desc, food=food, food_en=food_en, food_desc=food_desc, ornament=ornament, ornament_en=ornament_en, ornament_desc=ornament_desc, relative=relative, relative_en=relative_en, relative_desc=relative_desc, disease_1=disease_1, disease_1_en=disease_1_en, disease_1_desc=disease_1_desc, disease_2=disease_2, disease_2_en=disease_2_en, disease_2_desc=disease_2_desc, rishi_1=rishi_1, rishi_2=rishi_2, god_verse=god_verse, god=god)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
	#app.run()