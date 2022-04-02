import strawberry

from sbplay.resolvers import Query

schema = strawberry.Schema(query=Query)
