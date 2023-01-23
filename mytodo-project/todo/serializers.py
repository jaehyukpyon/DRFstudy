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
