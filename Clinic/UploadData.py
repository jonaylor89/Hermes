
import sys
import time
import requests
import json
import random

from temp_read import read_temperature

room_number = sys.argv[1]
Age = sys.argv[2]

firebase_url = 'https://healthhacks2017-ec6bf.firebaseio.com/Clinic/'

time_hhmmss = time.strftime('%H:%M:%S')

data = {'time':time_hhmmss,
        'age': int(Age),
        'sex': 'Male',
        'temperature': read_temperature(),
        'SpO2': 0.05 * math.sin() + 0.97,
        'HR': random.choice([90, 91, 92]),
        'systolic BP': random.choice([90, 100, 95, 91, 150, 110, 96, 93, 98, 100, 89])}

result = requests.post(firebase_url + 'Room_' + room_number + '.json', data=json.dumps(data))
