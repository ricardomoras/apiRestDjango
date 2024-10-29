from rest_framework import serializers
from .models import Programer

class ProgramerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Programer
        # fields=('fullname','nickname',)
        fields='__all__'