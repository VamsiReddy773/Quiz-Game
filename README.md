# Quiz-Game
This project implements a simple Python quiz application with user accounts.
This is a Python-based interactive Quiz Game with user account creation, login functionality, and dynamic quiz management. The project allows users to create accounts, login securely, and take a quiz based on questions stored in a text file. The game keeps track of the user’s score after each quiz session.

# Features:

User Account Management: Users can create an account with their name, username, gender, and password. The account details are stored securely in an SQLite database.

# Secure Login: 
Users can log in using their account number and password. Login credentials are validated against stored data in the database.

# Dynamic Quiz: 
The quiz questions are loaded from an external file (questions.txt), allowing easy modification of the quiz content. Each question comes with multiple-choice options, and the correct answer is tracked for scoring.

# Scoring System: 
Users' performance is evaluated based on the number of correct answers, and their final score is displayed at the end of the quiz.

# Technologies Used:
Python 3.x
SQLite Database for storing user accounts and quiz data
Text File for storing quiz questions and options

# How to Run:
Clone this repository.
Ensure you have Python 3.x installed.
Install the required libraries (if any) using:
pip install sqlite3
Create a questions.txt file with quiz data in the following format:
Question?|Option 1|Option 2|Option 3|Option 4|Correct Option Number
# Run the Quiz Game.py script:
python Quiz\ Game.py
Example questions.txt format:

What is 2 + 2?|1. 3|2. 4|3. 5|4. 6|2
What is the capital of France?|1. Berlin|2. Madrid|3. Paris|4. Rome|3
