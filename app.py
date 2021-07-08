
from stories import *
from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)

@app.route('/stories')
def choose_story():
    return render_template('stories.html', stories=stories.values())

@app.route('/input')
def get_input():
    story_id = request.args['story_id']
    story = stories[story_id]
    inputs = story.prompts
    return render_template('input.html',inputs=inputs,
                                        story_id=story_id,
                                        title = story.title
                                                )

@app.route('/story')
def get_story():
    story_id = request.args['story_id']
    story = stories[story_id]
    result = story.generate(request.args)
    return render_template('result.html', result=result, title = story.title)
