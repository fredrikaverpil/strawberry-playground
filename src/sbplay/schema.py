import pathlib

import strawberry

from sbplay.resolvers import Query

schema = strawberry.Schema(query=Query)

with open(pathlib.Path(".graphql/schema.graphql"), "w") as outfile:
    outfile.write(str(schema))
