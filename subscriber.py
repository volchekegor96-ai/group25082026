import redis

r = redis.Redis(
    host='happy-stitch-trick-90283.db.redis.io',
    port=14633,
    password='EUTo8FNmrR2XZW8gzE4pbxFVwKWWRfWW',
    decode_responses=True
)

pubsub = r.pubsub()
pubsub.subscribe('python_channel')

print("Subscriber started and listening to python_channel")

try:
    for message in pubsub.listen():
        if message['type'] == 'message':
            print(message['data'])
except KeyboardInterrupt:
    print("\nSubscriber stopped")
