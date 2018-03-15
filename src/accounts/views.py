from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView
# Create your views here.
from django.contrib.auth import get_user_model
from django.views import View
from .models import UserProfile
User = get_user_model()


class UserDetail(DetailView):

    template_name = "user_detail.html"
    queryset = User.objects.all()

    def get_object(self):
        return get_object_or_404(User, username__iexact=self.kwargs.get("username"))

    def get_context_data(self, **kwargs):
        context = super(UserDetail, self).get_context_data(*kwargs)
        context['following'] = UserProfile.objects.is_following(self.request.user, self.get_object())
        return context


class UserFollow(View):
    def get(self, username, *args, **kwargs):
        toggle_user = get_object_or_404(User, username__iexact=username)
        if self.request.user.is_authenticated():
            user_profile = UserProfile.objects.get_or_create(user=self.request.user)
            if toggle_user in user_profile.following.all():
                user_profile.following.remove(toggle_user)
            else:
                user_profile.following.add(toggle_user)
        return redirect("profile:detail", kwargs={"username": username})