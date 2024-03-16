# test task class with task objects and functions
from flask import Flask, request, render_template
from datetime import date
import uuid

class Tasks:
  def __init__(self, ID, taskName, taskType, createDate, dueDate, taskLocation, taskInvite, taskReminder):
    self.ID = uuid.uuid4()
    self.name = taskName
    self.type = taskType
    self.createDate = date.today()
    self.dueDate = dueDate
    self.location = taskLocation
    self.invites = taskInvite
    self.reminder = taskReminder

# Flask constructor
app = Flask(__name__)   

tasksDict = {}

# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def newTask():
    if request.method == "POST":
       # getting task ID using UUID
       taskID = str(uuid.uuid4())
      
       # task create date using datetime
       taskCreateDate = date.today()
      
       # getting input with taskName = taskName in HTML form
       taskName = request.form.get("taskName")
       # getting input with taskType = taskType in HTML form 
       taskType = request.form.get("taskType")
      # getting input with taskType = taskType in HTML form 
       taskDateDue = request.form.get("dateDue")
      # getting input with taskType = taskType in HTML form 
       taskLocation = request.form.get("taskLocation")
      # getting input with taskType = taskType in HTML form 
       taskInvite = request.form.get("taskInvite")
      # getting input with taskType = taskType in HTML form 
       taskRemind = request.form.get("taskRemind")

      # create task object
      newTask = Tasks(taskID, taskName, taskType, taskCreateDate, taskDateDue, taskLocation, taskInvite, taskRemind)

      # store new task in task dict
      tasksDict[taskID] = newTask
      
    return render_template("taskForm.html")

if __name__=='__main__':
   app.run()
 