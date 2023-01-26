
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

