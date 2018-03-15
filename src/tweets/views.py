from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Tweet
from django.db.models import Q

from django.urls import reverse_lazy
from django.views.generic import (
    DetailView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView

)
from .forms import TweetModelForm
from .mixins import UserFormMixin, UserOwner
from django.contrib.auth.mixins import LoginRequiredMixin


class TweetCreateView(LoginRequiredMixin, UserFormMixin, CreateView):

    form_class = TweetModelForm
    template_name = "tweets/create_view.html"
    #success_url = '/tweet/'
    login_url = '/admin/'


class TweetUpdateView(LoginRequiredMixin, UserOwner, UserFormMixin, UpdateView):

    model = Tweet
    form_class = TweetModelForm
    template_name = "tweets/update_view.html"
    #success_url = '/tweet/'
    login_url = '/admin/'


class TweetDeleteView(LoginRequiredMixin, UserOwner, DeleteView):

    model = Tweet
    template_name = "tweets/delete_view.html"
    #success_url = reverse_lazy("tweet:list")


class TweetDetailsView(DetailView):
    queryset = Tweet.objects.all()
    template_name = "tweets/detail_view.html"
    #
    # def get_object(self):
    #     print(self.kwargs)
    #     pk = self.kwargs.get('pk')
    #     obj = get_object_or_404(Tweet, pk=pk)
    #     return obj


#CLASS_BASE_VIEWS
class TweetListView(ListView):

    template_name = "tweets/list_view.html"
    queryset = Tweet.objects.all()

    def get_queryset(self, *args, **kwargs):
        qs = Tweet.objects.all()
        print(self.request.GET)
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
            )
        return qs

    def get_context_data(self, **kwargs):
        context = super(TweetListView, self).get_context_data(**kwargs)
        context['now'] = Tweet.objects.all()
        context['create_form'] = TweetModelForm()
        context['create_url'] = reverse_lazy('tweet:create')
        return context

