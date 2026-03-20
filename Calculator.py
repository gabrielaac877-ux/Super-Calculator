def calculator():
    while True:
        try:
            num1 = input('Soy una calculadora, dame el primer numero paa la operación matematica')
            num1 = float(num1)

            symbol = input('Entra un operador (+, -, *, /): ')

        
            if symbol not in {'+', '-', '*', '/'}:
                raise ValueError('El operador debe de ser uno de estos: +, -, *, /.')

          
            num2 = input('Dame el segundo numero')
            num2 = float(num2)

            if symbol == '+':
                result = num1 + num2
            elif symbol == '-':
                result = num1 - num2
            elif symbol == '*':
                result = num1 * num2
            elif symbol == '/':
                if num2 == 0:
                    raise ZeroDivisionError('No se puede dividir entre 0.')
                result = num1 / num2

        except ValueError as s:
            print(f'Error, hiciste algo mal: {s}')
        except ZeroDivisionError as s:
            print(f'Error, hiciste algo mal: {s}')
        else:
            print(f'{num1} {symbol} {num2} = {result}')
            print('Todo fue un exito, soy una muy buena calculadora.')
        finally:
            print('Terminamos.')

        again = input('Otra vez?? (seleccione continuar, o q en minuscula para salir) ').lower()
        if again == 'q':
            print('Nos vemos, no me extrañes demasiado')
            break

calculator()
