from flask import Flask

app = Flask('main')
app.app_context()

city_dict = {10001: "New York",
             20001: "Washington",
             101000: "Moscow"}

@app.route('/index/<int:city_code>')
def render_city(city_code):
    if city_code in city_dict.keys():
        return city_dict[city_code]
    return 'There is no city with this index'