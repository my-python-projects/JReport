from models.user import User

def register_user(db, email, password):
    if db.users.find_one({'email': email}):
        return None
    user = User(email, password)
    db.users.insert_one({
        'email': user.email,
        'password': user.password
    })
    return user

def authenticate_user(db, email, password):
    user_data = db.users.find_one({'email': email})
    if user_data:
        user = User(user_data['email'], user_data['password'])
        if user.check_password(password):
            return user
    return None
