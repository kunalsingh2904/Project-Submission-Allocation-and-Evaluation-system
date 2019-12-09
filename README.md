# Project-Submission-Allocation-and-Evaluation-system
Colleges, Universities or any Educational Institutes conduct projects or give Assignment for the better understanding of the practical approach towards the subject in the real world. And the project involves a lot of tasks like abstract or synopsis evaluation, thesis correction and updating the proposed module with your guides.


## PROPOSED WORK
  1. Registration or Login Module
  2. Upload/Download Module
  3. Previous submission Module
  4. User Module
  5. Open project Module
  6. Admin Module
 

This Project will help in building a collaborative system for students as well as professor
for performing assignment/project related tasks. This system has overcome all the
traditional process of manually submitting the project abstracts, synopsis or any other
Documents. Also it provides a platform where Instructor can allot tasks to their
respective group and student can choose his group as well as can choice his project
guide. Open Project related tasks can be allotted by the project guide and other
faculties can give reviews over it if they wish to. Students can directly upload their
proposed work and the documentation on this system for evaluation of the work. At the
end of the semester/year, based on the performance of the students, admin can
generate a report for the academics and grading of the student.

## requirements:
  1. python 3.7
  2. django 2.2

## how to run
  1. Download code and keep it inside a directory("moodle")
  2. create another directory with name "Moodle_files" at same location of "moodel".
     You can change Moodle_files name if you want but you will have to change it in settings also.
     this directory is for file and image storage.
  3. go to moodle/Moodel/settings.py and give your email-id and password at required place
  4. go to moodle 
  5. run following command:
      1. python manage.py makemigrations
      2. python manage.py migrate
      3. python manage.py createsuperuser
      4. python manage.py runserver
  6. open localhost on web browser.
      
