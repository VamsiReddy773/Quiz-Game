import sqlite3

class Account:
    def __init__(self, accountno, name, gender, username, password):
        self.accountno = accountno
        self.name = name
        self.gender = gender
        self.username = username
        self.password = password

class Quiz:
    account_counter = 100
    
    def __init__(self):
        self.score = 0
        self.questions = []
        self.options = []
        self.correct_answers = []
        self.acc = None

    def account_generate(self):
        Quiz.account_counter += 1
        return Quiz.account_counter

    def account_create(self, conn):
        self.acc = Account(self.account_generate(), "", "", "", "")
        self.acc.name = input("Enter the name: ")
        self.acc.gender = input("Enter the Gender: ")
        self.acc.username = input("Enter Username: ")
        self.acc.password = input("Enter your Password: ")
        
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS accounts (
                accountno INTEGER PRIMARY KEY, 
                name TEXT, 
                gender TEXT, 
                username TEXT, 
                password TEXT
            )
        ''')
        cursor.execute('''
            INSERT INTO accounts (accountno, name, gender, username, password) 
            VALUES (?, ?, ?, ?, ?)
        ''', (self.acc.accountno, self.acc.name, self.acc.gender, self.acc.username, self.acc.password))
        conn.commit()
        print(f"Account created successfully! Your account number is: {self.acc.accountno}")
        print(f"Thanks for creating account, {self.acc.username}")

    def login(self, conn):
        entered_acc_no = int(input("Enter your Account Number: "))
        entered_password = input("Enter your Password: ")
        
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM accounts WHERE accountno = ? AND password = ?', (entered_acc_no, entered_password))
        account = cursor.fetchone()

        if account:
            self.acc = Account(*account)
            print(f"Login successful! Welcome to the Quiz, {self.acc.name}!")
            return True
        else:
            print("Invalid Account Number or Password!")
            return False

    def load_questions(self, filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    parts = line.strip().split('|')
                    question = parts[0]
                    options = parts[1:5]
                    correct_answer = int(parts[5])
                    self.questions.append(question)
                    self.options.append(options)
                    self.correct_answers.append(correct_answer)
        except Exception as e:
            print(f"Error loading questions: {e}")

    def start_quiz(self):
        if not self.questions:
            print("No questions available. Please check the questions file.")
            return

        self.score = 0
        for i in range(len(self.questions)):
            print(f"Question {i + 1}: {self.questions[i]}")
            for j, option in enumerate(self.options[i]):
                print(f"{j + 1}. {option}")

            user_answer = int(input("Your answer (1-4): "))
            if user_answer == self.correct_answers[i]:
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer is: {self.correct_answers[i]}. {self.options[i][self.correct_answers[i] - 1]}\n")

        print(f"Quiz Over! Your total score: {self.score}/{len(self.questions)}")


def main():
    conn = sqlite3.connect('quiz_game.db')
    quiz = Quiz()
    while True:
        print("\n1. Create Account\n2. Login and Start Quiz\n3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            quiz.account_create(conn)
        elif choice == 2:
            if quiz.login(conn):
                quiz.load_questions("questions.txt")
                quiz.start_quiz()
        elif choice == 3:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")
    
    conn.close()

if __name__ == "__main__":
    main()
