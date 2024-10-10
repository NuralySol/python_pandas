
#! needs the import for pip project
import json
import html
import time
import random
import requests
import pandas as pd
import os  

#! API calls and trivia game using the above modules in Data Science environment Python
#! Fetch trivia questions from an API in JSON format
def fetch_trivia_questions():
    url = "https://opentdb.com/api.php?amount=5&category=9&difficulty=medium&type=multiple"
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.text)["results"]
    else:
        print("Failed to retrieve questions. Please check your internet connection.")
        return []

# Display question and choices (pipenv output shell)
def display_question(question_data):
    question = html.unescape(question_data['question'])
    correct_answer = html.unescape(question_data['correct_answer'])
    incorrect_answers = [html.unescape(ans) for ans in question_data['incorrect_answers']]
    
    #! Combine correct and incorrect answers
    choices = incorrect_answers + [correct_answer]
    random.shuffle(choices)

    print("\nQuestion:")
    print(question)
    
    # Show options for the player in the output
    for idx, choice in enumerate(choices, 1):
        print(f"{idx}. {choice}")
    
    return question, correct_answer, choices

# Function to check the answer against the API 
def check_answer(correct_answer, user_answer, choices):
    if choices[user_answer - 1] == correct_answer:
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
    # enumirate is a global function and ValueError is a meta-class of python (built in)
    for idx, question_data in enumerate(questions):
        question, correct_answer, choices = display_question(question_data)
        try:
            user_answer = int(input("Your answer (1-4): "))
            if user_answer < 1 or user_answer > 4:
                print("Invalid choice. Please enter a number between 1 and 4.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        is_correct = check_answer(correct_answer, user_answer, choices)
        if is_correct:
            score += 1
        
        # Store question, user's answer, and correctness
        game_data.append({
            "Question": question,
            "Correct Answer": correct_answer,
            "Your Answer": choices[user_answer - 1],
            "Correct?": "Yes" if is_correct else "No"
        })
        
        time.sleep(1)  # Pause for 1 second between questions
    
    print(f"\nGame Over! Your final score is {score}/{len(questions)}.")

    # Save results using pandas
    results_data = {
        "Timestamp": [time.strftime("%Y-%m-%d %H:%M:%S")],
        "Score": [score],
        "Total Questions": [len(questions)]
    }
    
    df_results = pd.DataFrame(results_data)
    df_results.to_csv("trivia_results.csv", mode='a', index=False, header=False)
    print("Your score has been saved!")

    # Save detailed question and answer data in CSV for user 
    df_game_data = pd.DataFrame(game_data)
    df_game_data.to_csv("trivia_detailed_results.csv", mode='a', index=False)
    print("Detailed results have been saved to trivia_detailed_results.csv!")

    # Save game data to a JSON fixture (dict. style) can be saved to DB (MangoDB?)
    save_to_json_fixture(game_data)

# Function to save game data to a JSON fixture file
def save_to_json_fixture(game_data):
    fixture_path = "./fixtures/trivia_fixture.json" # path to the fixture dir/trivia_fixture.json
    
    # Check if the file exists and is not empty
    if os.path.exists(fixture_path) and os.path.getsize(fixture_path) > 0:
        try:
            with open(fixture_path, "r") as file:
                existing_data = json.load(file)
        except json.JSONDecodeError:
            print("Warning: trivia_fixture.json is empty or invalid. Initializing as an empty list.")
            existing_data = []
    else:
        existing_data = []
    
    # Append the new game data
    existing_data.append({
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "game_data": game_data
    })

    # Write the updated data to the fixture file
    with open(fixture_path, "w") as file:
        json.dump(existing_data, file, indent=4)
    
    print(f"Game data has been saved to {fixture_path}")

#! play the game call function
if __name__ == "__main__":
    play_trivia_game()