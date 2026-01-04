def greet(name):
    print(f"hi {name}")
# greet("ali")   
def greet1(name):
    print(f"hi {name}")

def greet2(name):
    print(f"hi {name}")
#importing modules    

import math
print(math.sqrt(25))

#built in modules
import os
print(os.name)

#standard python libraries
import math
print(math.sqrt(16))

from datetime import datetime
now = datetime.now()
print(now) 

import os
current_dir = os.getcwd()
print(current_dir) 

import sys
print(sys.version) 

import json
data = '{"name": "John", "age": 30}'
parsed_data = json.loads(data)
print(parsed_data) 

#third party python libraries

import numpy as np
arr = np.array([1, 2, 3])
print(arr) # Output: [1 2 3]


import pandas as pd
data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
df = pd.DataFrame(data)
print(df)

import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [10, 20, 25, 40]
plt.plot(x, y)
plt.show()

import requests
response = requests.get('https://api.github.com')
print(response.status_code)

from bs4 import BeautifulSoup
import requests
page = requests.get("https://example.com")
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.title.text)

# python
# import tensorflow as tf
# hello = tf.constant('Hello, TensorFlow!')
# print(hello)

# python -m venv myenv
# myenv\Scripts\activate

