from django.db import models


class ExerciseTypeChoices(models.TextChoices):
    CARDIO = "Кардио"
    POWER = "Силовые"
    STRETCHING = "Растяжка"
    AEROBICS = "Аэробика"


class ExerciseDifficultyChoices(models.TextChoices):
    EASY = "Для начинающих"
    MEDIUM = "Средний"
    HARD = "Продвинутый"


class Exercise(models.Model):
    name = models.CharField(max_length=64, verbose_name="Название упражнения")
    description = models.CharField(max_length=500, verbose_name="Описание")
    type_exercise = models.CharField(max_length=50, choices=ExerciseTypeChoices, verbose_name="Тип упражнения")
    difficulty = models.CharField(max_length=50, choices=ExerciseDifficultyChoices, verbose_name="Уровень сложности")
    duration = models.CharField(max_length=50, verbose_name="Продолжительность выполнения")
    repeats = models.CharField(max_length=100, verbose_name="Количество повторений и подходов")

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.name
