import pyotp
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token

def create_user(db, username, email, password):
    hashed_password = generate_password_hash(password)
    secret          = pyotp.random_base32()  # Gera uma chave secreta para 2FA
    try:
        db.users.insert_one({
            'username' : username,
            'email'     : email, 
            'password'  : hashed_password, 
            '2fa_secret': secret
        })
        return True
    except Exception as e:
        print(f"Error creating user: {e}")
        return False

def authenticate_user(db, email, password):
    user = db.users.find_one({'email': email})
    if user and check_password_hash(user['password'], password):
        return user
    else:
        return None

def generate_tokens(user):
    access_token  = create_access_token(identity=user['email'])
    refresh_token = create_refresh_token(identity=user['email'])
    return access_token, refresh_token

def verify_2fa_token(secret, token):
    totp = pyotp.TOTP(secret)
    return totp.verify(token)
