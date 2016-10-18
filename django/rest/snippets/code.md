example
=======

note
----

``` python
# model
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

snippet = Snippet(code='foo = "bar"\n')
snippet.save()

snippet = Snippet(code='print "hello, world"\n')
snippet.save()

# serialize instance
serializer = SnippetSerializer(snippet)
serializer.data
# {'pk': 2, 'title': u'', 'code': u'print "hello, world"\n',
# 'linenos': False, 'language': u'python', 'style': u'friendly'}

# to json
content = JSONRenderer().render(serializer.data)
content
# '{"pk": 2, "title": "", "code": "print \\"hello, world\\"\\n",
# "linenos": false, "language": "python", "style": "friendly"}'


# deserialize
from django.utils.six import BytesIO

stream = BytesIO(content)
data = JSONParser().parse(stream)

# restore into object instance
serializer = SnippetSerializer(data=data)
serializer.is_valid()
# True
serializer.validated_data
# OrderedDict([('title', ''), ('code', 'print "hello, world"\n'),
# ('linenos', False), ('language', 'python'), ('style', 'friendly')])
serializer.save()
# <Snippet: Snippet object>

# serialize querysets
serializer = SnippetSerializer(Snippet.objects.all(), many=True)
serializer.data
# [OrderedDict([('pk', 1), ('title', u''), ('code', u'foo = "bar"\n'),
# ('linenos', False), ('language', 'python'), ('style', 'friendly')]),
# OrderedDict([('pk', 2), ('title', u''), ('code', u'print "hello,
# world"\n'), ('linenos', False), ('language', 'python'), ('style',
# 'friendly')]), OrderedDict([('pk', 3), ('title', u''), ('code',
# u'print "hello, world"'), ('linenos', False), ('language', 'python'),
# ('style', 'friendly')])]

# change to model serializer
from snippets.serializers import SnippetSerializer
serializer = SnippetSerializer()
print(repr(serializer))
# SnippetSerializer():
#    id = IntegerField(label='ID', read_only=True)
#    title = CharField(allow_blank=True, max_length=100, required=False)
#    code = CharField(style={'base_template': 'textarea.html'})
#    linenos = BooleanField(required=False)
#    language = ChoiceField(choices=[('Clipper', 'FoxPro'), ('Cucumber',
#  'Gherkin'), ('RobotFramework', 'RobotFramework'), ('abap', 'ABAP'),
# ('ada', 'Ada')...
#    style = ChoiceField(choices=[('autumn', 'autumn'), ('borland',
# 'borland'), ('bw', 'bw'), ('colorful', 'colorful')...

# test api(或者直接浏览器访问)
$ pip install httpie
$ http http://127.0.0.1:8000/snippets/

# format suffix ---------
# Accept
http http://127.0.0.1:8000/snippets/ Accept:application/json  # Request JSON
http http://127.0.0.1:8000/snippets/ Accept:text/html         # Request HTML
# suffix
http http://127.0.0.1:8000/snippets.json  # JSON suffix
http http://127.0.0.1:8000/snippets.api   # Browsable API suffix
# Content-Type header
http --form POST http://127.0.0.1:8000/snippets/ code="print 123"
http --json POST http://127.0.0.1:8000/snippets/ code="print 456"
# see request type
http --debug --json POST http://127.0.0.1:8000/snippets/ code="print 456"
http://127.0.0.1:8000/snippets/


```
