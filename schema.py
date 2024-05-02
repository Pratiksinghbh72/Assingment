import graphene
from collections.abc import Mapping

class Bank(graphene.ObjectType):
    name = graphene.String()

class Branch(graphene.ObjectType):
    branch = graphene.String()
    ifsc = graphene.String()
    bank = graphene.Field(Bank)

class Query(graphene.ObjectType):
    branches = graphene.List(Branch)

    def resolve_branches(self, info):
        # Implement logic to fetch branches from your database
        # Replace this with your actual data fetching logic
        return [{'branch': 'Branch 1', 'ifsc': 'IFSC1', 'bank': {'name': 'Bank 1'}},
                {'branch': 'Branch 2', 'ifsc': 'IFSC2', 'bank': {'name': 'Bank 2'}}]

schema = graphene.Schema(query=Query)


