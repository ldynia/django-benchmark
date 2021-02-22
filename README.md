# Instructions

```bash
$ docker-compose up
$ docker exec -it django-demo ash
$ umask 113
$ python manage.py seed
```

```

# Examples

### REST API

```bash
$ time curl http://172.25.0.2:8080/api/rest/dummy/
```

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