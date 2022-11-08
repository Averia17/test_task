from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from users.models import User
from users.serializers import UserSerializer


class UserViewSet(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @action(detail=False, methods=["GET"], permission_classes=(IsAuthenticated,))
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)
