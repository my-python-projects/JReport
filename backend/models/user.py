from werkzeug.security import generate_password_hash, check_password_hash

class User:
    def __init__(self, email, password):
        self.email = email
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
