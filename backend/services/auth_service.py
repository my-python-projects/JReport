import pyotp
import qrcode
import base64
import pyotp
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token
from flask import current_app
import png  # Importa o módulo pypng
from io import BytesIO

def create_user(db, username, email, password):
    hashed_password = generate_password_hash(password)
    secret          = pyotp.random_base32()  # Gera uma chave secreta para 2FA
    try:
        print(f"Generated 2FA secret: {secret}")
        db.users.insert_one({
            'username'  : username,
            'email'     : email, 
            'password'  : hashed_password, 
            '2fa_secret': secret
        })
        return True, secret
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
    print(f"Verifying token: {token} with secret: {secret}")
    return totp.verify(token, valid_window=1)

def generate_qr_code(secret, email):
    issuer = current_app.config['TWO_FACTOR_AUTH_ISSUER']
    totp = pyotp.TOTP(secret)
    uri = totp.provisioning_uri(name=email, issuer_name=issuer)
    qr = qrcode.make(uri)
    buffered = BytesIO()
    qr.save(buffered)  # Remove o argumento 'format'
    img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
    return img_str