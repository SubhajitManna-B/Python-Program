import math

def compute_trig_values():
    sin_60 = math.sin(math.radians(60))
    cos_pi = math.cos(math.pi)
    sin_val = math.sin(0.8660254037844386)
    try:
        tan_90 = math.tan(math.radians(90))
    except ValueError:
        tan_90 = 'undefined'
    
    return sin_60, cos_pi, sin_val, tan_90

# output
sin_60, cos_pi, sin_val, tan_90 = compute_trig_values()
print("sin(60 degrees):", sin_60)
print("cos(pi):", cos_pi)
print("sin(0.8660254037844386):", sin_val)
print("tan(90 degrees):", tan_90)
