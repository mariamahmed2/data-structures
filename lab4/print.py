class Polynomial:
    def __init__(self, coefficients):
        self.coeffs = coefficients

    def __str__(self):
        chunks = []
        for coeff, power in zip(self.coeffs, range(len(self.coeffs) - 1, -1, -1)):
            if coeff == 0:
                continue
            chunks.append(self.format_coeff(coeff))
            chunks.append(self.format_power(power))
        chunks[0] = chunks[0].lstrip("+")
        return ''.join(chunks)

    @staticmethod
    def format_coeff(coeff):
        return str(coeff) if coeff < 0 else "+{0}".format(coeff)

    @staticmethod
    def format_power(power):
        if power ==0:
            return ''
        elif power == 1:
            return 'x'.format(power)
        else:
            return 'x^{0}'.format(power)
def return_var(input):
    if input == "A" or "a":
        return A
if __name__ == "__main__":
   global A
   A=1

intt = return_var(input())
print(intt)



