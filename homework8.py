import os
from dotenv import load_dotenv
import redis

load_dotenv()

r = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", "6379")),
    password=os.getenv("REDIS_PASSWORD", ""),
    decode_responses=True,
)
print("Найулюбленіша машина")
r.set("favorite_car", "Hyundai Sonata 2009")
print(r.get("favorite_car"))

print("Найулюбленіший питомець")
r.set("favorite_pet", "Кішка Аліса, Кішка Мейсі", ex=7200)
print(r.get("favorite_pet"), r.ttl("favorite_pet"))

print("Список покупок")
r.delete("shopping_list")
r.rpush("shopping_list", "Хліб", "молоко", "яйця")
r.expire("shopping_list", 604800)
print(r.lrange("shopping_list", 0, -1), r.ttl("shopping_list"))

print("Інградієнти для торта")
cake_ingredients = {"flour": "250", "milk": "500"}
r.hset("cake_recipe", mapping=cake_ingredients)
print(r.hgetall("cake_recipe"))

print("Рецепт торта")
r.hset("cake_recipe", "sugar", "300")
print(r.hgetall("cake_recipe"))

print("Виправлений рецепт")
r.hset("cake_recipe", "sugar", "500")
print(r.hgetall("cake_recipe"))
