import time


def login():
    return "login---------time:%s" % time.ctime()


def register():
    return "register---------time:%s" % time.ctime()


def profile():
    return "profile---------time:%s" % time.ctime()


def main(file_name):
    if file_name == "login.py":
        return login()
    elif file_name == "register.py":
        return register()
    elif file_name == "profile.py":
        return profile()
    else:
        return "not found"
