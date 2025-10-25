from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from app.models import db, Robot, Mission
from app import missioncontrol
import os, random


app = Flask(__name__)
os.makedirs("instance", exist_ok=True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///robots.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    """Home page route."""
    missions = Mission.query.all()
    return render_template('index.html', missions=missions)

@app.route('/mission')
def start_mission():
    """Start a mission for a robot with random parameters."""
    x_coord = random.randint(10, 20)
    y_coord = random.randint(10, 20)
    
    missions_count = db.session.query(Mission).count()
    robot_name=f"ExplorerBot-{missions_count+1}"

    print(f"Previous missions: {missions_count}")
    print(f"Mission coordinates: X={x_coord}, Y={y_coord}")

    mission, robot = missioncontrol.create_mission(
        robot_name=robot_name,
        x=x_coord,
        y=y_coord,
        orientation=random.choice(['N', 'E', 'S', 'W']),
        instructions="FFRFLF"
    )

    
    return render_template('mission.html', mission=mission, robot=robot)

@app.route('/mission/<int:mission_id>' )
def view_mission(mission_id):
    """View details of a specific mission."""
    mission, robot = missioncontrol.get_mission_by_id(mission_id)
    if not mission:
        return "Mission not found", 404
    return render_template('mission.html', mission=mission, robot=robot)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)