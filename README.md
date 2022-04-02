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

The `schema.graphql` file is generated upon running the developer server.

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

## Codegen

Create a `query.graphql` file with the following contents:

```graphql
query MyQuery {
  books {
    title
    author
  }
  users {
    id
    name
    friends
  }
}
```

Export types for python and typescript:

```bash
strawberry codegen --schema schema --output-dir ./output -p python -p typescript .graphql/query.graphql
```
