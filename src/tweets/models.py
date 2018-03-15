from .validators import clean_content
from django.db import models
from django.urls import reverse

from django.contrib.auth import settings
User = settings.AUTH_USER_MODEL


class TweetManager(models.Manager):

    def retweet(self, user, parent_obj):
        obj = self.model(
            parent= parent_obj,
            user = user,
            content = parent_obj.content
        )
        obj.save()
        return obj


class Tweet(models.Model):
    parent      = models.ForeignKey("self", blank=True, null=True)
    user        = models.ForeignKey(User)
    content     = models.CharField(max_length=200, unique=True, validators=[clean_content])
    liked       = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="liked")
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    objects = TweetManager()

    def __str__(self):
        return str(self.content)

    def __unicode__(self): #python2
        return str(self.content)

    def get_absolute_url(self):
        return reverse("tweet:detail", kwargs={"pk":self.pk})
    # def clean(self, *args, **kwargs):
    #
    #     content = self.content
    #     if content == "abc":
    #         raise ValidationError("Cannot be ABC")
    #     return super(Tweet, self).clean(*args, **kwargs)