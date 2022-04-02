import dotenv
import uvicorn
from starlette.applications import Starlette
from strawberry.asgi import GraphQL

from sbplay.schema import schema


def create_app():
    graphql_app = GraphQL(schema)

    app = Starlette()
    app.add_route("/graphql", graphql_app)
    app.add_websocket_route("/graphql", graphql_app)

    return app


def main():
    dotenv.load_dotenv("env/.env.prod")
    uvicorn.run("sbplay.app:create_app", factory=True, reload=True)


if __name__ == "__main__":
    main()
