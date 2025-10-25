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

def reset_robot(mission_id: int) -> None:
    """Reset the robot to original mission corrds."""
    mission = Mission.query.get(mission_id)
    robot = Robot.query.get(mission.robot)
    robot.x_coordinate = mission.max_x_axis
    robot.y_coordinate = mission.max_y_axis
    robot.orientation = 'N'
    robot.out_of_bounds = False
    mission.completed = False
    mission.successful = False

    db.session.add(robot)
    db.session.add(mission)
    db.session.commit()

def move_robot(mission_id: int, instructions: str) -> None:
    """Move the robot based on users privided instruction."""
    
    mission = Mission.query.get(mission_id)
    robot = Robot.query.get(mission.robot)

    mission.instructions = instructions

    # Needed to determine the last position of the robot before going out of bounds
    prev_x = robot.x_coordinate
    prev_y = robot.y_coordinate
    try:
        for instruct in instructions.split(','):

            # setting based on the last instruction[]
            prev_x = robot.x_coordinate
            prev_y = robot.y_coordinate
            
            instruct = instruct.strip().upper()
            print(instruct)

            # there's probably a neater way to do this but didn't want to spend too much time on it.
            if instruct == 'F':
                if robot.orientation == 'N':
                    robot.y_coordinate += 1
                elif robot.orientation == 'E':
                    robot.x_coordinate += 1
                elif robot.orientation == 'S':
                    robot.y_coordinate -= 1
                elif robot.orientation == 'W':
                    robot.x_coordinate -= 1
            elif instruct == 'L':
                if robot.orientation == 'N':
                    robot.orientation = 'W'
                elif robot.orientation == 'E':
                    robot.orientation = 'N'
                elif robot.orientation == 'S':
                    robot.orientation = 'E'
                elif robot.orientation == 'W':
                    robot.orientation = 'S'
            elif instruct == 'R':
                if robot.orientation == 'N':
                    robot.orientation = 'E'
                elif robot.orientation == 'E':
                    robot.orientation = 'S'
                elif robot.orientation == 'S':
                    robot.orientation = 'W'
                elif robot.orientation == 'W':
                    robot.orientation = 'N'

            # Check for out of bounds
            print(f"Robot position: ({robot.x_coordinate}, {robot.y_coordinate})")
            if (robot.x_coordinate < 0 or robot.x_coordinate > mission.max_x_axis or
                robot.y_coordinate < 0 or robot.y_coordinate > mission.max_y_axis):
                robot.out_of_bounds = True
                mission.scent_x = prev_x
                mission.scent_y = prev_y
                mission.completed = True
                mission.successful = False
                print(f"Robot {robot.name} is out of bounds at ({robot.x_coordinate}, {robot.y_coordinate})")
                break
    except Exception as e:
        print(f"Error moving robot: {str(e)}")
        raise e

    db.session.add(robot)
    db.session.add(mission)
    db.session.commit()
    pass