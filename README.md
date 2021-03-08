# Instructions

```bash
$ docker-compose up
$ docker inspect django-benchmark | grep IPAddress | tail -n1 | awk '{print $2}'
"172.26.0.2",

$ docker exec -it django-benchmark ash
$ umask 113
```

# Varnish

```bash
$ varnishd -f /app/config/varnish.vcl -s malloc,256M -T 127.0.0.1:2000 -a 0.0.0.0:8888
```

# Examples

## Populate database with dummy data

```bash
$ docker exec -it django-benchmark python manage.py seed 1000
```

## Benchmark API vs GraphQL

```bash
$ time curl http://localhost:8080/api/rest/dummy/
$ time curl 'http://localhost:8080/api/graphql/' \
  -X 'GET' \
  -H 'Content-Type: application/json' \
  --data-raw '{"query":"query { allDummy { results { id } }}","variables":null}'
```

## GraphQL

### Queries
```
query {
  allDummy {
    results {
      id
      day
      weekday
      month
      year
      preSeeded
      createdAt
    }
  }
}
```

### Mutations

```
mutation {
  createDummy(newDummy:{ day:1, weekday: "Monday", month: "December", year: 2020}) {
    ok
    dummy {
      id
      day
      weekday
      month
      year
    }
  }
}
```