from rest_framework import serializers
from jhgjhg.models import JHgjhg


class JHgjhgSerializer(serializers.ModelSerializer):
    class Meta:
        model = JHgjhg
        fields = "__all__"
