# SSO-ScreenShot-Organiser
Organize and automate the task of handling snaps of slides/lecture notes/files

## How to use ?
1. Download and open the SSO python file in any text-editor
2. Change the :
-[New_Folder] *(destination)* string with the location of your Storage folder
For example, if you want to store the screenshots for the course M1 *(Mathematics)* and you wish to organise them into a folder into M1 folder(which is present in the D drive, 2-2 folder), replace "F:\2-2\{}" with "D:\2-2\M3\{}"
-[src] *(source)* string containing the location of your Screenshot folder
TO know your Screenshot Folder, Open file explorer and click on the *Pictures* under *This PC* sub-heading. You should now be able to see the Screeenshot's folder.If not, google your way around :stuck_out_tongue_closed_eyes: 
3. The previous steps need to be repeated incase you would be taking Screenshots for multiple Courses/subjects.Else, we are done with the editing part, ALMOST.
4. Incase your lecture is/was of more than 1 hour, change the variable x to the number of hours your lecture is going to take place.
5. Incase your work was one timer.You may now execute the program. Elsewise, depending on your OS you may undergo complete automation for an entire semester:
-[Windows] : Use Task Scheduler *(google for usage)* to set the timings for the execution of the various SSO-course python files at the time of end of each lecture to a weekly status.
-[Linux] : One word; Cron job.

## Installation
-Install Python *(Preferably 3.9 version)*
Thats all, Unless you do not have the basic modules such as datetime, os, etc. present locally on your system. In that case, install them with pip or again google your way around :stuck_out_tongue_closed_eyes: 

## Built with
- [Python] 
