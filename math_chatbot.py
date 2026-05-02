import math

print("="*40)
print(" 🤖 MATH AI CHATBOT ")
print("="*40)
print("Type 'exit' to quit\n")

while True:
    user = input("You: ").lower()

    # Exit
    if user == "exit":
        print("Bot: Goodbye! Keep practicing maths!")
        break

    # Algebra
    elif "quadratic formula" in user:
        print("Bot: x = (-b ± √(b² - 4ac)) / 2a")

    elif "square formula" in user:
        print("Bot: (a + b)² = a² + 2ab + b²")

    # Trigonometry
    elif "sin" in user:
        print("Bot: sin(x) = opposite / hypotenuse")

    elif "cos" in user:
        print("Bot: cos(x) = adjacent / hypotenuse")

    elif "tan" in user:
        print("Bot: tan(x) = opposite / adjacent")

    # Differentiation
    elif "derivative of x square" in user:
        print("Bot: d/dx (x²) = 2x")

    elif "derivative of sin x" in user:
        print("Bot: d/dx (sin x) = cos x")

    # Integration
    elif "integration of x" in user:
        print("Bot: ∫x dx = x²/2 + C")

    elif "integration of sin x" in user:
        print("Bot: ∫sin(x) dx = -cos(x) + C")

    # Simple calculator
    elif "+" in user:
        try:
            print("Bot:", eval(user))
        except:
            print("Bot: Invalid expression")

    elif "-" in user:
        try:
            print("Bot:", eval(user))
        except:
            print("Bot: Invalid expression")

    else:
        print("Bot: I can help with formulas, trig, derivatives, or simple calculations.")