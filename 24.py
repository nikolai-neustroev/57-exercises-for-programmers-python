# 24.
# Anagram Checker


def check_len(x, y):
    if len(x) != len(y):
        print("Strings are not anagrams.")
        exit()


def is_anagram(x, y):
    x = [char for char in x]
    y = [char for char in y]
    if sorted(x) == sorted(y):
        print("Strings are anagrams.")
    else:
        print("Strings are not anagrams.")


print("Enter two strings and I'll tell you if they are anagrams.")
print("Enter the first string:")
first = input().upper()
print("Enter the second string:")
second = input().upper()

check_len(first, second)
is_anagram(first, second)
