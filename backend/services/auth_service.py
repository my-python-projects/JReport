import pyotp
import qrcode
import base64
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token
from flask import current_app
from io import BytesIO
from log_config import setup_logging

logger = setup_logging()

def create_user(db, username, email, password):
    hashed_password = generate_password_hash(password)
    secret          = pyotp.random_base32()  # Gera uma chave secreta para 2FA
    
    try:
        logger.debug(f"Generated 2FA secret: {secret}")
        
        db.users.insert_one({
            'username'   : username,
            'email'      : email, 
            'password'   : hashed_password, 
            '2fa_secret' : secret,
            '2fa_enabled': False  # Por padrão, o 2FA está desabilitado
        })
        
        return True, secret
    
    except Exception as e:
        logger.error(f"Error creating user: {e}")
        return False, None

def authenticate_user(db, email, password, token_2fa=None):

    logger.debug(f"Authenticate User: {email}")
    user = db.users.find_one({'email': email})
    
    if not user:
        logger.error(f"User not found for email: {email}")
        return None, 'User not found'
    
    if not check_password_hash(user['password'], password):
        logger.error(f"Invalid password attempt for email: {email}")
        return None, 'Invalid password'

    if user.get('2fa_enabled', False):
        if not token_2fa:
            logger.error(f"2FA token not provided for email: {email}")
            return None, '2FA required'
        
        if not verify_2fa_token(user['2fa_secret'], token_2fa):
            logger.error(f"Invalid 2FA token for email: {email}")
            return None, 'Invalid 2FA token'

    access_token  = create_access_token(identity=user['email'])
    refresh_token = create_refresh_token(identity=user['email'])
    
    return {'success': True, 'access_token': access_token, 'refresh_token': refresh_token, 'require_2fa': user.get('2fa_enabled', False)}, None

def enable_2fa(db, email, token_2fa):
    logger.info(f"Authenticate User: {email}")
    user = db.users.find_one({'email': email})
    
    if not user:
        logger.error('User not found')
        return False, 'User not found'
    
    if verify_2fa_token(user['2fa_secret'], token_2fa):
        db.users.update_one({'email': email}, {'$set': {'2fa_enabled': True}})
        return True, None
    
    logger.debug('Invalid 2FA token')
    return False, 'Invalid 2FA token'

def verify_2fa_token(secret, token):
    totp = pyotp.TOTP(secret)
    logger.debug(f"Verifying token: {token} with secret: {secret}")
    return totp.verify(token, valid_window=1)

def is_2fa_enabled(db, email):
    user = db.users.find_one({'email': email})
    if not user:
        logger.error('User not found')
        return None, 'User not found'
    
    return user.get('2fa_enabled', False), None


def generate_qr_code(secret, email):
    issuer      = current_app.config['TWO_FACTOR_AUTH_ISSUER']
    totp        = pyotp.TOTP(secret)
    uri         = totp.provisioning_uri(name=email, issuer_name=issuer)
    qr          = qrcode.make(uri)
    buffered    = BytesIO()
    qr.save(buffered)  # Remove o argumento 'format'
    img_str     = base64.b64encode(buffered.getvalue()).decode('utf-8')
    return img_str