# test task class with task objects and functions
from flask import Flask, request, render_template
from datetime import date
import uuid

class Tasks:
  def __init__(self, ID, taskName, taskType, createDate, taskDueDate, taskLocation, taskInvite, taskReminder):
    self.ID = uuid.uuid4()
    self.name = taskName
    self.type = taskType
    self.createDate = date.today()
    self.dueDate = taskDueDate
    self.location = taskLocation
    self.invites = taskInvite
    self.reminder = taskReminder

class Reminders:
  def __init__(self, ID, reminderName, reminderCreateDate, reminderDueDate, reminderLocation, reminderInvite, reminderRecurr):
    self.ID = uuid.uuid4()
    self.name = reminderName
    self.createDate = date.today()
    self.dueDate = reminderDueDate
    self.location = reminderLocation
    self.invites = reminderInvite
    self.recurr = reminderRecurr

# Flask constructor
app = Flask(__name__)   

# A decorator used to tell the application
# which URL is associated function
@app.route('/taskHome', methods =["GET", "POST"])
def createNewTask():
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
      
    return render_template("taskHome.html")

# A decorator used to tell the application
# which URL is associated function
@app.route('/reminderHome', methods =["GET", "POST"])
def createNewReminder():
    if request.method == "POST":
       # getting task ID using UUID
       reminderID = str(uuid.uuid4())

       # task create date using datetime
       reminderCreateDate = date.today()

       # getting input with taskName = taskName in HTML form
       reminderName = request.form.get("reminderName")
       # getting input with taskType = taskType in HTML form 
       reminderDateDue = request.form.get("dateDue")
       # getting input with taskType = taskType in HTML form 
       reminderLocation = request.form.get("reminderLocation")
       # getting input with taskType = taskType in HTML form 
       reminderInvite = request.form.get("reminderInvite")
       # getting input with taskType = taskType in HTML form 
       reminderRecurr = request.form.get("reminderRecurr")

      # create task object
      newReminder = Reminders(reminderID, reminderName, reminderCreateDate, reminderDateDue, reminderLocation, reminderInvite, reminderRecurr)

    return render_template("reminderHome.html")

if __name__=='__main__':
   app.run()
 