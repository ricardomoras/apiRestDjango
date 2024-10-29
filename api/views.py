from rest_framework import viewsets
from .serializer import ProgramerSerializer
from .models import Programer

# Create your views here.


class ProgramerViewSet(viewsets.ModelViewSet):
    queryset = Programer.objects.all()
    serializer_class = ProgramerSerializer