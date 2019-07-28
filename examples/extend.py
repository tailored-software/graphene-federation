import graphene
from graphene_federation import build_schema, extend


@extend(fields='id')
class Message(graphene.ObjectType):
    id = graphene.Int(required=True)

    def resolve_id(self, **kwargs):
        return 1


class Query(graphene.ObjectType):
    message = graphene.Field(Message)

    def resolve_file(self, **kwargs):
        return None  # no direct access


schema = build_schema(Query)

query = '''
    query getSDL {
      _service {
         sdl
      }
    }
'''
result = schema.execute(query)
print(result.data)