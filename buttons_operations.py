unfiltered_number_list = []
final_input = []


def input_filter(inpt: str):
    print(inpt)
    operator_or_number = ""
    full_number = ""

    # Définit si le paramètre est un nombre ou un opérateur (pour le switch plus tard)
    if '0' <= inpt <= '9' or inpt == '.':
        operator_or_number = 'number'
    elif inpt == '+' or '-' or '*' or '/' or '^':
        operator_or_number = 'operator'
    if inpt == 'C':
        operator_or_number = 'C'
    if inpt == '=':
        operator_or_number = 'egalite'

    # print(operator_or_number)

    match operator_or_number:

        case 'number':
            unfiltered_number_list.append(inpt)

        case 'operator':
            for i in unfiltered_number_list:
                full_number += i
            unfiltered_number_list.clear()
            final_input.append(full_number)
            final_input.append(inpt)

        case 'C':
            final_input.clear()
            unfiltered_number_list.clear()
            print(final_input, 'sdsdsd')

        case 'egalite':
            for i in unfiltered_number_list:
                full_number += i
            unfiltered_number_list.clear()
            final_input.append(full_number)
            operation_solver(final_input)
            # final_input.clear()
            # final_input.append(full_number)

    return None


modified_equation = []


def operation_solver(equation: list):
    global modified_equation
    # print(modified_equation, 'is the global')
    modified_equation = equation
    # print(equation, 'is the local')
    # print(modified_equation)

    for i, element in enumerate(equation):

        if '^' in equation:
            if element == '^':
                print(float(equation[i-1]), 'is the i-1')
                print(float(equation[i+1]), 'is the i+1')
                result = pow(float(equation[i - 1]), float(equation[i + 1]))
                modified_equation.pop(i)
                modified_equation.pop(i)
                modified_equation[i - 1] = result
                operation_solver(modified_equation)

        # if element == '*' or element == '/':
        elif '*' in equation or '/' in equation:

            if element == '*':
                result = float(equation[i-1]) * float(equation[i+1])
                modified_equation.pop(i)
                modified_equation.pop(i)
                modified_equation[i-1] = result
                operation_solver(modified_equation)
            elif element == '/':
                result = float(equation[i-1]) / float(equation[i+1])
                modified_equation.pop(i)
                modified_equation.pop(i)
                modified_equation[i-1] = result
                operation_solver(modified_equation)

        elif element == '+' or element == '-':

            if element == '+':
                result = float(equation[i - 1]) + float(equation[i + 1])
                modified_equation.pop(i)
                modified_equation.pop(i)
                modified_equation[i - 1] = result
                operation_solver(modified_equation)
            else:
                result = float(equation[i - 1]) - float(equation[i + 1])
                modified_equation.pop(i)
                modified_equation.pop(i)
                modified_equation[i - 1] = result
                operation_solver(modified_equation)

    if not '+' or '-' or '*' or '/' or '^' in equation:
        return equation


def returning():
    return operation_solver(modified_equation)
