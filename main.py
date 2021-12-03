import datetime
import hashlib
import os






class Task:
    def __init__(self) -> None:
        self.identifier
        self.title
        self.description 
        self.date_added

    def edit(self):
        pass

    def create(self):
        pass

    def finish(self):
        pass


class Tasklist:
    def __init__(self) -> None:
        pass
    

def main():
    salt = os.urandom(32)
    password = 'password123'

    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000, dklen=128)

    storage = salt + key

    salt_from_storage = storage[:32]
    key_from_storage = storage[32:]

    print(salt_from_storage)
    print(key_from_storage)


if __name__ == "__main__":
    main()