import os
from mock_pyrobot import MockRoomba
from pyrobot import Roomba
from flask import Flask, jsonify, request


# read ENV and set up globals
mock = os.environ.get('MOCK', default='False')
run_mode = os.environ.get('RUN_MODE', default='prod')
robot = None
app = Flask(__name__)

if mock == 'True':
    print ('you are mocking me')
    robot = MockRoomba()
else:
    print ('its show time')
    robot = Roomba()


################################
# Routes
################################
@app.route('/api/drive', methods=['POST'])
def drive_robot():
    command = request.get_json(force=True)
    required_fields = ['velocity', 'radius']
    # build sanitized dict, then check for missing fields
    data = {k:v for k, v in command.items() if v and k in required_fields}
    dataKeys = data.keys()
    bad_request = False
    for item in required_fields:
        if item not in dataKeys:
            bad_request = True
    if bad_request is True:
        return jsonify('BAD REQUEST')
    robot.Drive(data['velocity'], data['radius'])
    return jsonify(data)

@app.route('/api/sensors', methods=['GET'])
def get_sensors():
    robot.sensors.GetAll()
    return jsonify(robot.sensors.data)

@app.route('/api/dock', methods=['POST'])
def docker_robot():
    robot.Dock();
    return jsonify({})
