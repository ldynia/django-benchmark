from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from graphene_django.views import GraphQLView
from demo.api.rest.dummy.views import dummy_list

from config.schema import schema


urlpatterns = [
    path('admin/', admin.site.urls),
    # API(s)
    path('api/rest/dummy/', csrf_exempt(dummy_list)),
    path("api/graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
]

