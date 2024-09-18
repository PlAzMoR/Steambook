from rest_framework import viewsets
from .models import User, Airticket
from .serializers import UserSerializer, AirticketSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AirticketViewSet(viewsets.ModelViewSet):
    queryset = Airticket.objects.all()
    serializer_class = AirticketSerializer
