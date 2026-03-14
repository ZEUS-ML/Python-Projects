questions = ("What is the capital of India?",
            "Which planet is known as the Red Planet?",
            "How many days are there in a week?",
            "Who is known as the Father of the Nation in India?",
            "What gas do plants take in during photosynthesis?")


answers = ("A.Kolkata B.New Delhi C.Mumbai D.Lucknow",
            "A.Earth B.Venus C.Jupiter D.Mars",
            "A.5 B.3 C.7 D.2",
            "A.S V Patel B.M K Gandhi C.Jawaharlal Nehru D.S C Bose",
            "A.CO2 B.N2 C.O2 D.CH4")

correct = ("B","D","C","B","A")
i=0
total = 0
for i,question in enumerate(questions):
    print(question)
    print(answers[i])
    guess = input("Enter your guess (A B C D): ").upper()
    if guess == correct[i]:
        total = total + 1
        print("Correct Answer!")
        
    else:
        print(f"Wrong Answer! \nThe Correct Answer is {correct[i]}")

print("YOUR SCORE IS :",int(total/len(questions)*100),"%")