import random

def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2 if num2 != 0 else "Error: Division by zero"

def generate_problem():
    operators = ['+', '-', '*', '/']
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 10) if random.choice(operators) != '/' else random.randint(1, 5)
    operator = random.choice(operators)
    if operator == '/' and num1 % num2 != 0:
        num1 = num2 * random.randint(1, 5)  # Ensure clean division
    return num1, num2, operator

def main():
    score = 0
    total_questions = 5
    
    print("Welcome to Calculator Game!")
    print(f"Solve {total_questions} math problems to test your skills!\n")
    
    for i in range(total_questions):
        num1, num2, operator = generate_problem()
        correct_answer = calculate(num1, num2, operator)
        
        print(f"Question {i+1}: {num1} {operator} {num2} = ?")
        
        try:
            user_answer = float(input("Your answer: "))
            if abs(user_answer - correct_answer) < 0.01:  # Handle floating point precision
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is {correct_answer}")
        except ValueError:
            print(f"Invalid input! The correct answer is {correct_answer}")
        print()
    
    print(f"Final Score: {score}/{total_questions}")
    
    if score == total_questions:
        print("Perfect! You're a math wizard!")
    elif score >= total_questions * 0.7:
        print("Great job! Keep practicing!")
    else:
        print("Keep studying! Practice makes perfect!")

if __name__ == "__main__":

    main()
