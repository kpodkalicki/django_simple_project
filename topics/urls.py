from django.conf.urls import url

from topics.views import TopicListView, TopicCreate, TopicUpdate, TopicDelete, TopicDetailView

urlpatterns = [
    url(r'^$', TopicListView.as_view(), name='topic-list'),
    url(r'^(?P<pk>\d+)/$', TopicDetailView.as_view(), name='topic-detail'),
    url(r'topic/add/$', TopicCreate.as_view(), name='topic-add'),
    url(r'topic/(?P<pk>[0-9]+)/$', TopicUpdate.as_view(), name='topic-update'),
    url(r'topic/(?P<pk>[0-9]+)/delete/$', TopicDelete.as_view(), name='topic-delete'),
]