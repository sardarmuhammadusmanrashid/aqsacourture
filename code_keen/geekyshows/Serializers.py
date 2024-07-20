from rest_framework import serializers
from .models import Student
class StudentSerilizers(serializers.Serializer):
    name=serializers.CharField(max_length=10)
    img=serializers.ImageField()
    def create(self,validate_data):
        instace=Student.objects.create(**validate_data)
        return instace
    def update(self,instance,validate_data):
        instance.name=validate_data.get('name',instance.name)
        instance.img=validate_data.get('img',instance.img)
        instance.save()
        return instance

    