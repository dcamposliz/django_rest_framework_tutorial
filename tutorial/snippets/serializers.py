from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User


class SnippetSerializer(serializers.ModelSerializer):
    """
    Defines SnippetSerializer as a function of Snippet model.
    Notice that this is a shortcut, compared to the commented out code below.
    ModelSerializers also provide simple implementations for the create()
    and update() methods.
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet
        fields = (
            'id',
            'title',
            'code',
            'linenos',
            'language',
            'style',
            'owner'
        )

class UserSerializer(serializers.ModelSerializer):
    """
    Defines UserSerializer.
    """
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    
    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')



# class SnippetSerializer(serializers.Serializer):
#     """
#     Defines the fields that get serialized/deserialized.
#     """
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
#
#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Snippet.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance

# The serializer class is very similar to a Django `Form` class.
# It includes similar validation flags on the various fields, as well as how data should be displayed.
