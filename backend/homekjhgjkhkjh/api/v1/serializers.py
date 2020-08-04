from rest_framework import serializers
from homekjhgjkhkjh.models import Hgjh


class HgjhSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hgjh
        fields = "__all__"
