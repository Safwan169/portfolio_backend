from .models import tecnologies
from  rest_framework import serializers
class tecnologiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = tecnologies
        fields = '__all__'