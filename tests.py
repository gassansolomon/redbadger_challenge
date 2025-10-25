import pytest
from app.models import db, Robot, Mission
from app.missioncontrol import create_mission
from main import app

@pytest.fixture
def test_client():
    """Flask test client memory database to setup testing environment for each time we run tests"""
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['TESTING'] = True

    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.drop_all()

def test_create_mission(test_client):
    with app.app_context():
        mission, robot = create_mission(
            robot_name="TestBot",
            x=30,
            y=30,
            orientation="N",
            instructions="FFRFLF"
        )

        assert robot.id is not None
        assert robot.name == "TestBot"
        assert robot.x_coordinate == 0
        assert robot.y_coordinate == 0
        assert robot.orientation == "N"
        assert robot.out_of_bounds == False

        assert mission.id is not None
        assert mission.completed == False
        assert mission.robot == robot.id
        assert mission.successful == False
        assert mission.max_x_axis == 30
        assert mission.max_y_axis == 30
        assert mission.instructions == "FFRFLF"

def test_get_mission_by_id(test_client):
    """Test retrieving a mission by its ID."""
    with app.app_context():
        mission, robot = create_mission(
            robot_name="TestBot2",
            x=25,
            y=25,
            orientation="E",
            instructions="LFRFF"
        )

        from app.missioncontrol import get_mission_by_id
        fetched_mission, fetched_robot = get_mission_by_id(mission.id)

        assert fetched_mission.id == mission.id
        assert fetched_robot.id == robot.id
        assert fetched_robot.name == "TestBot2"