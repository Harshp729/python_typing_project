import time
import random
import curses

# List of random sentences to type
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python programming is fun and challenging.",
    "Data science is a fascinating field to explore.",
    "Machine learning and artificial intelligence are transforming industries.",
    "Typing speed and accuracy can be improved with practice."
]

# Function to get random sentence
def get_random_sentence():
    return random.choice(sentences)

# Function to display instructions and handle typing speed check
def typing_test(stdscr):
    # Clear the screen
    stdscr.clear()

    # Get a random sentence
    sentence = get_random_sentence()

    # Display the sentence to be typed
    stdscr.addstr(0, 0, "Type the following sentence as fast as you can:")
    stdscr.addstr(1, 0, sentence)
    stdscr.addstr(3, 0, "Press any key to start...")

    # Wait for the user to press a key to start
    stdscr.refresh()
    stdscr.getkey()

    # Clear the screen for typing
    stdscr.clear()
    stdscr.addstr(0, 0, "Start typing the sentence:")

    # Start timing
    start_time = time.time()

    typed_sentence = ""
    row, col = 1, 0

    while typed_sentence != sentence:
        stdscr.clear()
        stdscr.addstr(0, 0, "Start typing the sentence:")
        stdscr.addstr(1, 0, sentence)

        # Check each typed word
        for i, word in enumerate(typed_sentence.split()):
            if word != sentence.split()[i]:
                stdscr.addstr(2, 0, sentence, curses.color_pair(1))  # Highlight wrong words in red

        # Show the typed sentence so far
        stdscr.addstr(2, 0, typed_sentence)
        stdscr.refresh()

        key = stdscr.getkey()
        if key == '\n':  # Enter key
            break
        elif key == '\b':  # Backspace key
            typed_sentence = typed_sentence[:-1]
        else:
            typed_sentence += key

    # Calculate typing speed and accuracy
    end_time = time.time()
    typing_duration = end_time - start_time
    word_count = len(sentence.split())
    typed_word_count = len(typed_sentence.split())
    correct_words = sum([1 for i in range(min(len(sentence.split()), len(typed_sentence.split()))) if sentence.split()[i] == typed_sentence.split()[i]])

    accuracy = (correct_words / word_count) * 100
    words_per_minute = (typed_word_count / typing_duration) * 60

    # Display results
    stdscr.clear()
    stdscr.addstr(0, 0, f"Typing Speed: {words_per_minute:.2f} WPM")
    stdscr.addstr(1, 0, f"Accuracy: {accuracy:.2f}%")
    stdscr.refresh()

    stdscr.getkey()

# Initialize curses and run the program
curses.wrapper(typing_test)

