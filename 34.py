# 34.


def remove_name(emp):
    try:
        emp.remove(input())
    except ValueError:
        print("Type existing name")
        return remove_name(emp)


user_emp = ["John", "Jack", "James", "Roy", "Ray"]
print(f"There are {len(user_emp)} employees: {user_emp}")

print("Enter an employee to remove")
remove_name(user_emp)
print(f"There are {len(user_emp)} employees: {user_emp}")
