from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer

from demo.models import Dummy


class DummySerializer(ModelSerializer):

    class Meta:
        model = Dummy
        fields = ['id']


@api_view(['GET'])
def dummy_list(request):
    """
    List all code Dummy, or create a new snippet.
    """
    data = Dummy.objects.all()
    serializer = DummySerializer(data, many=True)

    return Response(serializer.data)
