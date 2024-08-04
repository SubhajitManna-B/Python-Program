import math

def compute_values():
    power = 5 ** 8
    sqrt = math.sqrt(400)
    exp = math.exp(5)
    log_base_5 = math.log(625, 5)
    
    return power, sqrt, exp, log_base_5

# Example usage
power, sqrt, exp, log_base_5 = compute_values()
print("5 to the power of 8:", power)
print("Square root of 400:", sqrt)
print("Exponent of 5:", exp)
print("Logarithm of 625 base 5:", log_base_5)
