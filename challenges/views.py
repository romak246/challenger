from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from challenges.models import Challenge
from challenges.serializers import ChallengeSerializer, ChallengePostSerializer
from django.shortcuts import redirect


class ChallengeAPIView(APIView):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer

    def get(self, request):
        """Вывод списка всех челленджей"""
        challenges = Challenge.objects.all()
        serializer = self.serializer_class(challenges, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request):
        """Публикация челленджа"""
        serializer = ChallengePostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ChallengeItemAPIView(APIView):
    @staticmethod
    def get(request, pk):
        """Получить челлендж по id"""
        challenge = Challenge.objects.get(id=pk)
        serializer = ChallengeSerializer(challenge, many=False)
        context = {'title': challenge.title, 'reward': challenge.reward, 'date': challenge.date, 'description':challenge.description }
        # return Response(serializer.data)
        return render(request, "challenge.html", context)

    @staticmethod
    def delete(request, pk):
        """Удалить челлендж"""
        challenge = Challenge.objects.get(id=pk)
        challenge.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @staticmethod
    def put(request, pk):
        """Редактировать челлендж"""
        challenge = Challenge.objects.get(id=pk)
        serializer = ChallengeSerializer(challenge, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)



def index(request):
    challenges = Challenge.objects.all()
    output = list()
    for challenge in challenges:
        res = dict()
        res['id'] = challenge.id
        res['title'] =challenge.title
        res['description'] = challenge.description
        res['reward'] = challenge.reward
        output.append(res)


    context =  {"challenges": output, "test":'ok'}
    return render(request, "main.html", context)



def create_challenge(request):

    return render(request, "create_challenge.html")

def new_challenge(request):
    data = request.POST
    challenge = Challenge.objects.create(title=data['title'],  reward = data['reward'], description = data['description'] )
    context = {'title': challenge.title, 'reward': challenge.reward, 'date': challenge.date,
               'description': challenge.description}
    # return Response(serializer.data)
    return render(request, "challenge.html", context)


