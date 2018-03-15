from django.views.generic.base import RedirectView
from django.conf.urls import url
from .views import (
     TweetListAPIView,
    TweetCreateAPIView
)
urlpatterns = [
    # url(r'^$', RedirectView.as_view(url='/'), name="create"),  # /tweet/create
    #
    url(r'^create/$', TweetCreateAPIView.as_view(), name="create"),  # /tweet/create
    url(r'^$', TweetListAPIView.as_view(), name="list")# api/tweet/
    # url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name="update"),  # tweet/update/id
    # url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name="delete"),  # tweet/update/id
    # url(r'^(?P<pk>\d+)/$', TweetDetailsView.as_view(), name="detail"),  # tweet/id

]
