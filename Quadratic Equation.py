print("=" * 70)
print("QUADRATIC EQUATION SOLVER By Dacely BertrandS".center(70))
print("Solves equations of the form: ax² + bx + c = 0".center(70))
print("=" * 70)

import math
def display_equation(a, b, c):
    """Display the formatted equation"""
    print("\n" + "-" * 70)
    print("THE EQUATION:")
    
    # Build equation string with proper signs
    equation = f"{a}x²"
    
    if b >= 0:
        equation += f" + {b}x"
    else:
        equation += f" - {abs(b)}x"
    
    if c >= 0:
        equation += f" + {c}"
    else:
        equation += f" - {abs(c)}"
    
    equation += " = 0"
    print(f"  {equation}")
    print("-" * 70)

def calculate_discriminant(a, b, c):
    """
    Calculate discriminant: Δ = b² - 4ac
    Returns: float
    """
    discriminant = b**2 - 4*a*c
    return discriminant


def solve_quadratic(a, b, c, discriminant):
    """
    Solve the quadratic equation using the quadratic formula
    Returns: list of solutions (can be real or complex)
    """
    solutions = []
    s = " "
    
    if discriminant >= 0:
        # Real solutions
        sqrt_discriminant = math.sqrt(discriminant)
        x1 = (-b + sqrt_discriminant) / (2 * a)
        x2 = (-b - sqrt_discriminant) / (2 * a)
        
        if discriminant == 0:
            solutions.append(x1)  # Only one solution (repeated root)
            s ='one repeated real solution'
        else:
            solutions.append(x1)
            solutions.append(x2)
            s = 'two distinct real solutions'
    else:
        # Complex solutions
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2 * a)
        
        # Store as tuples: (real_part, imaginary_part)
        solutions.append((real_part, imaginary_part))
        solutions.append((real_part, -imaginary_part))
        s = 'two complex conjugate solutions'
    
    return s, solutions

a = int(input("\n Enter the value of a: "))
b = int(input("\n Enter the value of b: "))
c = int(input("\n Enter the value of c: "))

display_equation(a, b, c)
discriminant = calculate_discriminant(a, b, c)
s, solutions = solve_quadratic(a, b, c, discriminant)

print(f"The discriminant Δ = {discriminant}")

print(f"While Δ = {discriminant} we will have {s} {solutions}")




