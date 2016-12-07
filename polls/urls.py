from django.conf.urls import url

from polls import views

urlpatterns = [
    # ex: /polls/home/
    url(r'^home$', views.home, name='home'),
    # ex: /polls/instructions/
    url(r'^instructions$', views.instructions, name='instructions'),
    # ex: /polls/install/
    url(r'^install$', views.install, name='install'),
    # ex: /polls/init/
    url(r'^init$', views.init, name='init'),
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
