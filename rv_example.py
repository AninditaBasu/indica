from flask import Flask, render_template, request
import json
import requests

app = Flask(__name__)

base_URL = 'https://sheetlabs.com/IND/rv'
wiki_en_URL = 'https://en.wikisource.org/wiki/The_Rig_Veda/'
#format: https://en.wikisource.org/wiki/The_Rig_Veda/Mandala_1/Hymn_2

@app.route('/')
def first_page():
    return render_template('index.html')

@app.route('/rvget', methods = ['POST'])
def rvget():
    meter = request.form['meter']
    url_string = base_URL + '?meter=' + meter
    print(url_string)

    r = requests.get(url_string)
    json_data = json.loads(json.dumps(r.json()))

    url_list = []

    for line in json_data:
        for k, v in line.items():
            book = line['mandal']
            verse = line['sukta']
            en_URL = wiki_en_URL + 'Mandala_' + str(book) + '/Hymn_' + str(verse)
            url_list.append(en_URL)
    print(url_list)
    unique_urls = []
    for item in url_list:
        if item not in unique_urls:
            unique_urls.append(item)

    print(unique_urls)
    return render_template('rvresponse.html', unique_urls=unique_urls, meter=meter)

if __name__ == "__main__":
        port = int(os.environ.get("PORT", 5000))
        app.run(host='0.0.0.0', port=port)