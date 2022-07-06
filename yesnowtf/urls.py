from django.urls import path, include, re_path

from yesnowtf import views


urlpatterns = [
    path(r'question/', views.QuestionView.as_view()),
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
