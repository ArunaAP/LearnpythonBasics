from Question import Question
question_prompts = [
    "what color are apples?\n(a) Red/Green\n(b) purple\n(c) orange\n\n",
    "What color are bananas?\n(a) Teal\n(magenta)\n(c)Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) red\n(c) blue\n\n"
]
questions = [
    Question(question_prompts[0],"a"),
    Question(question_prompts[1],"c"),
    Question(question_prompts[2],"b"),
]


def run_test (questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1

    print("You got " + str(score)+ "/" + str(len(questions)) + " Correct")

run_test(questions  )
