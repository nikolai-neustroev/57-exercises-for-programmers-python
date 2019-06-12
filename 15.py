# 15.
# Password Validation

import getpass as gp
import bcrypt

# actual password values
# storage = {"user1": "password1",
#            "user2": "password2",
#            "user3": "password3"}

storage = {"user1": b'$2b$12$ppZlY.W1gLHTsVjVa9oj9OVnVVCtJIqYHVprZ4BUTrzBLgHtNb58G',
           "user2": b'$2b$12$JKWk3lW/IjEXRGQIbMVKAONenokN9pS0CWpXJPEAgHXkmyKbWrhzu',
           "user3": b'$2b$12$k7kKB0m.6LJcipuZXQCCGulhQ8.nWZkmbU7o1DzBvYMBBHaP895vK'}


def enter():
    print("Enter username:")
    username = str(input())
    if username in storage.keys():
        password = gp.getpass().encode("utf-8")
        if bcrypt.checkpw(password, storage[username]) is True:
            print("Welcome!")
        else:
            print("I don't know you.")
    else:
        return enter()


enter()
