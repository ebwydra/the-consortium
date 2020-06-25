from flask import Flask, render_template
import academia
from academia import generate_mission

app = Flask(__name__)

@app.route("/")
def index():
    mission = generate_mission()
    return render_template('index.html', mission=mission)

if __name__ == '__main__':
    print('starting Flask app', app.name)
    app.run(debug=True)
