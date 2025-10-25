from app.models import db, Robot, Mission

def create_mission(robot_name: str, x: int, y: int, orientation: str, instructions: str) -> Mission:
    """Create a Mars Mission with with initial and random parameters"""
    # Create a Robot
    robot = Robot(
        name=robot_name,
        x_coordinate=x, y_coordinate=y,
        orientation=orientation,
        out_of_bounds=False
    )
    db.session.add(robot)
    db.session.flush()


    # Create Mission for the Robot
    mission = Mission(
        robot=robot.id,
        max_x_axis=x,
        max_y_axis=y,
        instructions=instructions)
    db.session.add(mission)
    db.session.commit()

    return mission, robot

def get_mission_by_id(mission_id: int) -> Mission:
    """Retrieve a Mission by its ID."""
    mission = Mission.query.get(mission_id)
    robot = Robot.query.get(mission.robot)
    return mission, robot

def move_robot(mission_id: int, instruction: str) -> None:
    """Move the robot based on users privided instruction."""
    
    mission = Mission.query.get(mission_id)
    robot = Robot.query.get(mission.robot)

    mission.instructions = instruction

    for instruct in instructions:   
        print(instruct)


    db.session.commit()
    pass