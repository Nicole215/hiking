# Hiking - Game
Hiking is a text based adventure game, where the player goes on a virtual organized hike. At service points the hiker can get a map, drinks and snacks. But if the hiker makes a bad choice, the hike is over.
![Screenshot 2024-08-29 200135](https://github.com/user-attachments/assets/9aca3b8a-22a0-401a-b464-5c154329dd9f)
You can go on your hike [here](https://hiking-b532d6d90183.herokuapp.com/)
## User Experience
- As a player
  - I want to play an easy game
  - I always want to see what to type to make a choice
  - I want to get feedback by the game
## Design
### Flowchart
I used [app.diagrams.net](https://app.diagrams.net/) to create a flowchart.
![Screenshot 2024-08-29 203001](https://github.com/user-attachments/assets/75713dc7-0a58-43d8-b562-beb92518e3fe)
### Color scheme
- To make it easier to read, I used different colors in the game.
- Questions are green.

![Screenshot 2024-08-29 131516](https://github.com/user-attachments/assets/532bc3c8-5527-4cd6-8f73-be93e6a341af)

- When the hike ends because of a wrong choice, the feedback is given in red.
  
![Screenshot 2024-08-29 131538](https://github.com/user-attachments/assets/a130b85d-a771-4bae-a0a7-597e5c7e2261)

- A cheerful yellow let's the hiker know he made it to the end.

![Screenshot 2024-08-29 212319](https://github.com/user-attachments/assets/b2ccd434-fb04-4f91-899e-814f84fcbc3e)

## Features
- All inputs have error messages that let the player know when their input was incorrect.
- Player can quit anytime, but like in real life hikes quitting leaves the hiker in the middle of nowhere by himself.
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
- During coding I continually tested each function whether it was working correct and leading to the expected next funtion.
- While testing I entered the correct and the bad choices.
- I also tested several invalid inputs to see if it always gives the correct error message.
- After deploying I did the same testing in the Code Institute's Heroku Termial.
