import cmath

def roots(a, b, c):
    if a == 0:
        return "( )"

    discriminate = cmath.sqrt(b**2 - 4*a*c)
    r1 = (-b + discriminate) / (2*a)
    r2 = (-b - discriminate) / (2*a)

    if r1.imag == 0 and r2,imag == 0:
        r1 = r1.real
        r2 = r2,real
        if r1 == r2:
            return f"({r1})"
        else:
            return f"({r1}, {r2})"
    else:
         return "( )"
    


def value_y(a, b, c, x):
    return a * x**2 + b * x + c


def to_string(a, b, c):
    if a != 0 and b != 0 and c != 0:
        return f"f(x) = {a} * X^2 + {b} * x + {c}"
    elif a!=0 and b!=0 and  c==0:
        return f"f(x) = {a} * X^2 + {b} * X"
    elif a!=0 and b ==0 and c !=0:
        return f"f(x) = {a} * X^2 + {c}"
    elif a!=0 and b==0 and c==0:
        return f"f(x) = {a} * X^2"
    elif a==0 and b !=0 and c!=0:
        return f"f(x) = {b} * X + {c}"
    elif a == 0 and b!=0 and c ==0:
        return f"f(x) = {b} * X"
    elif a ==0 and b==0 and c!=0:
        return f"f(x) = {c}"
    else:
        return "f(x) = 0"
    


def derivation(a, b, c):
    if a != 0 and b !=0:
        return f"f´(x) = {2*a} * X + {b}"
    elif a!=0 and b == 0:
        return f"f´(x) = {2*a} * X"
    elif a== 0 and b!=0:
        return f"f´(x) = {b}"
    else:
        return "f´(x) = 0"
