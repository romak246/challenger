from django.contrib import admin
from django.urls import path

from challenges.views import ChallengeAPIView, ChallengeItemAPIView, index, create_challenge, new_challenge

urlpatterns = [
    path('admin/', admin.site.urls),
    path('challenge/', ChallengeAPIView.as_view()),
    path('challenge/<pk>', ChallengeItemAPIView.as_view()),
    path("", index),
    path("create_challenge", create_challenge),
    path("new_challenge", new_challenge),

]
