import os
import json
import psycopg2
import redis

pg = psycopg2.connect(
    host=os.getenv("DB_HOST", "postgres"),
    dbname=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
)

cache = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=6379,
    password=os.getenv("REDIS_PASSWORD"),
    decode_responses=True,
)


def obtener_productos():
    datos = cache.get("productos")
    if datos:
        print("Desde Redis (cache)")
        return json.loads(datos)
    print("Desde PostgreSQL")
    with pg.cursor() as cur:
        cur.execute("SELECT id, nombre, precio::float FROM productos;")
        filas = cur.fetchall()
    cache.set("productos", json.dumps(filas), ex=60)
    return filas


print(obtener_productos())  # primera vez: PostgreSQL
print(obtener_productos())  # segunda vez: Redis
