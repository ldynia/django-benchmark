import graphene

from demo.models import Dummy
from demo.api.graphql.common.enums import WeekdayEnum
from demo.api.graphql.common.enums import MonthEnum
from demo.api.graphql.common.types_n_inputs import DummyType


class CreateDummy(graphene.Mutation):

    ok = graphene.Boolean(default_value=True)
    dummy = graphene.Field(DummyType)

    class Arguments:
        id = graphene.ID()
        day = graphene.Int(required=True)
        weekday = WeekdayEnum(required=True)
        month = MonthEnum(required=True)
        year = graphene.Int(required=True)

    @classmethod
    def mutate(cls, root, info, **data):
        try:
            dummy = Dummy.objects.create(**data)
        except Dummy.DoesNotExist:
            return cls(ok=False, dummy=None)
        
        return cls(dummy=dummy)


class UpdateDummy(graphene.Mutation):

    ok = graphene.Boolean(default_value=True)
    dummy = graphene.Field(DummyType)

    class Arguments:
        id = graphene.ID(required=True)
        day = graphene.Int()
        weekday = WeekdayEnum(required=True)
        month = MonthEnum(required=True)
        year = graphene.Int()

    @classmethod
    def mutate(cls, root, info, id, **data):
        try:
            dummy = Dummy.objects.get(id=id)
            if Dummy.objects.filter(id=id).update(**data):
                dummy = Dummy.objects.get(id=id)
        except Dummy.DoesNotExist:
            return cls(ok=False, dummy=None)
        
        return cls(dummy=dummy)


class DeleteDummy(graphene.Mutation):

    ok = graphene.Boolean(default_value=True)

    class Arguments:
        id = graphene.ID(required=True)

    @classmethod
    def mutate(cls, root, info, id):
        try:
            Dummy.objects.get(id=id).delete()
        except Dummy.DoesNotExist:
            return cls(ok=False)
    
        return cls(ok=True)


class DummyMutations(graphene.ObjectType):
    create_dummy = CreateDummy.Field()
    update_dummy = UpdateDummy.Field()
    delete_dummy = DeleteDummy.Field()
