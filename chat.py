import redis
import json

HOST='de.futoke.ru'
PORT=6379
PIPE_NAME = 'itmo'

def init_chat():
    connector=redis.StrictRedis(
        host=HOST,
        port=PORT,
        db=0,
        username='default',
        password='itmoredis',
        charset='utf-8',
        decode_responses=True
    )
    reader = connector.pubsub()
    reader.subscribe(PIPE_NAME)
    return connector, reader


def send_msg(msg):
    connector.publish(PIPE_NAME,json.dumps(msg))


def read_msg(callback):
    for msg in reader.listen():
        print(msg)
        data=msg['data']
        if type(data) is int:
            continue
        else:
            data=json.loads(data)
            callback(f"{data['user']}\n{data['text']}")
connector,reader = init_chat()
