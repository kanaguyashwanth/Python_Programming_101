# Multiple return values:

# CODE: [Converting string to Title Case] [Function with a multiple return statements]

def format_name(f_name, l_name):
    # If no inputs are provided, then prompt to provide input.
    if f_name == "" or l_name == "":
        return "Please provide a valid input."
    
    # Using title function
    converted_f_name = f_name.title()
    converted_l_name = l_name.title()
    return f"{converted_f_name} {converted_l_name}"

print(format_name(input("Enter your first name: "), input("Enter your last name: ")))
