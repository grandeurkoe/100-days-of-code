# Creating a new class named User
class User:
    # 'pass' keyword can be used when you don't want to write a bunch of code in the class definition at the start.
    # Initialize the attribute values during the creation of an object using the __init__() function. This is called
    # as a Class constructor. Here self is the actual object being initialized.
    def __init__(self, ids, user_name):
        self.id = ids
        self.user_name = user_name
        self.value = 0

    # Here 'self' is the object that is calling the set_value() function.
    def set_value(self):
        self.value = 1
        return self.value


# Creating an object 'first_user' of User class.
# __init__() function will be called everytime an object is created.
# Pass "001" and "Meowya" as positional arguments to the __init__() function.
first_user = User("001", "Meowya")
second_user = User("002", "Vishal")

# Creating attributes for the first_user object.
# first_user.id = "001"
# first_user.user_name = "Meowya"

print(first_user.user_name)
print(second_user.user_name)
print(first_user.value)

# Calling the set_value() function.
print(first_user.set_value())
