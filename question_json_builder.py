import json

# Used for building questions.json 

sections = 'abcdefv'
exit = False
questions = {}

while not exit:
    first = input('Question on November list (-1 to exit): ')

    if first == '-1':
        break

    second = input('Question on September/October list (-1 if same, 0 if absent): ')

    print()
    match(second):
        case '-1':
            second = first
            pass
        case '0':
            second = 'N/A'
            pass
        case _:
            pass
    questions[first] = second


with open('questions.json', 'w') as fp:
    json.dump(questions, fp)