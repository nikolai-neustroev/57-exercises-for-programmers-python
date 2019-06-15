# 21.
# Numbers to Names

supp_lngs = ["ENG", "RUS"]

months = {
    "1": ["January", "Январь"],
    "2": ["February", "Февраль"],
    "3": ["March", "Март"],
    "4": ["April", "Апрель"],
    "5": ["May", "Май"],
    "6": ["June", "Июнь"],
    "7": ["July", "Июль"],
    "8": ["August", "Август"],
    "9": ["September", "Сентябрь"],
    "10": ["October", "Октябрь"],
    "11": ["November", "Ноябрь"],
    "12": ["December", "Декабрь"]
}


def choose_lng():
    print(f"Please choose language: {supp_lngs}")
    lng = str(input()).upper()
    if lng in supp_lngs:
        return lng
    else:
        return choose_lng()


def n2n(key, lng):
    return months[key][supp_lngs.index(lng)]


def input_mnumber():
    print("Please enter the number of required month.")
    try:
        mnumber = int(input())
        if mnumber in range(1, 13):
            return str(mnumber)
        else:
            print("Please enter a correct month number.")
            return input_mnumber()
    except ValueError:
        print("Error. Input must be a whole number.")
        return input_mnumber()


user_lng = choose_lng()

month = input_mnumber()

print(n2n(month, user_lng))
