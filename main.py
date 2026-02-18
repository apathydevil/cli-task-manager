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

def clearall():
     if(os.path.exists("tasks.json")):
        os.remove("tasks.json")
        print("All tasks have been cleared!")
     else:
          print("There are no tasks to clear!")

def main():
    
    tasks = load_tasks()

    while True:
        command = input("What would you like to do (add/list/complete/clearall/quit)?").strip().lower()

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
             case "quit":
                  break
             case _:
                  print("unknown command!")
                  
if __name__ == "__main__":
    main()