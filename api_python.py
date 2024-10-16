# import the needed modules for the game (Trivia Game API)
import json
import html
import time
import random
import requests
import pandas as pd
import os  # this is a path module in order to create csv files or JSON fixtures. 


#! API calls and trivia game using the above modules in Data Science environment Python
#! Fetch trivia questions from an API in JSON format
# Ask the user for the number of questions intify it
num_questions = int(
    input("Please enter the number of questions you want to play (1-10): ")
)

# Ensure the number of questions is between 1 and 10
if num_questions > 10:
    num_questions = 10
elif num_questions < 1:
    num_questions = 1

# Ask the user for the difficulty of the trivia game
trivia_difficulty = input(
    "Please enter the difficulty of the game (easy, medium, or hard): "
).lower()

#! while loop is good valid input using not in and also .lower() method for API call
while trivia_difficulty not in ["easy", "medium", "hard"]:
    print("Invalid difficulty level. Please choose 'easy', 'medium', or 'hard'.")
    trivia_difficulty = input(
        "Please enter the difficulty of the game (easy, medium, or hard): "
    ).lower()

# Output confirmation to play the game
print(
    f"\nYou will play {num_questions} question(s) at {trivia_difficulty} difficulty level."
)


#! (9) is a general category in the API call string, use the f-string for dynamic game for num_questions and trivia difficulty
def fetch_trivia_questions():
    url = f"https://opentdb.com/api.php?amount={num_questions}&category=9&difficulty={trivia_difficulty}&type=multiple"
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.text)["results"]
    else:
        print(
            "Failed to retrieve questions. Please check your internet connection."
        )  #! 500 error or 404
        return []


# Function to display question and choices with A, B, C, D format using enumerate, also need html. module for entities
def display_question(question_data):
    question = html.unescape(question_data["question"])
    correct_answer = html.unescape(question_data["correct_answer"])
    incorrect_answers = [
        html.unescape(ans) for ans in question_data["incorrect_answers"]
    ]

    # Combine correct and incorrect answers, shuffle them so that the user does not gues with last append!
    choices = incorrect_answers + [correct_answer]
    random.shuffle(choices)

    print("\nQuestion:")
    print(question)

    # Assign letters A, B, C, D to the choices using enumerate and for loop
    choice_letters = ["A", "B", "C", "D"]

    # Map of letter to choice
    choice_mapping = {}

    for idx, choice in enumerate(choices):
        print(f"{choice_letters[idx]}. {choice}")
        choice_mapping[choice_letters[idx]] = choice

    return (
        question,
        correct_answer,
        choice_mapping,
    )  # return the variables to be called upon later.


# Function to check the answer against the API payload!
def check_answer(correct_answer, user_answer, choice_mapping):
    if choice_mapping[user_answer.upper()] == correct_answer:
        print("Correct!")
        return True
    else:
        print(f"Incorrect! The correct answer was {correct_answer}")
        return False


# Main function to play the game
def play_trivia_game():
    print("Welcome to the Trivia Game!")

    questions = fetch_trivia_questions()
    score = 0
    game_data = []
    
    # for loop with with try and except validator with: -> list user_answer not in ["A", "B", "C", "D"]: 
    for idx, question_data in enumerate(questions):
        question, correct_answer, choice_mapping = display_question(question_data)
        try:
            user_answer = input("Your answer (A, B, C, D): ").upper()
            if user_answer not in ["A", "B", "C", "D"]:
                print("Invalid choice. Please enter A, B, C, or D.")
                continue
        except ValueError:
            print("Invalid input. Please enter a letter.")
            continue

        is_correct = check_answer(correct_answer, user_answer, choice_mapping)
        if is_correct:
            score += 1  # increament the score unlike JS language i++ it is different in Python!

        # Store question, user's answer, and correctness game_data main variable of storing data! dictionary type
        game_data.append(
            {
                "Question": question,
                "Correct Answer": correct_answer,
                "Your Answer": choice_mapping[user_answer],
                "Correct?": "Yes" if is_correct else "No",
            }
        )

        time.sleep(1)  #! sleep for 1 sec to give time for user part of the time imported module!

    print(f"\nGame Over! Your final score is {score}/{len(questions)}.")

    # Save results using pandas also a dictionary. 
    results_data = {
        "Timestamp": [time.strftime("%Y-%m-%d %H:%M:%S")],
        "Score": [score],
        "Total Questions": [len(questions)],
    }
    # csv using rows and columns part of the DataFrame class
    df_results = pd.DataFrame(results_data)
    df_results.to_csv("trivia_results.csv", mode="a", index=False, header=False)
    print("Your score has been saved!") # print for user result!

    # Save detailed question and answer data in CSV for user
    df_game_data = pd.DataFrame(game_data)
    df_game_data.to_csv("trivia_detailed_results.csv", mode="a", index=False)
    print("Detailed results have been saved to trivia_detailed_results.csv!")

    # Save game data to a JSON fixture (dict. style) can be saved to DB (MangoDB?)
    save_to_json_fixture(game_data)


# Function to save game data to a JSON fixture file
def save_to_json_fixture(game_data):
    fixture_path = (
        "./fixtures/trivia_fixture.json"  # path to the fixture dir/trivia_fixture.json
    )

    # Check if the file exists and is not empty
    if os.path.exists(fixture_path) and os.path.getsize(fixture_path) > 0:
        try:
            with open(fixture_path, "r") as file:
                existing_data = json.load(file)
        except json.JSONDecodeError:
            print(
                "Warning: trivia_fixture.json is empty or invalid. Initializing as an empty list."
            )
            existing_data = []
    else:
        existing_data = []

    # Append the new game data
    existing_data.append(
        {"timestamp": time.strftime("%Y-%m-%d %H:%M:%S"), "game_data": game_data}
    )

    # Write the updated data to the fixture file
    with open(fixture_path, "w") as file:
        json.dump(existing_data, file, indent=4)

    print(f"Game data has been saved to {fixture_path}")


# Play the game if __name__ == "__main__": call the script directly
if __name__ == "__main__":
    play_trivia_game()
