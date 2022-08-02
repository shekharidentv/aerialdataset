import os
import sys
sys.path.append(os.getcwd())
# os.chdir("airborne-detection-starter-kit/data")
sys.path.append("airborne-detection-starter-kit")
import random

from core.dataset import Dataset
from random import randrange, choice
notebook_path = os.path.dirname(os.path.realpath("__file__"))

local_path = notebook_path + '/part1'
s3_path = 's3://airborne-obj-detection-challenge-training/part1/'
dataset = Dataset(local_path, s3_path, partial=True, prefix='part1')


all_flight_ids = dataset.get_flight_ids()
lucky_flight_id = random.choice(all_flight_ids)
lucky_flight = dataset.get_flight_by_id(lucky_flight_id)


print(lucky_flight)

print("This flight has **%s frames** and total **%s airborne objects**." % (lucky_flight.num_frames, lucky_flight.num_airborne_objs))

for airborne_obj in lucky_flight.get_airborne_objects():
    print("- %s " % airborne_obj)

assert lucky_flight.num_airborne_objs > 0, "Unlucky draw; this flight sequence have 0 airborne objects; please re-run this cell"

image = lucky_flight.get_frame(choice(list(lucky_flight.frames.keys()))).image()
print(image)