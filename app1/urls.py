"""parakh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings

from django.conf.urls.static import static
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('',views.first, name='first'),
    path('login',  views.login, name='login'),
    path('choose_avatar',  views.choose_avatar, name='choose_avatar'),
    path('select_profile', views.select_profile, name='select_profile'),
    path('language', views.language, name='language'),
    path('start_assesment', views.start_assesment, name='start_assesment'),
    path('paragraph', views.paragraph, name='paragraph'),
    # path('recording_para', views.recording_para, name='recording_para'),
    path('start_recording', views.start_recording, name='start_recording'),
    path('answer/<str:text>/', views.answer, name='answer'),
    path('answer', views.answer, name='answer'),
    path('next_page', views.next_page, name='next_page'),
    path('next_para', views.next_para, name='next_para'),
    path('story', views.story, name='story'),
    path('story_recording', views.story_recording, name='story_recording'),
    path('story_answer/<str:text>/', views.story_answer, name='story_answer'),
    path('story_answer', views.story_answer, name='story_answer'),
    path('next_story', views.next_story, name='next_story'),
    path('thirteen', views.thirteen, name='thirteen'),
    path('fourteen', views.fourteen, name='fourteen'),
    path('word', views.word, name='word'),
    path('word_recording', views.word_recording, name='word_recording'),
    path('word_answer', views.word_answer, name='word_answer'),
    path('next_word', views.next_word, name='next_word'),
    path('retake_word', views.retake_word, name='retake_word'),
    path('retake_word2', views.retake_word2, name='retake_word2'),
    path('retake_word3', views.retake_word3, name='retake_word3'),
    path('retake_word4', views.retake_word4, name='retake_word4'),
    path('retake_word5', views.retake_word5, name='retake_word5'),
    path('letter', views.letter, name='letter'),
    path('letter_recording', views.letter_recording, name='letter_recording'),
    path('letter_answer', views.letter_answer, name='letter_answer'),
    path('next_letter', views.next_letter, name='next_letter'),
    path('retake_letter', views.retake_letter, name='retake_letter'),
    path('retake_letter2', views.retake_letter2, name='retake_letter2'),
    path('retake_letter3', views.retake_letter3, name='retake_letter3'),
    path('retake_letter4', views.retake_letter4, name='retake_letter4'),
    path('retake_letter5', views.retake_letter5, name='retake_letter5'),
    path('seventeen', views.seventeen, name='seventeen'),
    path('next_answer', views.next_answer, name='next_answer'),
    path('word_msg', views.word_msg, name='word_msg'),
    path('word_ltr', views.word_ltr, name='word_ltr'),
    path('word_beg', views.word_beg, name='word_beg'),
    # path('home',views.home, name='home'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
