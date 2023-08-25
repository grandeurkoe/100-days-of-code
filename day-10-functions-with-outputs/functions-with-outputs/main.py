# Function with Outputs
def format_name(first_name, last_name):
    if first_name == "" or last_name == "":
        return "You didn't provide valid inputs"
    full_name = first_name.title() + " " + last_name.title()
    return full_name


f_name = input("Enter first name: ")
l_name = input("Enter family name: ")
my_name = format_name(f_name, l_name)
print(f"Result: {my_name}.")
