from django.db import models
from django.conf import settings
# Create your models here.
from django.urls import reverse_lazy
from django.db.models.signals import post_save

class UserProfileManager(models.Manager):

    def all(self):
        qs = self.get_queryset().all()
        print(self)
        print(self.instance)
        try:
            if self.instance:
                qs = qs.exclude(user=self.instance)
        except:
            pass
        return qs

    def toggle_follow(self, user, to_toggle_user):
        toggle_user, created = UserProfile.objects.get_or_create(user=user)
        if self.request.user.is_authenticated():
            user_profile = UserProfile.objects.get_or_create(user=self.request.user)
            if toggle_user in user_profile.following.all():
                user_profile.following.remove(toggle_user)
                added = False
            else:
                user_profile.following.add(toggle_user)
                added = True
            return added

class UserProfile(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="profile")
    following = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="followed_by")

    objects = UserProfileManager # UserProfile.objects.all()
    abc = UserProfileManager() # UserProfile.abc.all()

    def __str__(self):
        return str(self.following.all().count())

    def get_following(self):
        users = self.following.all()
        return users.exclude(username=self.user.username)

    def get_follow_url(self):
        return reverse_lazy("profiles:follow", kwargs={"username": self.user.username})

    def get_absolute_url(self):
        return reverse_lazy("profiles:detail", kwargs={"username": self.user.username})




def post_save_user_receiver(sender, instance, created, *args, **kwargs):
    print(instance)
    if created:
        new_profile =   UserProfile.objects.get_or_create(user=instance)


post_save.connect(post_save_user_receiver, sender=settings.AUTH_USER_MODEL)