from random import sample

print("Welcome to quiz app!")

while True:
    # Quiz App Backstage
    score=0
    totalquestion=10

    # Question and Answers
    question=["What is the capital of France?","Who wrote the play Hamlet?",
    "What is the currency of Japan?","Who was the first president of the United States?",
    "In what year was the Declaration of Independence signed?","What is the tallest mountain in the world?",
    "Who painted the Mona Lisa?","What is the largest ocean in the world?",
    "What is the capital of Australia?","Who invented the telephone?"]
    answers=["Paris","William Shakespeare",
    "Yen","George Washington",
    "1776","Mount Everest",
    "Leonardo Davinci","Pacific Ocean",
    "Canberra","Alexander Graham Bell"]
    listnumbers=list(range(totalquestion))
    no=sample(listnumbers,totalquestion)

    # Quiz App Front-End
    for i in no:
        answer=input(question[i])
        if answer.lower()==answers[i].lower():
            score+=1
        else:
            print("Wrong Answer!")
    print("Congratulation, you're score is:",score)
    repeat=input("Do you want to try again (y/n): ")
    if repeat=="n":
        break