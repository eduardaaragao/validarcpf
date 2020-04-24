# Algorithm to validate a given CPF
# Author: Maria A. de M.


# The size must be 11
def validate_size(cpf):
    return len(cpf) == 11


# Remove characters such as . and -
def remove_characters(cpf):
    for i in cpf:
        if i == '.' or i == '-':
            cpf = cpf.replace(i, '')
    return cpf


# Validate the first element after the "-"
def validate_first(cpf):
    cont = 11
    sum = 0
    for i in cpf[0:9]:
        i = int(i)
        cont -= 1
        sum += i * cont
    return sum * 10 % 11


# Validate the second element after the "-"
def validate_second(cpf):
    cont = 12
    sum = 0
    for i in cpf[0:10]:
        i = int(i)
        cont -= 1
        sum += i * cont

    return sum * 10 % 11


# Check if all the elements are repeated
def repeated_elements(cpf):
    counter = cpf.count(cpf[0])

    return counter == 11


# Begin
running = True

while running:
    CPF = (input('Type in the CPF: ')).strip()
    CPF = remove_characters(CPF)

    validate_size(CPF)

    first = str(validate_first(CPF))
    second = str(validate_second(CPF))

    # Verifying if the first and second element after "-" is equal to the rest of the division

    if first == CPF[9] and second == CPF[10] and validate_size(CPF) and not repeated_elements(CPF):
        print("Valid!")
        running = False
    else:
        print("Invalid!")
