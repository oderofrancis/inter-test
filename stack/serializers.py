from rest_framework import serializers

from stack.models import Message, UserName

class MessageSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=200)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    def create(self, validated_data):
        return Message.objects.create(**validated_data)