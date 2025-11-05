import sys
import string
import os

# Define the file name where questions are stored
QUIZ_FILE = "quiz_data.txt"

def load_questions(filename):
    questions = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = [line.rstrip('\n') for line in file]
    except FileNotFoundError:
        print(f"Error: The quiz file '{filename}' was not found.")
        sys.exit(1)

    option_letters = string.ascii_lowercase

    # State machine based on line content:
    # 0 = Expecting Question (Start of a new unit)
    # 1 = Collecting all subsequent data lines (Options + Correct Letter)
    state = 0
    current_unit_lines = []

    for i, line in enumerate(lines):
        is_blank = not line.strip()

        if state == 0:
            # Expected: Question text (always the first non-blank line)
            if not is_blank:
                current_unit_lines.append(line)
                state = 1

        elif state == 1:
            # Collecting all subsequent data lines until a blank line is hit
            if not is_blank:
                current_unit_lines.append(line)
            else:
                # Blank line hit! This signals the end of the unit.

                # We expect at least the Answer Letter (1) and at least one Option (1)
                # Total lines (Question + Options + Answer Letter) must be >= 3
                if len(current_unit_lines) < 3:
                    print("---")
                    print(f"Error: Incomplete data unit ending on line {i+1}. Not enough options or answer letter found.")
                    print("Program will terminate.")
                    sys.exit(1)

                # --- Finalization and Validation for the completed unit ---

                # 1. Separate the components
                question_text = current_unit_lines[0]
                correct_answer = current_unit_lines[-1].strip().lower() # Last line is the answer letter
                final_options = current_unit_lines[1:-1] # All lines between Q and Answer are options

                # 2. Store the finalized dictionary
                current_unit = {
                    'question': question_text,
                    'options': final_options,
                    'correct_answer': correct_answer
                }

                # 3. Validation check
                num_options = len(final_options)

                if correct_answer not in option_letters[:num_options] or len(correct_answer) != 1:
                    print("---")
                    print("Critical Error: Invalid correct answer letter in the quiz file!")
                    print(f"Question: {current_unit['question']}")
                    print(f"Options found: {num_options}")
                    print(f"Expected one of: {option_letters[:num_options]}. Got: '{correct_answer}'")
                    print("The program will now terminate.")
                    sys.exit(1)

                # 4. Unit is validated, save it and reset for the next one
                questions.append(current_unit)
                current_unit_lines = []
                state = 0 # Look for the next question

    # Final check: Handle the last unit if the file did not end with a blank line
    if state == 1 and len(current_unit_lines) >= 3:
        print("---")
        print("Warning: Quiz file may be missing the final blank line separator. Processing the last unit.")

        try:
            question_text = current_unit_lines[0]
            correct_answer = current_unit_lines[-1].strip().lower()
            final_options = current_unit_lines[1:-1]
            num_options = len(final_options)

            if correct_answer not in option_letters[:num_options] or len(correct_answer) != 1:
                raise ValueError("Invalid final answer letter during finalization.")

            questions.append({
                'question': question_text,
                'options': final_options,
                'correct_answer': correct_answer
            })
        except (IndexError, ValueError):
            print("Error: Incomplete data in the final unit. Program will terminate.")
            sys.exit(1)

    elif state == 1 and len(current_unit_lines) < 3:
         print("---")
         print("Error: File ended unexpectedly with incomplete data. Program will terminate.")
         sys.exit(1)

    return questions


def run_quiz(questions):
    # displaying questions to the player and calculating the score.

    if not questions:
        print("No questions were loaded. Quiz cannot start.")
        return

    score = 0
    total_questions = len(questions)

    option_letters = string.ascii_lowercase

    print("\nStarting the Quiz!")

    for i, q_unit in enumerate(questions):
        question_number = i + 1
        print(f"\nQuestion {question_number} of {total_questions}:")
        print(q_unit['question'])

        options = q_unit['options']
        num_options = len(options)
        for j, option_text in enumerate(options):
            print(f"  {option_letters[j]}. {option_text}")

        correct_answer = q_unit['correct_answer']

        while True:
            player_answer = input("Your choice (enter the letter): ").strip().lower()

            if player_answer in option_letters[:num_options]:
                break
            else:
                print(f"Invalid option '{player_answer}'. Please choose a letter from the available options (a-{option_letters[num_options-1]}).")
                print(f"Question {question_number}: {q_unit['question']}")
                for j, option_text in enumerate(options):
                    print(f"  {option_letters[j]}. {option_text}")

        if player_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong. The correct answer was {correct_answer.upper()}.")

    print("\nQuiz Finished!)
    print(f"You got {score}/{total_questions} right.")


# 1. Load the data
all_questions = load_questions(QUIZ_FILE)

# 2. Run the quiz
run_quiz(all_questions)