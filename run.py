# Impoting random module, colorama, os and time
import random
from questions import questions
import time
import os
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

# To validate answer from answers_list
answers_list = ["A", "B", "C", "D"]

# Global vars of score and wrong_answers
score = 0

wrong_answers = 0

# List to check the matched question
asked_questions = []

available_questions=[]

def select_level():
    """Prompt the user to select a difficulty level."""
    print("Select Difficulty Level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    
    while True:
        try:
            choice = input("Enter 1, 2, or 3 for the desired difficulty level: ")
            if choice == "1":
                return "easy"
            elif choice == "2":
                return "medium"
            elif choice == "3":
                return "hard"
            else:
                raise ValueError("Invalid input, please enter 1, 2, or 3.")
        except ValueError as e:
            print(f"{Fore.RED}{e}")


def filter_questions_by_difficulty(difficulty_level):
    """Filter questions based on the selected difficulty."""
    return [q for q in questions if q["difficulty"] == difficulty_level]


def clear():
    """ Clear function to clean-up the terminal. """
    os.system("cls" if os.name == "nt" else "clear")


# Definition of playGame() method
def playGame():
    """
    Starts and manages the quiz game session for Fun Flick.
    This function randomly selects a question from the predefined
    list of questions and presents it to the user. The user is asked
    to input their answer by choosing between four options:  A, B, C, or D.
    The function validates the user's input to ensure it's one of the valid
    options and checks if it matches the correct answer. The player's score
    is updated based on their answers. No question will be repeated during
    a single game session, and the game ends when all questions have been
    answered.
    """
    print("Game begins!\n")
    # Calling clear method to clear screen
    clear()
    global score
    global wrong_answers
    difficulty = select_level()
    available_questions = filter_questions_by_difficulty(difficulty)

    # Check if there are any questions
    if not available_questions:
        print("No questions available.")
        return
    
    print(available_questions)
    # counter for iteration of list
    counter = 0
    while counter < len(available_questions):
        try:
            # Select a random question that hasn't been asked yet
            random_question = get_random_question(available_questions)
            if random_question is None:   # If all questions are asked
                print("All questions have been asked. Game over!")
                break
            print(f"Your Current Score is: {score} ")
            print(f"Question #{counter+1}: {random_question["question"]}")
            # to loop through dictionary in questions for options
            for option in random_question["options"]:
                print(option)
            print("")

            user_input = get_validated_input()
            validate_input(user_input, random_question)
            counter += 1

        except (IndexError, KeyError) as e:
            print(f"Error occurred while selecting question: {e}")
            break  # Or continue to the next iteration if it's recoverable
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break
    # Call DisplayScore method
    displayScore()


# Definition of get_random_question() method
def get_random_question(available_questions):
    """Retrieve a random question that hasn't been asked
        yet from given list"""

    if asked_questions is None:
        return None  # All questions have been asked

    # Getting random number from 0-49
    random_number = random.randrange(0, len(available_questions))
    while random_number in asked_questions:
        random_number = random.randrange(0, len(available_questions))
    # Marking the question as asked
    asked_questions.append(random_number)
    # Get the elements of questions list
    random_question = available_questions[random_number]
    return random_question


# Definition of get_validated_input() method
def get_validated_input():

    """Prompt the user for a valid input and keep
    asking until a valid answer is entered."""

    while True:
        try:
            user_input = input("Enter A/B/C/D to choose your answer\n")
            user = user_input.upper()
            if user in answers_list:
                return user
            else:
                raise ValueError(f"{user_input} is Invalid input.")
        except ValueError as e:
            print(f"{Fore.RED}Error:{e}.")
            print(Fore.RED + "Please enter a valid option A/B/C/D.")


# Definition validate_input(user,random_question) method
def validate_input(user, random_question):

    """Check if the user's input matches the correct
    answer and update the score."""
    global score
    global wrong_answers
    try:
        # Check if the user's input matches the correct answer
        if user == random_question["answers"]:
            score += 1
            print(Fore.GREEN+"Your Answer is correct!")
            print(Fore.GREEN+f"Your Score is:  {score}\n")
        else:
            wrong_answers += 1
            print(Fore.RED+"Wrong Answer")
            print(f"{Fore.RED}The correct answer:{random_question["answers"]}")
            print("\n")
    except Exception as e:
        print(f"An error occurred while validating input: {e}")
    time.sleep(1)
    clear()
# Definition of reset_game()


def reset_game():
    """Reset the necessary variables to start the game fresh."""
    global score, wrong_answers, asked_questions, available_questions
    score = 0
    wrong_answers = 0
    asked_questions = []
    available_questions=[]
    


def displayScore():
    """
    Display the score and wrong answers
    """
    global score, wrong_answers
    if score == 50:
        print(f"{Fore.BLUE}{Back.WHITE}Your total score is {score}")
        print(f"{Fore.BLUE}{Back.WHITE}Congratulations!")
        print(Fore.BLUE + "You have answered all questions right\n")
    elif score > 0 or score < 50:
        print(f"{Fore.BLUE}{Back.WHITE}Your total score is {score}")
        print(f"{Fore.BLUE}{Back.WHITE}Wrong answers are: {wrong_answers}\n")
    else:
        print(f"{Fore.BLUE}{Back.WHITE}Oops!The cats won this round!")
        print(f"{Fore.BLUE}{Back.WHITE}Try again and show them who's boss!")

    print(Fore.RED+"Game over\n")


# Definition of main() method
def main():
    """Main entry point of the program."""
    print("Welcome to Fun Flick - The Ultimate Quiz Game!")
    print("\nHow to Play Fun Flick: ")
    print("1. You will be asked a series of random questions.")
    print("2. Each question will have four options:  A, B, C, and D.")
    print("3. Type letter corresponding to the correct answer A, B, C, or D.")
    print("4. If you choose the right answer, your score will increase by 1.")
    print("5. The game will continue until all questions are answered")
    print("6. No questions will be repeated during the game.")
    print("\nNote:  Make sure to only enter A, B, C, or D as your answer.")
    print("\nLet's begin!\n")

    input("Press Enter to Play Game\n")
    # Call playGame() method
    playGame()
    while True:
        print("Do you want to play again this game")
        play_again = input("Enter 'Y' to play game or 'N' to exit from game\n")
        play = play_again.upper()
        if play == "Y":
            reset_game()
            clear()
            input("Press Enter to Play Game\n")
            playGame()
        elif play == "N":
            print(f"{Fore.BLUE}{Back.WHITE}Thank you for playing Fun Flick!")
            print("Goodbye!")
            break  # to exit from the loop
        else:
            print(f"{Fore.RED}{play_again} is Invalid input.")
            print(f"{Fore.RED}Please enter 'Y' to play again or 'N' to exit.")
            print("\n")


# Call main() method to start game
main()
