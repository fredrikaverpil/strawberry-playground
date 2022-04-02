# strawberry-playground

Playing around with [Strawberry GraphQL](https://strawberry.rocks).

## Install and run

With a virtual environment activated:

```bash
poetry install
```

```bash
# development server
strawberry server schema
```

## Perform query

- Go to http://0.0.0.0:8000/graphql
- Run query

```graphql
{
  books {
    title
    author
  }

  users {
    name
    friends
  }
}
```
