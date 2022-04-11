from rest_framework import serializers
from .models import Myprofile,Myprojects

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Myprojects
        fields = ('title', 'description')

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Myprofile
        fields = ('name', 'bio','email')