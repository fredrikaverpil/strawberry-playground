# strawberry-playground

Playing around with [Strawberry GraphQL](https://strawberry.rocks).

## Install and run

With a virtual environment activated:

```bash
poetry install
```

Then either run the development server:

```bash
strawberry server sbplay.schema
```

...or run the production server:

```bash
sbplay
```

The `schema.graphql` file is generated upon running the developer server.

## Perform queries

- Go to http://0.0.0.0:8000/graphql
- Run queries below

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

```graphql
query TestQuery($title: String! = "the lord of the rings") {
  books(title: $title) {
    title
    author
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

Export types for python and typescript into the `output` folder:

```bash
strawberry codegen --schema sbplay.schema --output-dir ./output -p python -p typescript .graphql/query.graphql
```
