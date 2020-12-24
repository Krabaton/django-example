from django.conf.urls import url
from . import views

urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),
    # Render all topics
    url(r'^topics/$', views.topics, name='topics'),
    # Inform for topic
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    # add new topic
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    # добавление новой записи
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    # редактирование записи
    url(r'edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
    # url('edit_entry/<entry_id>/', views.edit_entry, name='edit_entry'),
]
