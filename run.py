import random

# Define a list of questions and answers
questions = [
    {
        "question": "What is the scientific name for the common sunflower?",
        "answers": ["Helianthus annuus", "Rosa canina", "Cucurbita pepo", "Lilium auratum"],
        "correct_answer": "Helianthus annuus"
    },
    {
        "question": "What is the most widely cultivated fruit in the world?",
        "answers": ["Banana", "Apple", "Mango", "Orange"],
        "correct_answer": "Banana"
    },
    {
        "question": "What type of plant is poison ivy?",
        "answers": ["Vine", "Shrub", "Tree", "Grass"],
        "correct_answer": "Vine"
    },
    # Add more questions here...
]

# Define a function to run the game
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

# Run the game
run_game()
