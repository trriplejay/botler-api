import pyrobot
import time


def doStuff(r, key):
    print('key is ' + key);
    if key == "a":
        r.TurnInPlace(150, 'ccw');
    elif key == "d":
        r.TurnInPlace(150, 'cw');
    elif key == "w":
        r.DriveStraight(300);
    elif key == "s":
        r.DriveStraight(-300);
    elif key == "f":
        r.Control();
    elif key == "p":
        r.Passive(); 
    else:
        r.Stop();



def get_roomba():
    r = pyrobot.Roomba() #declare a roomba
    r.Control() #wake up the roomba (get control of it)
    time.sleep(.2) #sleep a bit before using
    return r
if __name__ == '__main__':
    r = get_roomba() #gain control of roomba in full mode

 #   thread.start_new_thread(stream_Video,("",))#start a thread to stream the video
    #draw_and_control("")#enter the main pygame loop
    print('use wasd to control the roomba');
    while 1:
      press = input();
      doStuff(r, press);
