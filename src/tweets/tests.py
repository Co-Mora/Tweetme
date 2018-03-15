from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.
from django.urls import reverse
from .models import Tweet

User = get_user_model()


class TweetModelTest(TestCase):

    def setUp(self):
        some_random_user = User.objects.create(username="omarahmed")

    def test_tweet_item(self):
        obj = Tweet.objects.create(
            user=User.objects.first(),
            content="Some Content"
        )
        self.assertTrue(obj.content == "Some Content")
        self.assertTrue(obj.id == 1)
        absolute_url = reverse("tweet:detail", kwargs={"pk": 1})
        self.assertEqual(obj.get_absolute_url(), absolute_url)


    def test_tweet_url(self):
        obj = Tweet.objects.create(
            user=User.objects.first(),
            content="Some Content"
        )
        absolute_url = reverse("tweet:detail", kwargs={"pk": obj.pk})
        self.assertEqual(obj.get_absolute_url(), absolute_url)