import random
import string


def generate_random_user():
    """Генерирует случайного пользователя"""
    email = ''.join(random.choices(string.ascii_lowercase, k=8)) + '@test.ru'
    password = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    name = ''.join(random.choices(string.ascii_lowercase, k=6))
    
    return {
        "email": email,
        "password": password,
        "name": name
    }