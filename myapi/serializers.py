from rest_framework import  serializers
from .models import Questions

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Questions
        fields=('id','title','tags','description')