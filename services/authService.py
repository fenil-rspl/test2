from models import User

def authenticate_user(username: str, password: str) -> User:
    # Dummy authentication logic
    if username == 'test' and password == 'test':
        return User(username='test', email='test@example.com')
    return None