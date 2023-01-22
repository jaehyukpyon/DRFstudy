from rest_framework import serializers
from datetime import datetime
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
        
class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField() 
    # CommentSerializer(data=data)로 JSON 데이터 넘길 때, 이메일 형식에 알맞지 않으면, serializer.is_valid()를 호출하면 바로 False return
    # serializers.errors > {'email': [ErrorDetail(string='Enter a valid email address.', code='invalid')]}
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()   
    mydate = serializers.HiddenField(
        default=datetime.now(),
    )
    
    def validate_email(self, value): # is_valid() 호출 시 이 메서드가 호출됨. validate 메서드보다 먼저 호출
        print('CommentSerializer - validated_email, type(value) > ', type(value)) # str
        print('CommentSerializer - validated_email, value > ', value) # 이메일 그 값 자체
        
        if 'egg' not in value.lower():
            raise serializers.ValidationError('egg is not included in email.')
        return value
    
    def validate_content(self, value): # is_valid() 호출 시 validate_email에서 error가 있더라도, validate_content 메서드도 무조건 실행된다.
        print('CommentSerializer - validate_content, type(value) > ', type(value)) # str
        print('CommentSerializer - validate_content, value > ', value) # content값 그 자체
        
        if 'django' not in value.lower():
            raise serializers.ValidationError('django is not included in content.')
        return value
    
    def validate_mydate(self, value):
        print('CommentSerializer - validate_mydate, type(value) > ', type(value)) 
        print('CommentSerializer - validate_mydate, value > ', value) # content값 그 자체
    
    def validate(self, data): # is_valid() 호출 시 이 메서드가 호출됨. validated_xxx보다 나중에 호출
        print('CommentSerializer - validate called...')
        print("data['email'] > ", data['email'])
        print("data['content'] > ", data['content'])
        print("data['created'] > ", data['created'])
        print('data > ', data) # OrderedDict
        return data # 반드시 validated 된 data를 return 해야 한다.
               