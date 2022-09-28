from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from challenges.models import Challenge
from challenges.serializers import ChallengeSerializer, ChallengePostSerializer


class ChallengeAPIView(APIView):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer

    def get(self, request):
        challenges = Challenge.objects.all()
        serializer = self.serializer_class(challenges, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request):
        serializer = ChallengePostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ChallengeItemAPIView(APIView):
    @staticmethod
    def get(request, pk):
        challenge = Challenge.objects.get(id=pk)
        serializer = ChallengeSerializer(challenge, many=False)
        return Response(serializer.data)

    @staticmethod
    def delete(request, pk):
        challenge = Challenge.objects.get(id=pk)
        challenge.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @staticmethod
    def put(request, pk):
        challenge = Challenge.objects.get(id=pk)
        serializer = ChallengeSerializer(challenge, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
