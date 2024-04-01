from rest_framework.schemas.coreapi import serializers

from exercises.models import Exercise


class ExerciseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exercise
        fields = "__all__"
