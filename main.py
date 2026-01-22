# If-elif-else statement
from pyscript import display, document


def julias_answer(e):
    document.getElementById('output').innerHTML = ' '

    response = document.getElementById('input1').value.lower()

    if response == 'Yes' :
        display(f'Keane will be her valentine', target='output')
    elif response == 'No':
        display(f' Keane will be heartbroken. Try again!', target='output')
    elif response == 'Maybe':
        display(f' Do not give up, try again!', target='output')
    else: 
        display(f'Invalid input', target='output')