import redis
import time

r = redis.Redis(
    host='happy-stitch-trick-90283.db.redis.io',
    port=14633,
    password='EUTo8FNmrR2XZW8gzE4pbxFVwKWWRfWW',
    decode_responses=True
)

print("Publisher started sending messages")

for i in range(10):
    message = f"Hello Redis! Message #{i}"
    r.publish('python_channel', message)
    print(f"Sent: {message}")
    time.sleep(0.3)

print("10 messages successfully sent")
