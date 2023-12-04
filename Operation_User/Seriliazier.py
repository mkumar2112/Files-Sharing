from rest_framework import serializers
from .models import Files, USER
from django.contrib.auth.forms import UserCreationForm


class FileSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model=Files
        fields = ['id','File']
    
class SignUpForm(UserCreationForm):
    class Meta:
        model = USER
        fields = ('email', )