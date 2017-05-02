import logging
import math
import serial
import struct
import time
import threading
import traceback

ROOMBA_OPCODES = dict(
    start = 128,
    baud = 129,
    control = 130,
    safe = 131,
    full = 132,
    power = 133,
    spot = 134,
    clean = 135,
    max = 136,
    drive = 137,
    motors = 138,
    leds = 139,
    song = 140,
    play = 141,
    sensors = 142,
    force_seeking_dock = 143,
    )

class MockRoombaSensors(object):
    def __init__(self, robot):
        self.robot = robot
        self.data = {}
    def GetAll(self):
        self.data = {
          'foo': 'bar',
          'sample': 'data',
          'test': 123
        }

class MockSerialCommandInterface(object):
    def __init__(self, tty, baudrate):
        self.ser = 'mock ser'
        self.opcodes = {}

    def Wake(self):
        pass
    def AddOpCodes(self, opcodes):
        self.opcodes.update(opcodes)

class MockRoomba(object):
    def __init__(self, tty=''):
        self.tty = tty
        self.sci = MockSerialCommandInterface(tty, 57600)
        self.sci.AddOpCodes(ROOMBA_OPCODES)
        self.sensors = MockRoombaSensors(self)
        self.safe = True

    def Passive(self):
        print ('entering passive mode')
    def Control(self):
        print ('entering control mode')
    def Drive(self, velocity, radius):
        print ('driving with velocity ' + velocity + ' and radius ' + radius)
    def Dock(self):
        print ('docking robot')
    def Stop(self):
        print ('i have stopped')
