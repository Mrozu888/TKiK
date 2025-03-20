def scanner(expression):
    tokens = []
    i = 0
    length = len(expression)

    while i < length:
        char = expression[i]

        if char.isspace():
            i += 1
            continue

        elif char.isdigit():
            num = 0
            while i < length and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            tokens.append(("NUMBER", num))
            continue

        elif char.isalpha() or char == '_':
            ident = ''
            while i < length and (expression[i].isalnum() or expression[i] == '_'):
                ident += expression[i]
                i += 1
            tokens.append(("ID", ident))
            continue

        elif char in '+-*/':
            tokens.append(("OP", char))

        elif char == '(':
            tokens.append(("LPAREN", char))

        elif char == ')':
            tokens.append(("RPAREN", char))

        else:
            print(f"Błąd: nierozpoznany znak '{char}' na pozycji {i}")

        i += 1

    return tokens


# test
expr = "2 + 3*(76+8/3) + 3*(9-3)"
tokens = scanner(expr)
print(tokens)
