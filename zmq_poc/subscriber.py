import json
import zmq
from time import sleep

PORT = 2000
TOPIC = 'main'

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect(f'tcp://zmq-publisher:{PORT}')
socket.subscribe(topic=TOPIC)

try:
    while True:
        message = socket.recv_string()
        _, body = message.split(maxsplit=1)
        deserialized = json.loads(body)

        song = deserialized.get('song')
        album = deserialized.get('album')
        artist = deserialized.get('artist')

        print(f'Song: {song}')
        print(f'Album: {album}')
        print(f'Artist: {artist}')
        print()

        sleep(1)
except KeyboardInterrupt:
    pass
