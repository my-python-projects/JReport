from werkzeug.security import generate_password_hash, check_password_hash

def create_user(db, email, password):
    hashed_password = generate_password_hash(password)
    try:
        db.users.insert_one({'email': email, 'password': hashed_password})
        return True
    except Exception as e:
        print(f"Error creating user: {e}")
        return False

def authenticate_user(db, email, password):
    user = db.users.find_one({'email': email})
    if user and check_password_hash(user['password'], password):
        return True
    else:
        return False
