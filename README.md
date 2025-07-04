## Introduction
On a Windows device, I often open the app PC Manager. There is a boost button that deletes temp files, but the app does this automatically when the size is more than 1GB. This script automates this so you do not have to manually do it everytime or wait for it to reach 1GB.

# Steps
1). Make sure you have Python installed

2). `Win + R` and enter `taskschd.msc` to open the Task Scheduler

3). Create a Task (not "Create Basic Task"). Make sure you have selected "Run with highest privileges".

4). Click New to create a new trigger in the Triggers tab.

Begin the task: Choose "On a schedule".

Set the Schedule to repeat every 10 minutes:

Daily: Set a start date/time.

Repeat task every: Set to 10 minutes and for a duration of: Indefinitely (or set a time limit as needed).

5). Click New to create a new action in the Actions tab.

Action: Choose "Start a program".

Program/script: Browse to the path of python.exe.

Add arguments: In this field, type the path to this script like "C:\scripts\boost_performance.py"
