import os
from dotenv import load_dotenv
import redis

load_dotenv()

r = redis.Redis(
    host=os.getenv("REDIS_HOST"),
    port=int(os.getenv("REDIS_PORT")),
    password=os.getenv("REDIS_PASSWORD"),
    decode_responses=True
)

try:
    if r.ping():
        print("підключено до редіс")
except Exception as e:
    print(f"Помилка підключення: {e}")
    exit()

r.set("favorite_car", "Hyndai Sonata 2009")
print(f"1. Авто збережено: {r.get('favorite_car')}")

r.set("favorite_pet", "Кішка Аліса, Кішка Мейсі", ex=7200)
print(f"2. Улюбленецей збережено (Час до зникнення: {r.ttl('favorite_pet')} секонд): {r.get('favorite_pet')}")

r.delete("shopping_list")
products = ["Молоко", "Хліб", "Яйця", "Сир"]
r.rpush("shopping_list", *products)
r.expire("shopping_list", 604800)
print(f"3. Список продуктів: {r.lrange('shopping_list', 0, -1)} (Час до зникнення: {r.ttl('shopping_list')} секонд)")

r.delete("cake_ingredients")
cake_data = {"flour": "250", "milk": "500"}
r.hset("cake_ingredients", mapping=cake_data)
print(f"4. Початкові інгредієнти торта: {r.hgetall('cake_ingredients')}")

r.hset("cake_ingredients", "sugar", "300")
print(f"5. Додано цукор: {r.hgetall('cake_ingredients')}")

r.hset("cake_ingredients", "sugar", "500")
print(f"6. Виправлено цукор: {r.hgetall('cake_ingredients')}")
