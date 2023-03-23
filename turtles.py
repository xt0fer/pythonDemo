
# ....

try:
    fin = open('i_like_turtles.py', 'r')
    # ...
except FileNotFoundError:
    print('Oh well! The file does not exist!')
    # might as well create it

# more code

print('run this dammit! run turtles')

try:
    print(100 / 10)
except ZeroDivisionError:
    print("Division by zero is not allowed.")
else:
    print("No issues were encountered.")
finally:
    print("This runs no matter what happened.")

