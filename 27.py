# 27.
# Validating Inputs.


def validate_fname(fname):
    if len(fname) == 0:
        print("The first name must be filled in.")
    elif len(fname) > 0 and len(fname) >= 2:
        return True
    else:
        print(f'"{fname}" is not a valid first name. It is too short.')


def validate_lname(lname):
    if len(lname) == 0:
        print("The last name must be filled in.")
    elif len(lname) >= 2:
        return True
    else:
        print(f'"{lname}" is not a valid last name. It is too short.')


def validate_zip(zip_code):
    if zip_code.isdigit() is False:
        print("The ZIP code must be numeric.")
    elif len(zip_code) < 5:
        print("The ZIP code is too short.")
    else:
        return True


def validate_empid(empid):
    if len(empid) != 7:
        print(f'"{empid}" is not a valid ID.')
    else:
        if empid[0:1].isalpha() is False:
            print(f'"{empid}" is not a valid ID.')
        elif empid[2] != "-":
            print(f'"{empid}" is not a valid ID.')
        elif empid[3:6].isdigit() is False:
            print(f'"{empid}" is not a valid ID.')
        else:
            return True


def validate_input(*args):
    if None in args:
        pass
    else:
        print("There were no errors found.")


print("Enter the first name:")
user_fname = input()
print("Enter the last name:")
user_lname = input()
print("Enter the zip code:")
user_zip = input()
print("Enter an employee ID:")
user_empid = input()

validate_input(
    validate_fname(user_fname),
    validate_lname(user_lname),
    validate_zip(user_zip),
    validate_empid(user_empid)
)
