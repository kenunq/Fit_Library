from django.contrib import admin

from exercises.models import Exercise


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ("name", "type_exercise", "difficulty")
    search_fields = ("name",)
    list_filter = ("type_exercise", "difficulty")
