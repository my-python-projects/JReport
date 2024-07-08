from mongoengine import Document, StringField, BooleanField, DateTimeField
from werkzeug.security import generate_password_hash, check_password_hash
import pyotp

class User(Document):
    username            = StringField(required=True, unique=True)
    password_hash       = StringField(required=True)
    email               = StringField(required=True, unique=True)
    two_factor_enabled  = BooleanField(default=False)
    two_factor_secret   = StringField()

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def enable_two_factor(self):
        self.two_factor_enabled = True
        self.two_factor_secret  = pyotp.random_base32()

    def get_totp_uri(self):
        return pyotp.TOTP(self.two_factor_secret).provisioning_uri(self.email, issuer_name="YourApp")

    def verify_totp(self, token):
        totp = pyotp.TOTP(self.two_factor_secret)
        return totp.verify(token)
