from rest_framework import serializers
from .models import Todo

class TodoSimpleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Todo
        fields = ('id', 'title', 'complete', 'important')
        
# TodoSimpleSerializer():
#     id = IntegerField(label='ID', read_only=True)
#     title = CharField(max_length=200)
#     complete = BooleanField(required=False)      
#     important = BooleanField(required=False)   


class TodoDetailSerializer(serializers.ModelSerializer):
    
    def validate_id(self, value):
        print('### TodoDetailSerializer - validate_id called.')
        print('### TodoDetailSerializer - validate_id, value > ', value)
        
    def validate(self, data):
        print('TodoDetailSerializer - validate called.')
        for key, value in data.items():
            print(f'@@@ key: {key}, value: {value}')
    
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'created', 'complete', 'important')
        
# TodoDetailSerializer():
#     id = IntegerField(label='ID', read_only=True)
#     title = CharField(max_length=200)
#     description = CharField(allow_blank=True, required=False, style={'base_template': 'textarea.html'})
#     created = DateTimeField(read_only=True)
#     complete = BooleanField(required=False)
#     important = BooleanField(required=False)


class TodoCreateSerializer(serializers.ModelSerializer):
    
    comment_count = serializers.SerializerMethodField()
    def get_comment_count(self, obj):
        # 이 메서드는 post나 put deserialization의 validation할 때 끼어들지 않는다.
        # 또한, validate_xxx및 validate 메서드가 다 호출 된 이후 가장 마지막에 호출된다. 
        print('type(obj) >> ', type(obj)) # type(obj) >>  <class 'todo.models.Todo'>
        return 'Hello World!'
    
    # important = serializers.BooleanField(required=False, default=True) # important = BooleanField(default=True, required=False) 
    #important = serializers.BooleanField(allow_null=True, required=False) # important = BooleanField(allow_null=True, required=False) 이렇게 설정해줘도 post시 사용자가 값을 안 보내도 validate_important실행되고, validate 메서드 안에 important정보가 포함된다.
    important = serializers.BooleanField(required=False)
    def validate_important(self, value): # POSt 요청 시 important를 body에 포함하지 않아도 무조건 호출된다. 값은 False
        print('### TodoCreateSerializer - validate_important called.')
        print('### TodoCreateSerializer - validate_important, value > ', value)
        return value
    
    # testtext = serializers.CharField(required=False)
    # def validate_testtext(self, value): # important 필드와 다르게, POST 요청 시 body에 포함되지 않으면 호출되지 않는다. validate 메서드에서도 key, value에서 testtext 관련 정보는 나오지 않는다. 
    #     print('### TodoCreateSerializer - validate_testtext called.')
    #     print('### TodoCreateSerializer - validate_testtext, value > ', value)
    #     return value
    
    def validate_description(self, value):
        print('&&& TodoCreateSerializer - valid_description called.')
        print('&&& TodoCreateSerializer - valid_description, value > ', value)
        return value
        
    def validate(self, data):
        print('TodoDetailSerializer - validate called.')
        for key, value in data.items():
            print(f'@@@ key: {key}, value: {value}')
        return data
# @@@ key: title, value: DRF공부하기
# @@@ key: description, value: 책 보며 DRF 공부하기
# @@@ key: important, value: True # POST 요청 시 important를 body에 포함하지 않아도 무조건 호출. 값은 False
    
    class Meta:
        model = Todo
        fields = ('title', 'description', 'important', 'comment_count')
        extra_kwargs = { 
            'important': # 만약 important가 명시적으로 serializer 클래스 안에 필드로 선언 돼 있다면, extra_kwargs에서 설정한 important에 대한 내용은 무시된다.
                {
                    'required': False,
                    'allow_null': True,
                },
        }
        # fields = '__all__' # 이런식으로 하면, comment_count도 추가적으로 포함 된다. comment_count = SerializerMethodField()
        
#     TodoCreateSerializer():
# title = CharField(max_length=200)
# description = CharField(allow_blank=True, required=False, style={'base_template': 'textarea.html'}) # 만약 POST, PUT(수정)요청 시 사용자가 body에 description을 포함하지 않는다면 validate_description는 호출되지 않으며 validate 메서드의 data 딕셔너리 안에 description 관련 정보는 포함되지 않는다.
# important = BooleanField(required=False) 이 부분의 경우, models의 BooleanField(default=True) default와 상관 없이 사용자가 값을 보내지 않는다면 무조건 False가 기본 값인 것 같다. 
# testtext = CharField(required=False) 임의로 추가해본 testtext 필드는 이런 식으로 나온다.

