# SSO-ScreenShot-Organiser
Organize and automate the task of handling snaps of slides/lecture notes/files

## Motivation
>Scored pretty low on my end-semester exams, as I didn't have good notes :cry:

>To prepare and hype-up myself for the upcoming semester, I thought I should ease up some of my note-taking work. So there it is, my motivation for building this program :blush:

## How to use ?
1. Download and open the SSO python file in any text-editor :computer:
2. Change the :
    - **New_Folder** string with the location of your Storage folder <br>
    For example, if you want to store the screenshots for the course M1 *(Mathematics)* and you wish to organise them into a folder into M1 folder(which is present in the D drive, 2-2 folder), replace "F:\2-2\{}" with "D:\2-2\M3\{}"
    ```py
        New_Folder = r"F:\2-2\{}" .format(today().strftime('%I %p %d %b')) 
    ```
    Replace with
     ```py
        New_Folder = r"D:\2-2\M1\{}" .format(today().strftime('%I %p %d %b')) 
    ```
    - **src** string with the location of your Screenshot folder <br>
    TO know your Screenshot Folder, Open file explorer and click on the *Pictures* under *This PC* sub-heading. You should now be able to see the Screeenshot's folder.If not, google your way around :stuck_out_tongue_closed_eyes:
    ```py 
        src = r"C:\Users\Swastik\Pictures\Screenshots"
    ```
    Replace with
    ```py 
        src = r"Your_Screenshot_Folder_Address"
    ``` 
3. The previous steps need to be repeated incase you would be taking Screenshots for multiple Courses/subjects.Else, we are done with the editing part, **ALMOST**.
4. Incase your lecture is/was of more than 1 hour, change the variable **x** to the number of hours your lecture is going to take place.
5. Incase your work was one timer, you may now execute the program. Elsewise, depending on your OS you may want to undergo **complete automation** for an entire semester:
    - [Windows](https://www.windowscentral.com/how-create-automated-task-using-task-scheduler-windows-10) : Use **Task Scheduler** to set the timings for the execution of the various SSO-course python files at the time of end of each lecture to a weekly status.
    - [Linux](https://code.tutsplus.com/tutorials/scheduling-tasks-with-cron-jobs--net-8800) : Use **Cronjob**, as a linux-user you must be knowing it! :no_mouth:


After all this work, its time to consume the fruits of your labour.Take Screenshots with *Win + Prt Scr* or your set hotkey for taking Screenshots and let SSO handle the task of organising them into your study folder each course.
#### NOTE 
 Be sure to organise the time of execution of this program so that past 1 hour of SS are organized.For example, for the M1 course, if the class is from 3-3:50 PM, Schedule the SSO's execution at 3:55 PM so that all SS since 2:55 PM are organized into the M1 folder.
## Installation
- Install Python *(Preferably 3.9 version)*
- Thats all, Unless you **do not** have the basic modules such as datetime, os, etc. present locally on your system. In that case, install them with pip or again google your way around :stuck_out_tongue_closed_eyes: 

## Built with
- [Python] 
