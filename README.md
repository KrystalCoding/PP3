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
  - [_Implemented Features_](#implemented-features)
  - [_Features to be Implemented_](#features-to-be-implemented)
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

 * If a player get all 13 answers correct they presented with a unique message: "Congratulations, {player_name}! You are a plant Master!"

! [Top Score]()

### _9 - Play Again_

 * The player will be prompted with a message on how to play again.

! [Play Again]()

## _Implemented Features_

 * Organized code with quiz questions at the top, very easily altered.
  
## _Features to be Implemented_

 * I would like to store the quiz questions on an external google sheet.

# _Bugs_

 * Through testing, I was made aware that the user was allowed to make an empty entry. I fixed this by running a while loop.

 * Instead of ending the quiz with instruction to the user on how to refresh the page, I inserted play_again and clear_screen functions to make a cleaner, easier, and more efficient user experience.

# _Testing_

| Test     | Expected      |   Outcome  | 
| :----     |    :----   |  :---- | 
| Run run.py | run.py loads, username prompt appears | As Expected |
| Press Enter with no Input | Loads Incorrect Value Output, prompts user to try again | As Expected |
| Insert desired username and press Enter | Welcome message and quiz-begin instructions appear | As Expected |
| Press Enter to start the quiz | Page Clear function executes and first quiz question appears | As Expected |
| Enter answer in digits 1-4 + Enter | Loads correct/incorrect Output and provides correct answer, loads next question | As Expected |
| Press Enter With No Input | Loads Incorrect Value Output, prompts user to enter digits 1-4 | As Expected |
|Random Selection of Quiz Questions until all 13 have been answered |Display Outputs Questions and correct answers | As Expected |
| Press Enter on Final Quiz guess | Displays correct Output depending on user guess, Loads Game Over message, Loads Final Score Output, Loads Try Again option | As Expected |
| User gets perfect score | A congratulations message appears along with the final 13/13 score | As Expected |
| Press Enter with no input | Loads Invalid Input message, prompts the user to enter 'y' or 'n'. | As Expected |
| Press Y on Try Again prompt |  Clears the page and runs quiz again, Starts the score back at 0, Runs through all 13 randomized questions again | As Expected |
| Press N on Try Again Prompt | Loads final message to player, system exit command executed | As Expected |

# _Validation_

 * This game passes through the [Code Institute PEP8](https://pep8ci.herokuapp.com/) Validator with no errors.

![Validation]()

# _Technologies_

 * Python is the programming language used to produce the game.
  
 * 'random' was imported to handle the mixing up of the quiz question order.
  
 * 'textwrap' was imported to handle breaking up of any lines longer than the CLI.
  
 * [GitHub](https://www.github.com) was used to hold the game repository files.

 * [Gitpod](https://www.gitpod.io) and [CodeAnywere](https://app.codeanywhere.com/) were used for the coding environment.

 * [Heroku](https://www.heroku.com) was used to deploy the game to the web.

# _Deployment_

## _1 - Version Control_

 Version control was maintained using git within GitPod and CodeAnywhere to push code to the main repository.

 * From the Gitpod terminal use "git add .", which tells git you would like to make changes/updates to the files.

 * Then use "git commit -m (plus a comment)", which commits the changes and updates the files.

 * Then use the "git push" command, which pushes the committed changes to the main repository. To go back and forth between Gitpod and CodeAnywhere workspaces, use the command "git pull" to make sure all data has been brought over before working from the new space.

## _2 - Page Deployment_

 Heroku CLI was used for this game's deployment. Directions on how to do that are as follows:

 * After creating an account and logging in, click "New" to create a new app from the dashboard.

 * Choose app's unique name and select your region; press "Create app".

 * Go to "Settings" and navigate to Config Vars.

 * Add Config Vars. 
    * This app used only one:
        * KEY = PORT : VALUE = 8000.
 
 * Add buildpacks Python and NodeJS - in this order.
 
 * Now you may click the Deploy tab.
 
 * Scroll Down to Deployment Method and select GitHub.
 
 * Select repository to be deployed and connect to Heroku.
 
 * Scroll down to deploy: 
    * Option 1 is selecting Automatic deploys (Will Update Automatically with every "git push"). This is what I chose for this project.
    * Option 2 is selecting Manual deploy (Needs to be manually redeployed after every change, via Heroku deploy tab).

 Visit the live deployment [HERE](https://plant-quiz.herokuapp.com/).

# _Credits_

 * I used a fellow student's "Riddles" code for this README.md format inspiration: [A. Croshaw](https://github.com/A-Croshaw/Riddles/blob/main/README.md)

 * Code for exiting the game or restarting was inspired by fellow student's portfolio project: [Haniibani](https://github.com/Haniibani/Project-portfolio-3/blob/main/run.py#L56)

 * Much of the run_game function was inspired by (and learned from) Code Institute's walkthrough project: [love_sandwiches](https://github.com/KrystalCoding/Love-Sandwiches)

 * For Python code functionality, I borrowed advice and bits of code from: [python.org](https://www.python.org/), [w3schools](https://www.w3schools.com/python/default.asp), and [stackoverflow](https://stackoverflow.com/)