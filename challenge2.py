#Vashti Dalchand
#Period #1-2
#2/27/25
#Python Coding Challenge 2

def right_justify(s):
    # Calculate the number of leading spaces required
    spaces_needed = 70 - len(s)
    # Create the justification string by adding the required spaces
    justified_string = ' ' * spaces_needed + s
    # Print the justified string
    print(justified_string)

# Example usage
right_justify('allen')
