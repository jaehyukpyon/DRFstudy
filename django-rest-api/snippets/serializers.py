from rest_framework import serializers

from snippets.models import Snippet


class SnippetSerializer(serializers.Serializer):
    """
    serializer 클래스의 첫 번째 부분은 serialize/deserialize되는 필드를 정의합니다.
    """
    
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    
    """
    The create() and update() methods define how fully fledged(필요한 자격을 다 갖춘da) instances are 
    created or modified when calling serializer.save()
    """
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        print('*** SnippetSerializer.create called.')
        print('*** SnippetSerializer.create - type(validated_data) > ', type(validated_data))
        print('*** SnippetSerializer.create - validated_data > ', validated_data)
        
        return Snippet.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        print('### SnippetSerializer.update called.')
        print('### SnippetSerializer.update - type(validated_data) > ', type(validated_data))
        print('### SnippetSerializer.update - validated_data > ', validated_data)
        
        print('### SnippetSerializer.update - type(instance) > ', type(instance))
        print('### SnippetSerializer.update - instance > ', instance)
        
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.save()
        return instance
    
    
class SnippetSerializer2(serializers.ModelSerializer):
    
    """
    It's important to remember that ModelSerializer classes don't do anything particularly magical, 
    they are simply a shortcut for creating serializer classes:
    1. An automatically determined set of fields.
    2. Simple default implementations for the create() and update() methods.
    """
    
    class Meta:
        model = Snippet
        fields = [
            'id',
            'title',
            'code',
            'created',
        ]
