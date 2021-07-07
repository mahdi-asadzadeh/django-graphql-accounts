from graphql_jwt.decorators import login_required
from django.contrib.auth import get_user_model
from .types import UserType
import graphene


User = get_user_model()


class AccountsQuery(graphene.ObjectType):
    account = graphene.Field(UserType)

    @login_required
    def resolve_account(parent, info):
        user = info.context.user
        return User.objects.get(id=user.id)
        