from models import User

def get_user(user_id: int) -> User:
    # Dummy user retrieval logic
    return User(id=user_id, username='test', email='test@example.com')