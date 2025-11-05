import sys
import string

# file name where questions are stored
QUIZ_FILE = "quiz_data.txt"

def load_questions(filename):
    # Reads questions by splitting the file content into blocks
    questions = []

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            question_blocks = content.strip().split('\n\n')

    except FileNotFoundError:
        print(f"Error: The quiz file '{filename}' was not found.")
        sys.exit(1)

    option_letters = string.ascii_lowercase

    # Process one question unit
    for block in question_blocks:
        lines = [line.strip() for line in block.split('\n') if line.strip()]
        # A valid unit must have at least 3 parts: Question, 1 Option, 1 Answer Letter
        if len(lines) < 3:
            if block.strip(): # Check if the block contains data
                print(f"Error: Incomplete data unit found. Expected at least 3 non-blank lines. Found: {block.strip()}")
                print("Program will terminate.")
                sys.exit(1)
            continue

        # Devide into the components
        question_text = lines[0]           # the question
        correct_answer = lines[-1].lower() # the answer letter
        final_options = lines[1:-1]        # the options

        num_options = len(final_options)

        # check if the answer letter exist in the options provided?
        if correct_answer not in option_letters[:num_options] or len(correct_answer) != 1:
            print("Critical Error: Invalid correct answer letter in the quiz file!")
            print(f"Question: {question_text}")
            print(f"Options found: {num_options}")
            print(f"Expected one of: {option_letters[:num_options]}. Got: '{correct_answer}'")
            print("The program will now terminate.")
            sys.exit(1)

        # making the dictionary
        questions.append({
            'question': question_text,
            'options': final_options,
            'correct_answer': correct_answer
        })

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

    print("\nQuiz Finished!")
    print(f"You got {score}/{total_questions} right.")



all_questions = load_questions(QUIZ_FILE)
run_quiz(all_questions)