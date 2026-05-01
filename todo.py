import sys
import json
from datetime import datetime

FILE = "tasks.json"

def loadTasks():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []
    
def saveTasks(tasks):
    with open(FILE, "w") as f:
        return json.dump(tasks, f, indent=4)

def gettime():
    return datetime.now().isoformat()  

def addTask(taskDescription):
    tasks = loadTasks()
    newId = 1
    if(len(tasks)>0):
        newId = tasks[-1]["id"]+1
    
    task = {
        "id" : newId,
        "description" : taskDescription,
        "status" : "todo",
        "createdAt" : gettime(),
        "updatedAt" : gettime()
    }

    tasks.append(task)
    saveTasks(tasks)
    print(f"Task added successfully (ID: {newId})")

def listTasks(status=""):
    tasks = loadTasks()

    if status != "":
        tasks = [task for task in tasks if task["status"] == status]

    if len(tasks) == 0:
        print("No tasks found")
        return

    for task in tasks:
        print(f'{task["id"]}. {task["description"]} [{task["status"]}]')

def deleteTask(taskId):
    tasks = loadTasks()

    newTasks = [task for task in tasks if task["id"] != taskId]

    if len(newTasks) == len(tasks):
        print("Task not found.")
        return

    saveTasks(newTasks)
    print("Task deleted successfully.")

def updateTask(taskId, Newdesc):
    tasks = loadTasks()

    for task in tasks:
        if task["id"] == taskId:
            task["description"] = Newdesc
            task["updatedAt"] = gettime()
            saveTasks(tasks)
            print("Task updated successfully.")
            return

    print("Task not found.")

def markTask(taskId, status):
    tasks = loadTasks()

    for task in tasks:
        if task["id"] == taskId:
            task["status"] = status
            task["updatedAt"] = gettime()
            saveTasks(tasks)
            print(f"Task marked as {status}.")
            return

    print("Task not found.")

def main():
    if len(sys.argv) < 2:
        print("Please provide a command.")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Please provide task description.")
            return

        description = sys.argv[2]
        addTask(description)
    
    elif command == "list":
        if len(sys.argv)==2:
            listTasks()
        else : 
            listTasks(sys.argv[2])

    elif command == "delete":
        if len(sys.argv) < 3:
            print("Please provide task ID.")
            return
        else :
            deleteTask(int(sys.argv[2]))

    elif command == "update":
        if len(sys.argv) < 3:
            print("Please provide task ID and New Description.")
            return
        elif len(sys.argv) < 4:
            print("Please provide New Description.")
            return
        else :
            updateTask(int(sys.argv[2]),sys.argv[3])

    elif command == "mark-in-progress":
        if len(sys.argv) < 3:
            print("Please provide task ID.")
            return

        taskId = int(sys.argv[2])
        markTask(taskId, "in-progress")

    elif command == "mark-done":
        if len(sys.argv) < 3:
            print("Please provide task ID.")
            return

        taskId = int(sys.argv[2])
        markTask(taskId, "done")
    
    else:
        print("Unknown command.")


main()