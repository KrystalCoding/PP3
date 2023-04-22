import random

# The list of questions and answers in the quiz game
questions = [
    {
        "question": "What is the scientific name for the common sunflower?",
        "answers": ["Rosa rubiginosa", "Cucurbita pepo", "Helianthus annuus", "Lilium auratum"],
        "correct_answer": "Helianthus annuus"
    },
    {
        "question": "What is the most widely cultivated fruit in the world?",
        "answers": ["Apple", "Banana", "Mango", "Orange"],
        "correct_answer": "Banana"
    },
    {
        "question": "What type of plant is poison ivy?",
        "answers": ["Vine", "Shrub", "Tree", "Grass"],
        "correct_answer": "Vine"
    },
    {
        "question": "What is the process called by which plants convert light into energy?",
        "answers": ["Respiration", "Transpiration", "Fertilization", "Photosynthesis"],
        "correct_answer": "Photosynthesis"
    },
    {
        "question": "What is the largest flower in the world?",
        "answers": ["Titan arum", "Corpse flower", "Rafflesia arnoldii", "Hydrangea macrophylla"],
        "correct_answer": "Rafflesia arnoldii"
    },
    {
        "question": "What is the most common element found in all living organisms?",
        "answers": ["Oxygen", "Carbon", "Nitrogen", "Hydrogen"],
        "correct_answer": "Carbon"
    },
    {
        "question": "What is the name of the largest tree in the world?",
        "answers": ["Sequoia sempervirens", "Eucalyptus regnans", "Picea sitchensis", "Sequoiadendron giganteum"],
        "correct_answer": "Sequoiadendron giganteum"
    },
    {
        "question": "What is the process called by which plants lose water through their leaves?",
        "answers": ["Transpiration", "Photosynthesis", "Respiration", "Fertilization"],
        "correct_answer": "Transpiration"
    },
    {
        "question": "What is the national flower of Japan?",
        "answers": ["Lotus", "Rose", "Cherry blossom", "Tulip"],
        "correct_answer": "Cherry blossom"
    },
    {
        "question": "What is the name of the plant tissue that transports water and nutrients from the roots to the rest of the plant?",
        "answers": ["Phloem", "Xylem", "Cambium", "Epidermis"],
        "correct_answer": "Xylem"
    },
    {
        "question": "What is the name of the process by which plants bend or grow towards a light source?",
        "answers": ["Gravitropism", "Hydrotropism", "Thigmotropism", "Phototropism"],
        "correct_answer": "Phototropism"
    },
    {
        "question": "What is the name of the process by which plants shed their leaves?",
        "answers": ["Transpiration", "Abcission", "Photosynthesis", "Respiration"],
        "correct_answer": "Abcission"
    },
    {
        "question": "What is the name of the chemical compound responsible for giving plants their green color?",
        "answers": ["Chlorophyll", "Carotenoid", "Anthocyanin", "Chloroform"],
        "correct_answer": "Chlorophyll"
    }    
]


#Gets and saves user name
def player_info():
    print("Please enter your preferred username:\n")
    player_name = input()
    welcome(player_name)
    return player_name

# Welcome message
def welcome():
    print(f"Hello, {player_name}! Welcome to the Plant Quiz.\n")
    input("Press Enter to test your plant knowledge with 13 questions:")

# Defines the function to run the game
def run_game():
    random.shuffle(questions)  # Shuffle the questions
    score = 0  # Initialize the score
    for i, question in enumerate(questions):
        print(f"Question {i+1}: {question['question']}")
        for j, answer in enumerate(question['answers']):
            print(f"{j+1}. {answer}")
        player_answer = input("Enter your answer (1-4): ")
        if player_answer == str(question['answers'].index(question['correct_answer'])+1):
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {question['correct_answer']}.")
        print()  # Print a blank line for formatting
    print(f"Game over. Your score is {score}/{len(questions)}.")


#Get player name
player_name = player_info()

# Run the game
run_game()
