import os

from dotenv import load_dotenv
from redis import Redis

load_dotenv(".env.falkordb")

host = os.getenv("FALKOR_HOST")
port = int(os.getenv("FALKOR_PORT"))
username = os.getenv("FALKOR_USERNAME")
password = os.getenv("FALKOR_PASSWORD")

client = Redis(
    host=host,
    port=port,
    username=username,
    password=password,
    ssl=True,
    decode_responses=True
)

print(client.ping())
print("Connected Successfully!")