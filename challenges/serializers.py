from rest_framework import serializers

from challenges.models import Challenge


class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = '__all__'


class ChallengePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = ['title', 'description', 'reward']
