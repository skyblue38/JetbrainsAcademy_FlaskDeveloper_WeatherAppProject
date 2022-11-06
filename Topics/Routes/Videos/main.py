from flask import Flask

app = Flask('main')
app.app_context()

@app.route('/videos/<animal>')
def render_videos(animal):
    return 'Here will be a video with ' + animal