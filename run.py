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

available_questions = []


def select_level():
    """Prompt the user to select a difficulty level."""
    print("Select Difficulty Level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    while True:
        try:
            choice = input("Enter 1, 2, or 3 for the difficulty level:\n")
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
    global score, wrong_answers, available_questions, asked_questions
    difficulty = select_level() 
    available_questions = filter_questions_by_difficulty(difficulty)

    # Check if there are any questions
    if not available_questions:
        print("No questions available.")
        return
    clear()
    # counter for iteration of list
    counter = 0
    while counter <= len(available_questions):
        try:
            # Select a random question that hasn't been asked yet
            random_question = get_random_question(available_questions)
            if random_question is None:
                print(f"{Fore.RED}All questions have been asked.")
                break
            print(f"You will be asked {len(available_questions)} questions")
            print(f"Current Score is:{Fore.GREEN}{score}")
            print(f"level is:{Fore.GREEN}{difficulty.capitalize()}\n")
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


# Definition of get_random_question() method
def get_random_question(available_questions):
    """Retrieve a random question that hasn't been asked yet from the given list."""
    global asked_questions
    if len(asked_questions) == len(available_questions):
        return None  # No more questions left

    # Getting a random number from 0 to len(available_questions) - 1
    random_number = random.randrange(0, len(available_questions))
    while random_number in asked_questions:
        random_number = random.randrange(0, len(available_questions))
    # Marking the question as asked
    asked_questions.append(random_number)
    return available_questions[random_number]
    


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
    global score, wrong_answers
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


def reset_game():
    """Reset the necessary variables to start the game fresh."""
    global score, wrong_answers, asked_questions, available_questions
    score = 0
    wrong_answers = 0
    asked_questions = []
    available_questions = []


def displayScore():
    """
    Display the score and wrong answers
    """
    global score, wrong_answers
    if score >= 15:
        print(f"{Fore.GREEN}Your total score is {score}")
        print(f"{Fore.GREEN}Congratulations!")
        print(Fore.GREEN + "You have answered all questions right\n")
    elif score > 0:
        print(f"{Fore.GREEN}Your total score is {score}")
        print(f"{Fore.GREEN}Wrong answers are: {wrong_answers}")
        print(f"{Fore.GREEN}Better Luck Next Time\n")
    else:
        print(f"{Fore.GREEN}Oops!The cats won this round!")
        print(f"{Fore.GREEN}Try again and show them who's boss!")

    print(Fore.RED+"Game over\n")


def main():
    clear()
    """Main entry point of the program."""
    print("Welcome to Fun Flick - The Ultimate Quiz Game!")
    print("\nHow to Play Fun Flick:")
    print("1. You will first be prompted to select level")
    print("2. Then,a series of random questions from that level.")
    print("3. Each question will have four options: A, B, C, and D.")
    print("4. Type the letter corresponding to (A, B, C, or D).")
    print("5. For each correct answer, your score will increase by 1.")
    print("6. The game will continue until all questions are answered.")
    print("7. No question will be repeated during the game session.")
    print("\nNote: Make sure to only enter A, B, C, or D as your answer.")
    print("\nLet's begin by selecting a difficulty level!\n")

    input("Press Enter to Play Game\n")
    # Call playGame() method
    playGame()
    # Call DisplayScore method
    displayScore()
    while True:
        time.sleep(3)
        clear()
        print("Do you want to play again this game")
        play_again = input("Enter 'Y' to play game or 'N' to exit from game\n")
        play = play_again.upper()
        if play == "Y":
            reset_game()
            clear()
            input("Press Enter to Play Game\n")
            playGame()
            displayScore()
        elif play == "N":
            print(f"{Fore.YELLOW}Thank you for playing Fun Flick!")
            print("Goodbye!")
            break  # to exit from the loop
        else:
            print(f"{Fore.RED}{play_again} is Invalid input.")
            print(f"{Fore.RED}Please enter 'Y' to play again or 'N' to exit.")
            print("\n")


# Call main() method to start game
main()