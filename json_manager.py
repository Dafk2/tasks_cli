import json
import os

def readJson():
  if not os.path.isfile('tasks.json'):
    with open('tasks.json', 'w') as tasks:
      json.dump([], tasks)

  with open('tasks.json', 'r') as tasks:
    task = json.load(tasks)
    return task;    

def writeJson(task):
  with open('tasks.json', 'w') as tasks:
    json.dump(task, tasks)    