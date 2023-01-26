def print_poly(coeff, power):
    equation = ""
    for i in range (len(coeff)):
        if (power[i] == 1 & coeff[i+1]>0):
            equation += f"{coeff[i]}x+"
        elif (power[i] == 1 & coeff[i+1]<0):
            equation += f"{coeff[i]}x"
        elif (power[i] == 0):
            equation += f"{coeff[i]}"
        else:
            equation += f"{coeff[i]}x^{power[i]}+"

    print(equation)

print_poly([1,3,6],[2,1,0] )


def __str__(coeffs):
    chunks = []
    for coeff, power in zip(coeffs, range(len(coeffs) - 1, -1, -1)):
        if coeff == 0:
            continue
        chunks.append(format_coeff(coeff))
        chunks.append(format_power(power))
    chunks[0] = chunks[0].lstrip("+")
    return ''.join(chunks)

def format_coeff(coeff):
    return str(coeff) if coeff < 0 else "+{0}".format(coeff)

def format_power(power):
    return 'x^{0}'.format(power) if power != 0 else ''