# redbadger_challenge
Coding challenge for Red Badger


See the Conding_Challenge.pdf for instructions. 


## Thought process
I had planned to create a docker container for this using python 3.12 slim. Howver that turned out to be complete overkill. The docker files still exist in the root folder, which I will leave in place. 
I still went ahead with a python 3.12.12 venv in pyenv - I used this version of python as I have worked in it before and I wasn't going to explore the later versions in the short time.

I wanted to create an api backend that has the controller functions, but as I began, a more simpler approach overruled any bigger aspirations, also had a strange issue at the beginning when setting up the app where the db wasn't being created. I could however take a peak at other applications I had created previously to take some information from those.

On the frontend I somewhat got what I wanted to display, showing a grid and "Robot" direction. I gave chatGPT my expected out here and got some elements and styling suggested - though I've customised it a lot more, adding spacing, buttons, margin lines, and also removing all the suggested inputs.

The idea with the database was to show all missions, which was very easily change to be able to "reset" a mission.

There are a few instructions which I never got to, such a using the robot scent to determine where not to go off, but with time contrainst and family obligations I unfortunately had to leave it.



## To run the app
- setup a python virtualenv:
python3 -m venv venv 

- activate the virtualenv:
. venv/bin/activate

- run the app:
python main.py

- to run tests:
  pytest -v tests.py -- running the tests seems to delete /instance/robots.db, git checkout the database if it's required again
  
