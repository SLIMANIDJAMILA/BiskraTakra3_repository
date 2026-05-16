#!/usr/bin/env python3
"""Safe Calculator with Error Handling"""

def _safe_op(op_name, func, n1, n2):
    """Helper to run operations with consistent error handling."""
    try:
        return func(n1, n2)
    except ZeroDivisionError:
        print(f"❌ {op_name}: Cannot divide by zero.")
    except TypeError:
        print(f"❌ {op_name}: Inputs must be numbers.")
    except Exception as e:
        print(f"❌ {op_name}: Unexpected error - {e}")
    return None

def addition(n1, n2): return n1 + n2
def multiplication(n1, n2): return n1 * n2
def minus(n1, n2): return n1 - n2
def division(n1, n2): return n1 / n2
def division_rest(n1, n2): return n1 % n2
def division_con(n1, n2): return n1 // n2

if __name__ == '__main__':
    try:
        Number_1 = float(input("Number_1 : "))
        Number_2 = float(input("Number_2 : "))

        print(f"\n{'='*40}")
        print(f"✅ Results for {Number_1} and {Number_2}:")
        print(f"{'='*40}")
        print(f"addition:       {_safe_op('Addition', addition, Number_1, Number_2)}")
        print(f"multiplication: {_safe_op('Multiplication', multiplication, Number_1, Number_2)}")
        print(f"minus:          {_safe_op('Subtraction', minus, Number_1, Number_2)}")
        print(f"div:            {_safe_op('Division', division, Number_1, Number_2)}")
        print(f"division_rest:  {_safe_op('Modulo', division_rest, Number_1, Number_2)}")
        print(f"division_con:   {_safe_op('Integer Division', division_con, Number_1, Number_2)}")
        print(f"{'='*40}")

    except ValueError:
        print("❌ Error: Please enter valid numbers (e.g., 5, 3.14, -2).")
    except KeyboardInterrupt:
        print("\n👋 Cancelled.")

"""
def addition(n1, n2):
    add = n1 + n2
    return add


def multiplication(n1, n2):
    multi = n1 * n2
    return multi


def minus(n1, n2):
    minu = n1 - n2
    return minu

def division(n1, n2):
    div = n1 / n2
    return div

def division_rest(n1, n2):
    div_rest = n1 % n2
    return div_rest

def division_con(n1, n2):
    div = n1 // n2
    return div
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Number_1 = float(input("Number_1 : "))
    Number_2 = float(input("Number_2 : "))
    print(f"addition {addition(Number_1, Number_2)}")
    print(f"multiplication {multiplication(Number_1, Number_2)}")
    print(f"minus {minus(Number_1, Number_2)}")
    print(f"div {division(Number_1, Number_2)}")
    print(f"division_rest {division_rest(Number_1, Number_2)}")
    print(f"division_con {division_con(Number_1, Number_2)}")
"""
