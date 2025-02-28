import bcrypt
import random
import string


def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed


def verify_password(hashed_password, user_password):
    return bcrypt.checkpw(user_password.encode('utf-8'), hashed_password)


def generate_passcode():
    return ''.join(random.sample(string.ascii_letters + string.digits, 6))
