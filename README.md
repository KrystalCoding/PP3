# Plant Quiz

! Insert image responsiveness

[_Click here to view live deployment_](https://plant-quiz.herokuapp.com/)

This featured low level Python game deploys to a console.

The quiz game consists of a short welcome message to get the player's desired username, and then 13 quextions which each have 4 answers to choose from. All data is in the run.py file, nothing is imported to an external file.

The game code contains functions both to score the right and wrong answers at the end, as well as stop the player from entering anything other than answers as digits: 1, 2, 3, and 4.

# _Content Menu_

- [_Content Menu_](#content-menu)
- [_Features_](#features)
  - [_How To Play_](#how-to-play)
  - [_Game Elements_](#game-elements)
    - [\_1 - Welcome \_](#_1---welcome-_)
    - [_2 - Player_](#2---player)
    - [_3 - How To Play_](#3---how-to-play)
    - [_4 - Saved Score Viewing_](#4---saved-score-viewing)
    - [_5 - Displayed Riddles_](#5---displayed-riddles)
    - [_6 - Correct Answer_](#6---correct-answer)
    - [_7 - Incorrect Answer_](#7---incorrect-answer)
    - [_8 - Invalid Entries_](#8---invalid-entries)
    - [_9 - Final Score_](#9---final-score)
    - [_10 - Saving Scores_](#10---saving-scores)
    - [_11 - Play Again_](#11---play-again)
    - [_12 - Game End_](#12---game-end)
  - [_Data Storage_](#data-storage)
  - [_Implemented Features_](#implemented-features)
  - [_Features to be Implemented_](#features-to-be-implemented)
- [_Design_](#design)
- [_Bugs_](#bugs)
- [_Testing_](#testing)
- [_Validation_](#validation)
- [_Technologies_](#technologies)
- [_Deployment_](#deployment)
  - [_1 - Version Control_](#1---version-control)
  - [_2 - Page Deployment_](#2---page-deployment)
- [_Credits_](#credits)

# _Features_

## _How To Play_
    
 * The player will be prompted to enter their desired username.
 
 * Skipping the name input will stop the user from saving there score.
 
 * The player can display scores that have been saved.
 
 * This is a multiple choice game prompting the player to select the corret answer for the riddles from a choice of 3 answers.
 
 * The idea of the game is to get as many correct as possible.
 
 * The player will be able to save there score at the end of the game(if name has been entered)
 
 * There is a play again prompt allowing the player to play again.

## _Game Elements_

### _1 - Welcome _

 * is a simple Welcome to riddles header

![Welcome](documents/readme-images/welcome.png)

### _2 - Player_

 * After the welcome header the player will be prompt to enter there mane or press enter to continue.
 
 * This then take the player to the [How To Play](#3---how-to-play) section.

![Player](documents/readme-images/player.png)

### _3 - How To Play_

 * This explains to the player How to play the game.

 * This is outputted as soon as the player has either entered ther name or pressed enter to skip.

 * The has a prompt saying 'Press Enter To Continue' and this will take the palyer to [See Saved Scores](#4---saved-score-viewing) prompt.

![How To Play](documents/readme-images/how-to.png)

### _4 - Saved Score Viewing_

 * The player is prompt with asking to view the saved scores and asked to type 'Yes', 'Or Press Enter To Continue'. 

 * Typing yes will Show the stored scores and display this table below.

 * Pressing enter then the player is taken to the [Riddles](#5---displayed-riddles)

 * If the player is at the end of the game then pressing enter will take then to [Play Again](#11---play-again) to allow the player to either exit or restart.

![Saved Score Viewing](documents/readme-images/open-saved-scores.png)

 * This table will show if the user has requested viva the prompt.

 * It shows the name, score and the preceentage of each player that has saved scores.

 * If the player has chosen to save there score at the end of the game, there is another prompt to allow then to view the scores.

 * At the bottom of there table there is a message saying 'Press Enter To Contiune'.

 * If the player is at the begining of the game this will take the player to the [Riddles](#5---displayed-riddles) to begin playing.

 * If the player is at the end of the game then this will take the player to [Play Again](#11---play-again) to allow the player to either exit or restart.

![Score Table](documents/readme-images/score-table.png)

### _5 - Displayed Riddles_

 * The player will be Shown a message saying 'Good Luck' before the first riddle only.

![Good Luck](documents/readme-images/good-luck.png)

 * Then the player will be pressented with the first riddle.

 * This shows The player What riddle there are currently on first.

 * Then Shows The riddle.

 * Then Shows The options to choose from.

 * Then the player is prompr to Type 'A', 'B' or 'C'.

 * Once the player has answered the user will be prompted with the correct output.

 * If the player answers correctly then ['You Answered Correctly'](#6---correct-answer) message is show with the current score.

 * If the player answers incorrectly then ['Sorry Wrong Answer'](#6---correct-answer) message is show with the current score.

 * If the player answers enters an incorrect value then th you ['Incorrect Value'](#6---correct-answer) message is show a prompt saying enter A, B or C. 

 * This will be the same steps untill the 20th riddle is answered.

![Displayed Riddles](documents/readme-images/riddles.png)

### _6 - Correct Answer_

 * If the player answers the riddle correctly then this 'You Answered Correctly' message will show.

 * The players score will increase by one point and display their currnt score below.

![Correct Answer](documents/readme-images/correct-answer.png)

### _7 - Incorrect Answer_

 * If the player answers the riddle incorrectly then this 'Sorry Wrong Answer' message will show.

 * The players score will not change but will display their currnt score below.

![Incorrect Answer](documents/readme-images/wrong-answer.png)

### _8 - Invalid Entries_

 * Whilst the player is answering the riddles and does not enter 'A' or 'a', 'B' or 'b', 'C' or 'c'

    this incorrect value message will show and prompt the user to enter A, B or C.

![Invalid Enterys](documents/readme-images/incorrect-value.png)

### _9 - Final Score_

 * After the play has answered all the riddles this final score message will show.

 * The final score message will show the player their score with an accuracy percentage aswell.

 * IF a player get all 20 riddles correct the will be pressented with a 'CONGRATULATIONS (Players Name) YOU ARE A RIDDLE MASTER' message.

![Top Score](documents/readme-images/top-score.png)
 
 * Then the user will be prompted with [To Save Your Score](#10---saving-scores)* or [See Saved Scores](#4---saved-score-viewing).

    *(only displays when player provides a name, is shown before 'See Saved Scores'  if name is provided).

### _10 - Saving Scores_
 
 * This is option only shows whan a player has provided a name. 

 * if a name is not given the use will be prompted with the [See Save Scores](#4---saved-score-viewing). (See Above For Details).

 * If the player had given a name then they will be asked if they would like to save there score and asked to type 'Yes', 'Or Press Enter To Continue'.

![Saving Scores](documents/readme-images/save-score.png)

 * If the user Types Yes then The 'Uploading Score" message will show first and once the proccess has finished the 'Successfully Added' message will appear.

 * Then the user will be prompted with the [See Save Scores](#4---saved-score-viewing). (See Above For Details).

![Saved Scores](documents/readme-images/score-saved.png)

 * If the player presses enter then this process will be skipped and the user will be prompted with the [See Save Scores](#4---saved-score-viewing). (See Above For Details).

### _11 - Play Again_

 * The player will be prompt with 'Play Again' message and asked to type 'Yes', 'Or Press Enter To Conintue'.

 * If the player types yes the the game will loop back to the how to play screen so the player can start again.

 * If the plyer presses enter to continue the game will procceed to end.

![Play Again](documents/readme-images/play-again.png)

### _12 - Game End_

 * After the player has pressed enter not to play again, this 'Thank You For Playing' message is deployed.

![Game End](documents/readme-images/end.png)

## _Data Storage_
 
 * The data for this game is exchanged using google sheets

 * The riddles are generated from a worksheet riddles that holds all the riddles, answer options and correct answer indicater.

 * The player scores are saved to another worksheet scores that then is inputted back to the score table.

## _Implemented Features_

 * Has difreent colour outputs so show the different types of information shown to the player.

 * has a save funtion to save the players scores.

 * Has a function to resart the game.

 * Easily able to implent more riddles buy inputting them to the google sheet worksheet
  
## _Features to be Implemented_

 * Change the score table from showing all saved scores to the top 10 higest scores.

# _Design_
 
 * This flow chart shows how the game responds within the different sections.

 * This flow chart will Help through the testing to determine whether the game responds as it should.

 ![Flow Chart](documents/readme-images/flow-chart.png)

# _Bugs_

 * Through testing there are no current known bugs within the game
 
 * Throught development there was a bug of same questions being show more than once within one game sequence
    * which was fixed using an if statment to check if a generated item had been used already.

# _Testing_

| Test     | Expected      |   Outcome  | 
| :----     |    :----   |  :---- | 
|Run run.py| run.py loads, Welcome banner appears, player name prompt, appears| As Expected |
|Enter Player Name and press enter | How To Play Information appear| As Expected|
|Press enter on how to play|Loads To See Saved Scores Prompt| As Expected|
|Type yes on To See Saved Scores Prompt and Press enter|Loads Saved Scores Table|As Expected|
|Press enter on Saved Score Table to Continue|Loads Good Luck Banner And first Riddle|As Expected|
|Enter C For Correct Answer|Loads Correct Answer Output and Score Output with score of 1, Loads Second Riddle|As Expected|
|Enter B for Wrong Answer |Loads Wrong Answer Output and Score Output with score of 1, Loads Third Riddle|As Expected|
|Enter C For Correct Answer|Loads Correct Answer Output and Score Output with score of 2, Loads fourth Riddle|As Expected|
|Enter A for Wrong Answer |Loads Wrong Answer Output and Score Output with score of 2, Loads fith Riddle|As Expected|
|Enter B For Correct Answer|Loads Correct Answer Output and Score Output with score of 3, Loads sixth Riddle|As Expected|
|Enter C for Wrong Answer |LoadsWrong Answer Output and Score Output with score of 3, Loads Seventh Riddle|As Expected|
|Enter C For Correct Answer|Loads Correct Answer Output and Score Output with score of 4, Loads 8th Riddle|As Expected|
|Enter D For Incorrect Value|Loads Incorrect Value Output, And Enter (A, B, C)  Prompt|As Expected|
|Press Enter With No Input|Loads Incorrect Value Output, And Enter (A, B, C)  Prompt|As Expected|
|Randon Select Rest of Riddle Answers  untill final Riddle|Diplay Outputs According to Correct, or Wrong Answers|As Expected|
|Enter Last Riddle Choice|Displays Correct Output Depening on selection, Loads Finall Score Output, Loads Save Score Prompt|As Expected|
|Type yes to Save Score|Shows Uploading output, Shows Successful output, Loads See Saved Scores Prompt|As Expected|
|Type yes on To See Saved Scores Prompt and Press enter|Loads Saved Scores Table|As Expected|
|Press enter on Saved Score Table to Continue|Loads Play Again Prompt|As Expected|
|Type Yes On Play Again Prompt|Loads Up How To Play Output|As Expected|
|Press enter on how to play|Loads To See Saved Scores Prompt|As Expected|
|Press Enter To Skip Score Table |Loads Good Luck Banner And first Riddle|As Expected|
|Randomly Selectect Answers To all 20 Riddles|Diplay Outputs According to Correct, or Wrong Answers, Loads Save Score Prompt|As Expected|
|Press Enter To SkipSave Score|Loads See Saved Score Prompt|As Expected|
|Press Enter To See Saved Score Score|Loads Play Again Prompt|As Expected|
|Press Enter To Skip Play Again Prompt|Loads Thank you for playing Output, Game ends|As Expected|
|Load run.py Skip player Name,|Load welcome banner and Player prompt, loads how to play output|As Expected|
|Press enter to continue, and press enter again to not load score table|Loads see saved score prompt, loads goodluck banner and first riddle|As Expected|
|Randomly Selectect Answers To 19 Riddles|Diplay Outputs According to Correct, or Wrong Answers, Loads Save Score Prompt|As Expected|
|Enter Last riddle|Correct ouptput shows depending in Answwer given, Final Score output shows, See Saved Scores prompt|As Expected|
|Press Enter To Skip Save Score|Loads See Saved Score Prompt|As Expected|
|Press Enter To Skip See Saved Score Score|Loads Play Again Prompt|As Expected|
|Press Enter To Skip Play Again Prompt|Loads Thank you for playing Output, Game ends|As Expected|

# _Validation_

 * This game passes through the [Code Institute PEP8](https://pep8ci.herokuapp.com/) Validator with no errors.

![Validation](documents/readme-images/validation.png)

# _Technologies_

 * Python is the main programming language to produce the game.
  
 * rich was imported.
      * Table - To create the table in Saved Scores. 
      * Box - For the outline of the table in Saved Scores. 
      * Console - For the colour styling for the output to the console.
  
 * random was imported to handle the random numbers to select the riddles at random.
  
 * gspread was imported to handle the access to the google sheets data.
  
 * google.oauth2.service_account import Credentials was used to handle the access to the google drive where the google sheet is stored.

 * [LucidChart](https://www.lucidchart.com/pages/) used to create the flow chart showing the game's functionality and flow.

 * [GitHub](https://www.github.com) was used to hold the game repository files.

 * [Gitpod](https://www.gitpod.io) was used for the coding environment.

 * [Heroku](https://www.heroku.com) was used to deploy the game to the web.
 
 * [NHC Debut Video](https://www.nchsoftware.com/capture/download-now.html?ns=true&kw=nch%20debut%20video&gclid=Cj0KCQjwxYOiBhC9ARIsANiEIfaBgkFY226We0Niciqf_go8kAI_hYrSRyhBh2FvxDuEqUfzJi1j0YoaAtjGEALw_wcB) Capture used to screen recored the game play for gif.

 * To create the gif [ezgif.com](https://www.ezgif.com) was used

# _Deployment_

## _1 - Version Control_

 Verion controle was maintained using GIT within GitPod to push code to the GitHub repository

 * From the Gitpod terminal use "git add ." which tells git you would like to make changes/updates to the files.

 * Then use "git commit -m " with a comment, this will commit the changes and update the files.

 * Then using the "git push" command this will push the committed changes to your GitHub repository.

## _2 - Page Deployment_

 * Go to Heroku and log in

 * click "New" to create a new app from the dashboard

 * Choose app name and select your region, press "Create app".

 * Go to "Settings" and navigate to Config Vars.

 * Add Config Vars. 
    * This app used two 
        * One for the credentials to allow access to the google sheets. KEY = CREDS : VALUE = CREDS.json content.
        * Second KEY = PORT : VALUE = 8000.
 
 * Add buildpacks Python and NodeJS in this order.
 
 * Now go to the Deploy tab.
 
 * Scroll Down to Deployment Method and select GitHub.
 
 * Select repository to be deployed and connect to Heroku.
 
 * Now Scroll down to depoly : 
    * Option 1 is selecting Automatic deploys (Will Update Automaticly when every git push to the repository).
    * Option 2 is selecting Manual deploy (Needs to be redeployed after every change manually via Heroku deploy tab).

 Visit the live deployment [HERE](https://plant-quiz.herokuapp.com/).

# _Credits_

 * I used a fellow student's "Riddles" code for this README.md format inspiration: [A. Croshaw](https://github.com/A-Croshaw/Riddles/blob/main/README.md)

 * Much of the run_game function was inspired by (and learned from) Code Institute's walkthrough project: [love_sandwiches](https://github.com/KrystalCoding/Love-Sandwiches)

 
 * For Python code functionality, I borrowed advice and bits of code from: [python.org](https://www.python.org/), [w3schools](https://www.w3schools.com/python/default.asp), and [stackoverflow](https://stackoverflow.com/)