import os
import sys
sys.path.append(os.getcwd())
# os.chdir("airborne-detection-starter-kit/data")
sys.path.append("airborne-detection-starter-kit")
import random

from core.dataset import Dataset
notebook_path = os.path.dirname(os.path.realpath("__file__"))

local_path = notebook_path + '/part1'
s3_path = 's3://airborne-obj-detection-challenge-training/part1/'
dataset = Dataset(local_path, s3_path, partial=True, prefix='part1')

# You can add multi-part dataset as well, using below..
local_path = notebook_path + '/part2'
s3_path = 's3://airborne-obj-detection-challenge-training/part2/'
dataset.add(local_path, s3_path, prefix='part2')

# You can add multi-part dataset as well, using below..
local_path = notebook_path + '/part3'
s3_path = 's3://airborne-obj-detection-challenge-training/part3/'
dataset.add(local_path, s3_path, prefix='part3')



"""{
    'time': 1550844897919368155,
    'blob': {
        'frame': 480,
        'range_distance_m': nan # signifies, it was an unplanned object
    },
    'id': 'Bird2',
    'bb': [1013.4, 515.8, 6.0, 6.0],
    'labels': {'is_above_horizon': 1},
    'flight_id': '280dc81adbb3420cab502fb88d6abf84',
    'img_name': '1550844897919368155280dc81adbb3420cab502fb88d6abf84.png'
}
"""

all_flight_ids = dataset.get_flight_ids()
lucky_flight_id = random.choice(all_flight_ids)
lucky_flight = dataset.get_flight_by_id(lucky_flight_id)


print(lucky_flight)

print("This flight has **%s frames** and total **%s airborne objects**." % (lucky_flight.num_frames, lucky_flight.num_airborne_objs))

for airborne_obj in lucky_flight.get_airborne_objects():
    print("- %s " % airborne_obj)

assert lucky_flight.num_airborne_objs > 0, "Unlucky draw; this flight sequence have 0 airborne objects; please re-run this cell"