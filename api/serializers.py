from dataclasses import fields
from pyexpat import model
from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'description']
        
    