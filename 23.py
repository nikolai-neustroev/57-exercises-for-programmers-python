# 23.
# Troubleshooting Car Issues

questions = {
    "root": "Is the car silent when you turn the key?",
    "y_node_1": "Are the battery terminals corroded?",
    "n_node_1": "Does the car make a clicking noise?",
    "y_node_21": "Clean terminals and try starting again.",
    "n_node_21": "Replace cables and try again.",
    "y_node_22": "Replace the battery.",
    "n_node_22": "Does the car crank up but fail to start?",
    "y_node_3": "Check spark plug connections.",
    "n_node_3": "Does the engine start and then die?",
    "y_node_4": "Does your car have fuel injection?",
    "n_node_5": "Check to ensure the choke is opening and closing.",
    "y_node_5": "Get it in for service."
}


def ask(question):
    print(question)
    answer = input().upper()
    if answer in ["YES", "NO", "Y", "N"]:
        return answer
    else:
        print("Please enter 'yes' or 'no'.")
        return ask(question)


ans0 = ask(questions["root"])
if ans0 in ["YES", "Y"]:
    ans1 = ask(questions["y_node_1"])
    if ans1 in ["YES", "Y"]:
        print(questions["y_node_21"])
    else:
        print(questions["n_node_21"])
else:
    ans1 = ask(questions["n_node_1"])
    if ans1 in ["YES", "Y"]:
        print(questions["y_node_22"])
    else:
        ans2 = ask(questions["n_node_22"])
        if ans2 in ["YES", "Y"]:
            print(questions["y_node_3"])
        else:
            ans3 = ask(questions["n_node_3"])
            if ans3 in ["YES", "Y"]:
                ans4 = ask(questions["y_node_4"])
                if ans4 in ["YES", "Y"]:
                    print(questions["y_node_5"])
                else:
                    print(questions["n_node_5"])
