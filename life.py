from flask import Flask, render_template
import json
import requests
import random

app = Flask(__name__)

r = requests.get('https://api-vs.herokuapp.com/vs/v1/resources/all')
json_data_vs = json.loads(json.dumps(r.json()))

r = requests.get('https://api-rv.herokuapp.com/rv/v1/resources/all')
json_data_rv = json.loads(json.dumps(r.json()))

animal_list = []
building_list = []
clothing_list = []
distance_list = []
games_list = []
grain_list = []
grass_list = []
literature_list = []
metal_list = []
object_list = []
ornament_list = []
occupation_list = []
place_list = []
plant_list = []
river_list = []
subject_list = []
sungby_list = []
time_list = []
tree_list = []
weight_list = []

x = random.randint(0, (len(json_data_rv))-1)
y = random.randint(0, (len(json_data_rv))-1)
z = random.randint(0, (len(json_data_rv))-1)
sungby1 = json_data_rv[x].get('sungby')
sungby2 = json_data_rv[y].get('sungby')
sungby3 = json_data_rv[z].get('sungby')
print(sungby1, sungby2, sungby3)

for entry in json_data_vs:
    print(entry)
    if entry['category'] == 'animal':
        animal_list.append(entry.get('nagari'))
    if entry['category'] == 'building':
        building_list.append(entry.get('nagari'))
    if entry['category'] == 'clothing':
        clothing_list.append(entry.get('nagari'))
    if entry['category'] == 'distance':
        distance_list.append(entry.get('nagari'))
    if entry['category'] == 'games':
        games_list.append(entry.get('nagari'))
    if entry['category'] == 'grain':
        grain_list.append(entry.get('nagari'))
    if entry['category'] == 'grass':
        grass_list.append(entry.get('nagari'))
    if entry['category'] == 'literature':
        literature_list.append(entry.get('nagari'))
    if entry['category'] == 'metal':
        metal_list.append(entry.get('nagari'))
    if entry['category'] == 'occupation':
        occupation_list.append(entry.get('nagari'))
    if entry['category'] == 'object':
        object_list.append(entry.get('nagari'))
    if entry['category'] == 'animal':
        animal_list.append(entry.get('nagari'))
    if entry['category'] == 'ornament':
        ornament_list.append(entry.get('nagari'))
    if entry['category'] == 'place':
        place_list.append(entry.get('nagari'))
    if entry['category'] == 'plant':
        plant_list.append(entry.get('nagari'))
    if entry['category'] == 'river':
        river_list.append(entry.get('nagari'))
    if entry['category'] == 'subject':
        subject_list.append(entry.get('nagari'))
    if entry['category'] == 'time':
        time_list.append(entry.get('nagari'))
    if entry['category'] == 'tree':
        tree_list.append(entry.get('nagari'))
    if entry['category'] == 'weight':
        weight_list.append(entry.get('nagari'))

x = random.randint(0, (len(animal_list))-1)
print(x)
print(animal_list[x])
for entry in json_data_vs:
    if entry['nagari'] == animal_list[x]:
        animal = animal_list[x]
        animal_en = entry.get('word')
        animal_desc = entry.get('description')
print(animal, animal_en, animal_desc)

x = random.randint(0, (len(building_list))-1)
print(x)
print(building_list[x])
for entry in json_data_vs:
    if entry['nagari'] == building_list[x]:
        building = building_list[x]
        building_en = entry.get('word')
        building_desc = entry.get('description')
print(building, building_en, building_desc)

x = random.randint(0, (len(clothing_list))-1)
print(x)
print(clothing_list[x])
for entry in json_data_vs:
    if entry['nagari'] == clothing_list[x]:
        clothing = clothing_list[x]
        clothing_en = entry.get('word')
        clothing_desc = entry.get('description')
print(clothing, clothing_en, clothing_desc)

x = random.randint(0, (len(distance_list))-1)
print(x)
print(distance_list[x])
for entry in json_data_vs:
    if entry['nagari'] == distance_list[x]:
        distance = distance_list[x]
        distance_en = entry.get('word')
        distance_desc = entry.get('description')
print(distance, distance_en, distance_desc)

x = random.randint(0, (len(ornament_list))-1)
print(x)
print(ornament_list[x])
for entry in json_data_vs:
    if entry['nagari'] == ornament_list[x]:
        ornament = ornament_list[x]
        ornament_en = entry.get('word')
        ornament_desc = entry.get('description')
print(ornament, ornament_en, ornament_desc)

x = random.randint(0, (len(games_list))-1)
print(x)
print(games_list[x])
for entry in json_data_vs:
    if entry['nagari'] == games_list[x]:
        games = games_list[x]
        games_en = entry.get('word')
        games_desc = entry.get('description')
print(games, games_en, games_desc)

x = random.randint(0, (len(subject_list))-1)
print(x)
for entry in json_data_vs:
    if entry['nagari'] == subject_list[x]:
        subject = subject_list[x]
        subject_en = entry.get('word')
        subject_desc = entry.get('description')
print(subject, subject_en, subject_desc)

x = random.randint(0, (len(grain_list))-1)
print(x)
print(grain_list[x])
for entry in json_data_vs:
    if entry['nagari'] == grain_list[x]:
        grain = grain_list[x]
        grain_en = entry.get('word')
        grain_desc = entry.get('description')
print(grain, grain_en, grain_desc)

x = random.randint(0, (len(grass_list))-1)
print(x)
print(grass_list[x])
for entry in json_data_vs:
    if entry['nagari'] == grass_list[x]:
        grass = grass_list[x]
        grass_en = entry.get('word')
        grass_desc = entry.get('description')
print(grass, grass_en, grass_desc)

x = random.randint(0, (len(literature_list))-1)
print(x)
print(literature_list[x])
for entry in json_data_vs:
    if entry['nagari'] == literature_list[x]:
        literature = literature_list[x]
        literature_en = entry.get('word')
        literature_desc = entry.get('description')
print(literature, literature_en, literature_desc)

x = random.randint(0, (len(metal_list))-1)
print(x)
print(metal_list[x])
for entry in json_data_vs:
    if entry['nagari'] == metal_list[x]:
        metal = metal_list[x]
        metal_en = entry.get('word')
        metal_desc = entry.get('description')
print(metal, metal_en, metal_desc)

x = random.randint(0, (len(object_list))-1)
print(x)
print(object_list[x])
for entry in json_data_vs:
    if entry['nagari'] == object_list[x]:
        object = object_list[x]
        object_en = entry.get('word')
        object_desc = entry.get('description')
print(object, object_en, object_desc)

x = random.randint(0, (len(occupation_list))-1)
print(x)
print(occupation_list[x])
for entry in json_data_vs:
    if entry['nagari'] == occupation_list[x]:
        occupation = occupation_list[x]
        occupation_en = entry.get('word')
        occupation_desc = entry.get('description')
print(occupation, occupation_en, occupation_desc)

x = random.randint(0, (len(place_list))-1)
print(x)
print(place_list[x])
for entry in json_data_vs:
    if entry['nagari'] == place_list[x]:
        place = place_list[x]
        place_en = entry.get('word')
        place_desc = entry.get('description')
print(place, place_en, place_desc)

x = random.randint(0, (len(plant_list))-1)
print(x)
print(plant_list[x])
for entry in json_data_vs:
    if entry['nagari'] == plant_list[x]:
        plant = plant_list[x]
        plant_en = entry.get('word')
        plant_desc = entry.get('description')
print(plant, plant_en, plant_desc)

x = random.randint(0, (len(river_list))-1)
print(x)
print(river_list[x])
for entry in json_data_vs:
    if entry['nagari'] == river_list[x]:
        river = river_list[x]
        river_en = entry.get('word')
        river_desc = entry.get('description')
print(river, river_en, river_desc)

x = random.randint(0, (len(time_list))-1)
print(x)
print(time_list[x])
for entry in json_data_vs:
    if entry['nagari'] == time_list[x]:
        time = time_list[x]
        time_en = entry.get('word')
        time_desc = entry.get('description')
print(time, time_en, time_desc)

x = random.randint(0, (len(tree_list))-1)
print(x)
print(tree_list[x])
for entry in json_data_vs:
    if entry['nagari'] == tree_list[x]:
        tree = tree_list[x]
        tree_en = entry.get('word')
        tree_desc = entry.get('description')
print(tree, tree_en, tree_desc)

x = random.randint(0, (len(weight_list))-1)
print(x)
print(weight_list[x])
for entry in json_data_vs:
    if entry['nagari'] == weight_list[x]:
        weight = weight_list[x]
        weight_en = entry.get('word')
        weight_desc = entry.get('description')
print(weight, weight_en, weight_desc)

number1 = random.randint(12, 423)
number2 = random.randint(27, 56)
number3 = random.randint(89, 596)
number4 = random.randint(2, 11)
number5 = random.randint(6298, 93406)
print(number1, number2, number3, number4, number5)


@app.route('/')
def first_page():
    return render_template('life.html', sungby1=sungby1, sungby2=sungby2, sungby3=sungby3, animal=animal, animal_en=animal_en, animal_desc=animal_desc, building=building, building_en=building_en, building_desc=building_desc, clothing=clothing, clothing_en=clothing_en, clothing_desc=clothing_desc, distance=distance, distance_en=distance_en, distance_desc=distance_desc, ornament=ornament, ornament_en=ornament_en, ornament_desc=ornament_desc, games=games, games_en=games_en, games_desc=games_desc, subject=subject, subject_en=subject_en, subject_desc=subject_desc, grass=grass, grass_en=grass_en, grass_desc=grass_desc, grain=grain, grain_en=grain_en, grain_desc=grain_desc, literature=literature, literature_en=literature_en, literature_desc=literature_desc, metal=metal, metal_en=metal_en, metal_desc=metal_desc, object=object, object_en=object_en, object_desc=object_desc, occupation=occupation, occupation_en=occupation_en, occupation_desc=occupation_desc, place=place, place_en=place_en, place_desc=place_desc, plant=plant, plant_en=plant_en, plant_desc=plant_desc, river=river, river_en=river_en, river_desc=river_desc, time=time, time_en=time_en, time_desc=time_desc, tree=tree, tree_en=tree_en, tree_desc=tree_desc, weight=weight, weight_en=weight_en, weight_desc=weight_desc, number1=number1, number2=number2, number3=number3, number4=number4, number5=number5)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
	#app.run()
