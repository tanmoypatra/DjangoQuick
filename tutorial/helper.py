__author__ = 'tanmoy'

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

if __name__ == '__main__':

    snippet = Snippet(code='foo = "bar"\n')
    snippet.save()

    snippet = Snippet(code='print "hello, world"\n')
    snippet.save()

    serializer = SnippetSerializer(snippet)
    print serializer.data
    content =JSONRenderer().render(serializer.data)
    print content
