__author__ = 'tanmoy'
from rest_framework import serializers
from snippets.models import Snippet

class SnippetSerializer(serializers.Serializer):
    pk = serializers.