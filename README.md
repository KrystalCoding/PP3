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
    - [_1 - Player_](#_1---player)
    - [_2 - Welcome_](#2---welcome)
    - [_3 - How To Play_](#3---how-to-play)
    - [_4 - Quiz Questions_](#5---quiz-questions)
    - [_5 - Correct Answer_](#6---correct-answer)
    - [_6 - Incorrect Answer_](#7---incorrect-answer)
    - [_7 - Invalid Entries_](#8---invalid-entries)
    - [_8 - Final Score_](#9---final-score)
    - [_9 - Play Again_](#11---play-again)
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
 
 * Skipping the name input is allowed. The line will simply be left blank.
 
 * This is a multiple choice quiz game which presents a question with four possible answers. The user is then prompted to select the correct choice from the options presented.
 
 * The goal is for the user to guess as many correct answers as possible.
 
 * At the end of the 13 randomized questions, the player's score is presented in a ?/13 format. 
 
 * Finally, there are instructions on how to play again.

## _Game Elements_

### _1 - Player_

 * The player is prompted to enter their desired username.

! [Player]()

### _2 - Welcome_

 * After the player enters their prefered username, a short welcome message is displayed.

! [Welcome]()

### _3 - How To Play_

 * This prompts the player to press Enter in order to try the quiz.

! [How To Play]()

### _4 - Quiz Questions_

 * Then player is presented with the first randomized quiz question.

 * Immediately, along with the question, appear 4 possible answers. Only one is correct.

 * Instructions to enter a number between 1-4 appear beneath the quiz question and answers. This allows the user to answer the quiz question via one of these digits: '1', '2', '3', or '4'.

 * This loop is repeated until the 13th question is answered.

! [Quiz Questions]()

### _5 - Correct Answer_

 * If the player answers the quiz question correctly, they are presented simply with the message: "Correct!"

 * The players score will increase by one point each time a correct answer is guessed. The score will be displayed at the every end.

! [Correct Answer]()

### _6 - Incorrect Answer_

 * If the player answers the quiz question incorrectly, they are presented with the message: "Incorrect. The correct answer is {correct_answer}."

 * The players score will not increase, as only correct answers are incremented. Final score is displayed after the 13th question is answered.

! [Incorrect Answer]()

### _7 - Invalid Entries_

 * If anything other than the digits 1-4 are entered as an answer, the player will receive this message: "Invalid input. Please enter a number between 1 and 4."

! [Invalid Entries]()

### _8 - Final Score_

 * After the play has answered all 13 quiz questions, their score is presented.

 * Only a total of correct answers are tallied and compared to the total number of questions.

 * If a player get all 13 answers correct they presented with a 'CONGRATULATIONS (Players Name) YOU ARE A RIDDLE MASTER' message.

![Top Score](documents/readme-images/top-score.png)
 
 * Then the user will be prompted with [To Save Your Score](#10---saving-scores)* or [See Saved Scores](#4---saved-score-viewing).

    *(only displays when player provides a name, is shown before 'See Saved Scores'  if name is provided).

### _9 - Play Again_

 * The player will be prompt with 'Play Again' message and asked to type 'Yes', 'Or Press Enter To Conintue'.

 * If the player types yes the the game will loop back to the how to play screen so the player can start again.

 * If the plyer presses enter to continue the game will procceed to end.

![Play Again](documents/readme-images/play-again.png)

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