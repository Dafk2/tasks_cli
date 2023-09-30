import click
import json_manager

@click.group()
def cli():
  pass

@cli.command()
@click.pass_context
def task (ctx):
  name = input('Enter name of task: ')
  description = input('Enter description of task: ')
  
  tasks = json_manager.readJson();

  task = {
    'id': len(tasks) + 1,
    'name': name,
    'description': description,
    'complete': False
  }

  tasks.append(task)
  json_manager.writeJson(tasks)
  
  print(
    f'Task created successfully \nname: {name}\n' \
    f'description: {description}\n' \
    f'complete: {task["complete"]}'
  )

# get all task
@cli.command()
def tasks ():
  result = ''
  tasks = json_manager.readJson() 
  if not tasks:
    print('No task has been created')

  for task in tasks:
    result += f'{task["id"]}: name: {task["name"]}\n' \
          f'description: {task["description"]}\n' \
          f'completed: {task["complete"]}\n\n'

  print(result)

@cli.command()
@click.argument('id', type=int)
def getTaskId(id):
  tasks = json_manager.readJson()

  task = next((task for task in tasks if task["id"] == id), None)
  print(f'name: {task["name"]} description: {task["description"]}')

@cli.command()
@click.argument('id', type=int)
@click.option('--name', required=True, help='name of the task')
@click.option('--description', required=True, help='description of the task')
def updateTask (id, name, description):
  tasks = json_manager.readJson()
  task = next((task for task in tasks if task["id"] == id), None)
   
  for task in tasks:
    if task["id"] == id:
      if not task["description"] == description:
        task["description"] = description
      
      if not task["name"] == name:
        task["name"] = name
      break  

  json_manager.writeJson(tasks)  

  print(f'Task with id {id} updated successfully')

@cli.command()
@click.argument('id', type=int)
def deleteTask(id):
  tasks = json_manager.readJson()
  task = next((task for task in tasks if task['id'] == id), None) 

  if task is None:
    return print(f'Task with id {id} not found')

  tasks.remove(task)

  json_manager.writeJson(tasks)
  print(f'Task with id: {id} deleted successfully')

@cli.command()
def completeTask():
  tasks = json_manager.readJson()
  if not tasks:
    return print('No task has been created')

  print(f'=========================================== \n\nAll Task:') 
  for task in tasks:
    print(
      f'{task["id"]} name: {task["name"]}\n' 
      f'description: {task["description"]}\n'
      f'completed {task["complete"]}\n'
    )
  print(f'===========================================\n')
 
  try:
    option = input('Enter the number of the task you want to mark as complete: ')  

    for task in tasks:
      if(int(option) == task['id']):
        task['complete'] = True
        print(f'{task["id"]} complete: {task["complete"]}')
        break   

  except ValueError:
    print('Invalid input. Please enter a valid task number.')
    return

  json_manager.writeJson(tasks)
