import json
import os


def load_tasks():
    if(os.path.exists("tasks.json")):
        with open("tasks.json", "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
      with open("tasks.json", "w") as f:
          json.dump(tasks, f ,indent=2)

def add_task(tasks):
     task = input("Enter task: ")
     tasks.append({"id": len(tasks) + 1, "task": task, "done": False})
     save_tasks(tasks) 
     print(f"Task added!")

def list_tasks(tasks):
     if not tasks:
          print("There are no tasks yet!")
          return
     for t in tasks:
          print(f"{t['id']}. | {t["task"]} | {t["done"]}")

def complete_task(tasks):
     print("A list of all tasks:")
     list_tasks(tasks)
     targetId = int(input("Please provide the task id:"))
     for t in tasks:
          if(t["id"] == targetId):
               t["done"] = True
               save_tasks(tasks)
               print("Task has been completed!")
               return
     print("Task not found")

def remove_tasks(tasks):
     print("Here is a list of all tasks:")
     list_tasks(tasks)
     print("Would you like to remove one task, all of them or all completed tasks?")
     answer = input("Please type one, all or completed: ")
     if(answer == "all"):
          clearall()
     elif(answer == "one"):
          print("Which tasks would you like to remove?")
          targetId = int(input("Please type the id of the task"))
          original_length = len(tasks)
          tasks = [t for t in tasks if t["id"] != targetId]
          if(len(tasks) == original_length):
               print("Task not found!")
          print("Task successfully removed!")
     elif(answer == "completed"):
          numberofcompleted = 0
          for t in tasks:
               if(t["done"] != False):
                    numberofcompleted = numberofcompleted + 1
          print(f"{numberofcompleted} completed tasks found!")
          confirmation = input("Are you sure you want to remove them? yes/no ")
          if(confirmation == "yes"):
               tasks = [t for t in tasks if t["done"] == False]
               print("All completed tasks have been removed!")
          else:
               print("No tasks were removed!")
     else:
          print("Unknown command!")
     save_tasks(tasks)

def clearall():
     if(os.path.exists("tasks.json")):
        os.remove("tasks.json")
        print("All tasks have been cleared!")
     else:
          print("There are no tasks to clear!")

def main():
    
    tasks = load_tasks()

    while True:
        command = input("What would you like to do (add/list/complete/remove/clearall/quit)?").strip().lower()

        match command:
             case "add":
                  add_task(tasks)
             case "list":
                  list_tasks(tasks)
             case "complete":
                  complete_task(tasks)
             case "clearall":
                  clearall()
                  tasks = load_tasks()
             case "remove":
                  remove_tasks(tasks)
                  tasks = load_tasks()
             case "quit":
                  break
             case _:
                  print("unknown command!")
                  
if __name__ == "__main__":
    main()