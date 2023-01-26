from single import SingleLinkedList

def eval(poly, x):

    result = 0
    for coeff in poly:
        result = x * result + coeff
    return result

def equation(list_coeff):
    temp = []
    for coeff, power in zip(list_coeff, range(len(list_coeff) - 1, -1, -1)):
        if coeff == 0:
            continue
        temp.append(coeff_format(coeff))
        temp.append(power_format(power))
    temp[0] = temp[0].lstrip("+")
    return ''.join(temp)

def coeff_format(coeff):
       return str(coeff) if coeff < 0 else "+{0}".format(coeff)


def power_format(power):
    if power ==0:
        return ''
    elif power == 1:
        return 'x'.format(power)
    else:
        return 'x^{0}'.format(power)

if __name__ == "__main__":

    command = input()
    try:
        if command == "set":
            sym = input()
            if sym not in ["A", "a", "B", "b", "C", "c", "R", "r"]:
                raise TypeError("")
            if sym == "A" or "a":
                Aa = input()
                A = SingleLinkedList()
                A.initialize(Aa)
            elif sym == "B" or "b":
                Bb = input()
                B = SingleLinkedList()
                B.initialize(Bb)
            elif sym == "C" or "c":
                Cc = input()
                C = SingleLinkedList()
                C.initialize(Cc)
            else:
                raise TypeError("")

        if command == "print":
            letter_print = input()
            if letter_print not in ["A", "a", "B", "b", "C", "c", "R", "r"]:
                raise TypeError("")
            if letter_print == "A" or "a":
                print(equation(A))
            if letter_print == "B" or "b":
                print(equation(B))
            if letter_print == "C" or "c":
                print(equation(C))
            if letter_print == "R" or "r":
                print(equation(R))

        if command == "eval":
            eval_letter = input()
            value = input()
            if eval_letter == "A" or "a":
                eval(A, value)
            if eval_letter == "B" or "b":
                eval(B, value)
            if eval_letter == "C" or "c":
                eval(C, value)

        else:
            print("Error")
    except TypeError:
        print("Error")




