import time
import jwt

SECRET_KEY = "my_super_secret_key_at_least_256_bits_long"
WRONG_SECRET_KEY = "wrong_secret_key_for_testing_errors"

payload = {
    "lastName": "Волчек",
    "group": "group25082026",
    "sub": "subject_test"
}

print("ТЕст 1: Успішне декодування")

payload_success = payload.copy()
payload_success["exp"] = int(time.time()) + 3600

token = jwt.encode(payload_success, SECRET_KEY, algorithm="HS256")
print(f"Згенерований токен:\n{token}\n")

try:
    decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    print("Токен успішно декодовано на ПК:")
    print(decoded)
except Exception as e:
    print(f"Помилка: {e}")

print("Тест 2: Помилка просрочення токена")

payload_expired = payload.copy()
payload_expired["exp"] = int(time.time()) - 10

token_expired = jwt.encode(payload_expired, SECRET_KEY, algorithm="HS256")

try:
    jwt.decode(token_expired, SECRET_KEY, algorithms=["HS256"])
except jwt.ExpiredSignatureError as e:
    print("Токен неуспішно декодовано на ПК з помилкою прострочення:")
    print(f"Помилка: {e} (Термін дії токена закінчився)")
except Exception as e:
    print(f"Інша помилка: {e}")

print("Тест 3: Помилка невірного підпису")

try:
    jwt.decode(token, WRONG_SECRET_KEY, algorithms=["HS256"])
except jwt.InvalidSignatureError as e:
    print("Токен неуспішно декодовано на ПК з помилкою підпису:")
    print(f"Помилка: {e} (Невірний секретний ключ)")
except Exception as e:
    print(f"Інша помилка: {e}")

print(f"Секретний ключ для вставки на jwt.io:\n{SECRET_KEY}")
