from flask import Flask, render_template, request, redirect, url_for
from models import db, Robot
import os

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/robots.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.route('/')
    def index():
        robots = Robot.query.all()
        return render_template('index.html', robots=robots)

    @app.route('/add', methods=['POST'])
    def add_robot():
        name = request.form.get('name')
        model = request.form.get('model')
        if name and model:
            new_robot = Robot(name=name, model=model)
            db.session.add(new_robot)
            db.session.commit()
        return redirect(url_for('index'))

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        os.makedirs('db', exist_ok=True)
    app.run(host='0.0.0.0', port=5000, debug=True)