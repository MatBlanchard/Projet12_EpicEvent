from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from app.permissions import IsManager
from app.serializers import SignupSerializer


class SignupViewSet(ViewSet):
    permission_classes = [IsManager]

    @action(methods=['post'], detail=False)
    def signup(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

