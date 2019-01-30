from rest_framework import serializers

from .models import Data

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ('id_num', 'title', 'link', 'city', 'main_image', )
