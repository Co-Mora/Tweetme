from django.views.generic.base import RedirectView
from django.conf.urls import url
from .views import (
    UserDetail
)
urlpatterns = [
    # url(r'^$', RedirectView.as_view(url='/'), name="create"),  # /tweet/create
    # url(r'^create/$', TweetCreateView.as_view(), name="create"),  # /tweet/create
    # url(r'^search/$', TweetListView.as_view(), name="list"), #/tweet/
    # url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name="update"),  # tweet/update/id
    # url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name="delete"),  # tweet/update/id
    url(r'^(?P<username>[\w.@+-]+)/$', UserDetail.as_view(), name="detail"),  # tweet/id

]
