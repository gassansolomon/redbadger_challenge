from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Robot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    out_of_bounds = db.Column(db.Boolean, default=False)
    x_coordinate = db.Column(db.Integer, nullable=True)
    y_coordinate = db.Column(db.Integer, nullable=True)
    orientation = db.Column(db.String(1), nullable=True)

    def __repr__(self):
        return "<Robot {self.id}>"
    
class Mission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    robot = db.Column(db.Integer, db.ForeignKey("robot.id"))
    instructions = db.Column(db.String(255), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    successful = db.Column(db.Boolean, default=False)
    max_x_axis = db.Column(db.Integer, nullable=True)
    max_y_axis = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return "<Mission {self.id}>"
    