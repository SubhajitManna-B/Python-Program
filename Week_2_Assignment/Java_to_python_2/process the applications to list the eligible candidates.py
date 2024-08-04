n = int(input("Enter number of students: "))

for i in range(n):
    math, physics, chemistry = map(int, input(f"Enter marks for student {i+1} in Mathematics, Physics, Chemistry: ").split())
    
    if (math >= 60 and physics >= 50 and chemistry >= 40 and (math + physics + chemistry >= 200)) or (math + physics >= 150):
        print(f"Student {i+1} is eligible.")
    else:
        print(f"Student {i+1} is not eligible.")
