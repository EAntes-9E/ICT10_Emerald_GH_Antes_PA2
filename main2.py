# if-elif-else statement
from pyscript import display, document


def students_classifications(e):
    document.getElementById('result').innerHTML = ' '

    classification = float(document.getElementById('number1').value)

    if classification >= 95:
        display(f'Bergamo 1', target='result')

    elif classification >= 91:
        display(f'Bergamo 2', target='result')

    elif classification >= 86:
        display(f'Bergamo 3', target='result')

    elif classification >= 75:
        display(f'Perugia 1', target='result')

    elif classification >= 65:
        display(f'Perugia 2', target='result')

    else: 
        display(f'You are terrible!', target='result')