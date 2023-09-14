from rest_framework import serializers
from aws_app.models import aws_app, LANGUAGE_CHOICES, STYLE_CHOICES

class awsSerializer(serializers.ModelSerializer):
    class Meta:
        model = aws_app
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']

    def create(self, validated_data):
        return aws_app.objects.create(**validated_data)
    def update(self, instance, validate_data):
        instance.title = validate_data.get('title', instance.title)
        instance.code = validate_data.get('code', instance.code)
        instance.linenos = validate_data.get('linenos', instance.linenos)
        instance.style = validate_data.get('style', instance.style)
        instance.save()
        return instance