from rest_framework import serializers
from django.utils.timesince import timesince
from ..models import Tweet # from tweets.models

from accounts.api.serializers import UserDsiplaySerializers


class TweetModelSerializer(serializers.ModelSerializer):

    user = UserDsiplaySerializers(read_only=True)
    date_display    = serializers.SerializerMethodField()
    timesince       = serializers.SerializerMethodField()

    class Meta:
        model = Tweet
        fields = [
            'user',
            'content',
            'timestamp',
            'date_display',
            'timesince'
        ]

    def get_date_display(self, obj):
        return obj.timestamp.strftime("%b %d %I: %M %p")

    def get_timesince(self, obj):
        return timesince(obj.timestamp) + " ago"