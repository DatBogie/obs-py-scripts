import obsws_python as obs
import pytweening, os, tty, sys, termios, select, math
from time import sleep, time, time_ns
from pathlib import Path
from random import randrange, choice
from dotenv import load_dotenv
load_dotenv()
cl = obs.ReqClient(host=os.environ.get("OBS_HOST"),port=int(os.environ.get("OBS_PORT")),password=os.environ.get("OBS_PASSWORD"))

IMAGES_DIR = "./random_images"
IMAGES = []

for f in os.listdir(IMAGES_DIR):
    IMAGES.append(os.fspath(Path(os.path.join(IMAGES_DIR,f)).absolute()))

def show_random():
    cl.set_source_filter_settings("Bunnies","Color Correction",{"opacity":1},overlay=True)
    val = 0
    x = 0
    cl.set_input_settings("Bunnies",{"file":choice(IMAGES)},overlay=True)
    cl.set_scene_item_transform("Virtual Camera",cl.get_scene_item_id("Virtual Camera","Bunnies").scene_item_id,{
        "boundsType": "OBS_BOUNDS_SCALE_OUTER",
        "boundsWidth": 850,
        "boundsHeight": 850,
        "positionX": 800/2 - 850/2,
        "positionY": 800/2 - 850/2
    })
    st = time_ns()/1e6
    while val < 1:
        if time_ns()/1e6 - st >= 15:
            st = time_ns()/1e6
            x+=.01
            val = pytweening.easeOutSine(x)
            cl.set_source_filter_settings("Bunnies","Color Correction",{"opacity":1-val},overlay=True)
    cl.set_source_filter_settings("Bunnies","Color Correction",{"opacity":0},overlay=True)

orig_settings = termios.tcgetattr(sys.stdin)
tty.setcbreak(sys.stdin)

st = time()
x = None

print("Running...")
print("Focus terminal and press any key to quit...")

class vec2():
    def __init__(self, transform):
        self.x=transform["positionX"]
        self.y=transform["positionY"]
    x:float=0
    y:float=0

bird_id = cl.get_scene_item_id("Virtual Camera","Bird").scene_item_id
bird_pos = cl.get_scene_item_transform("Virtual Camera",bird_id).scene_item_transform
bird_pos = vec2(bird_pos)

while not x:
    if time() - st >= float(os.environ.get("OBS_SCRIPT_DEFAULT_DELAY")):
        st = time()
        if randrange(1,float(os.environ.get("OBS_SCRIPT_DEFAULT_RANDOM_CHANCE_IN"))+1) == 1:
            show_random()
    cl.set_scene_item_transform("Virtual Camera",bird_id,{
        "positionX": bird_pos.x + math.sin(time())*20,
        "positionY": bird_pos.y + math.cos(time())*20,
        "rotation": math.sin(time())*5,
        "alignment": 0
    })
    if select.select([sys.stdin],[],[],0) == ([sys.stdin],[],[]):
        x = sys.stdin.read(1)

print("Stopping...")

cl.set_source_filter_settings("Bunnies","Color Correction",{"opacity":0},overlay=True)
cl.set_scene_item_transform("Virtual Camera",bird_id,{
    "positionX": bird_pos.x,
    "positionY": bird_pos.y,
    "rotation": 0
})
termios.tcsetattr(sys.stdin.fileno(),termios.TCSADRAIN,orig_settings)