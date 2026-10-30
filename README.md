# Docker con Redis y PostgreSQL

Entorno con PostgreSQL 17, Redis 7 y una app Python de ejemplo (patron cache-aside), orquestado con Docker Compose.

## Uso

```bash
cp .env.example .env      # en Windows: copy .env.example .env
docker compose up -d --build
docker compose ps
docker compose logs app
```

## Estructura

- `docker-compose.yml`: servicios postgres, redis y app
- `.env.example`: variables de entorno (copiar a `.env`)
- `init/01-esquema.sql`: tabla y datos iniciales
- `app/`: aplicacion Python que lee de PostgreSQL y cachea en Redis
