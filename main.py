from pyscript import display, document

def Click(e):
    name = document.getElementById('name').value
    age = document.getElementById('age').value
    school = document.getElementById('school').value

    tell = f'''
    Student information:
    Name   : {name}
    Age    : {age}
    School : {school}

    ✏️ Notes:
    {name}\' is currently {age} years old and studies at\t{school}.
    '''

    display(tell, target="output")