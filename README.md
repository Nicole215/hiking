# Hiking - Game
Hiking is a text based adventure game, where the player goes on a virtual organized hike. At service points the hiker can get a map, drinks and snacks. But when the hiker makes a bad choice, the hike is over.
![Screenshot 2024-08-29 200135](https://github.com/user-attachments/assets/9aca3b8a-22a0-401a-b464-5c154329dd9f)
You can go on your hike [here](https://hiking-b532d6d90183.herokuapp.com/)
## User Experience
- As a player
  - I want to play an easy game
  - I always want to see what to input to make a choice
  - I want to get feedback by the game
## Design
### Flowchart
I used [app.diagrams.net](https://app.diagrams.net/) to create a flowchart.
![Screenshot 2024-08-29 203001](https://github.com/user-attachments/assets/75713dc7-0a58-43d8-b562-beb92518e3fe)
### Color scheme
- To make it easier to read, I used different colors in the game.
- Questions are green.

![Screenshot 2024-08-29 131516](https://github.com/user-attachments/assets/532bc3c8-5527-4cd6-8f73-be93e6a341af)

- When the hike ends because of a wrong choice, feedback is given in red.
  
![Screenshot 2024-08-29 131538](https://github.com/user-attachments/assets/a130b85d-a771-4bae-a0a7-597e5c7e2261)

- A cheerful yellow let's the hiker know he made it to the end.

![Screenshot 2024-08-29 212319](https://github.com/user-attachments/assets/b2ccd434-fb04-4f91-899e-814f84fcbc3e)

## Features
- All inputs have error messages that let the player know when their input was incorrect.
- Player can quit anytime, but like in real life hikes, quitting leaves the hiker in the middle of nowhere by himself.
- User name is used throughout the game to make the user feel like a member of a great community.
### Future Features
The code was written in an easy to read and also easy to expand way. It is possible to extend the hike and add more service points.

![Screenshot 2024-08-29 120359](https://github.com/user-attachments/assets/aaa47e75-72b9-462e-8b20-56ed5017540a)

## Testing
The code was tested using the PEP8 [link](https://pep8ci.herokuapp.com/) provided by Code Institute. Some lines were to long and I rewrote the code until the test came back all clear.

![Screenshot 2024-08-29 133955](https://github.com/user-attachments/assets/2daa9938-d082-43a4-84ba-6f1956640657)

The site was also tested using Lighthouse:

![Screenshot 2024-08-29 195800](https://github.com/user-attachments/assets/6446e3e9-09e7-469c-9100-a7b693279983)

### Manual Testing
- During coding I continually tested each function whether it was working correct and leading to the expected next function.
- While testing I entered the correct and the wrong choices.
- I also tested several invalid inputs to see if it always gives the correct error message.
- After deploying I did the same testing in the Code Institute's Heroku Termial.
### Bugs
During development the code was constantly tested. At time of deployment there were no bugs that I know of.
## Technologies  used
#### Language
- Python
#### Others
- [Colorama](https://pypi.org/project/colorama/) to add some color
- [Heroku](https://dashboard.heroku.com/apps) to deploy the game
- [app.diagrams.net](https://app.diagrams.net/) to create the flowchart

## Deployment
This project was deployed using Code Institute's mock terminal for Heroku
- Log into Heroku or create an account
- Click "Create new app"
- Click "Settings" and scroll down to Config Vars
- In the KEY input field, enter "PORT"
- In the VALUE input field next to it, enter "8000"
- Confirm by clicking "Add"
- Still in "Settings" scroll down to Buildpacks
- Select Python and save changes
- Still in Buildpacks, select Nodejs and save
- Make sure, the Python buildpack is above the Nodejs buildpack
- Click "Deploy" in the top navbar
- Select "GitHub" and click "Connect to GitHub"
- Choose the GitHub repository you want to deploy and confirm by clicking "connect"
- Scroll down and click on "Deploy Branch"
- Once the app is deployed, a button to view the app will be provided
## Credits
- The game is based on real life experiences that i have gained as a participant in various hiking events.
- To avoid endless if-elif nesting I googled for alternatives and found this [tutorial](https://www.youtube.com/watch?v=pEfBKamHJew).
- To use the user name throughout the game, my mentor Rory Patrick Sheridan advised me to pass the name as an argument and avoid using a global variable.
- To install Colorama, I used this [tutorial](https://www.youtube.com/watch?v=u51Zjlnui4Y)
