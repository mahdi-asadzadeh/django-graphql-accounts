from graphene_django.types import DjangoObjectType
from django.contrib.auth import get_user_model


User = get_user_model()


class UserType(DjangoObjectType):
    class Meta:
        model = User
        exclude = ['password']
