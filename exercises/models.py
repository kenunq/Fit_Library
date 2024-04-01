from django.db import models


class Exercise(models.Model):
    EXERCISE_TYPE_CHOICES = (
        ("Кардио", "Кардио"),
        ("Силовые", "Силовые"),
        ("Растяжка", "Растяжка"),
        ("Аэробика", "Аэробика"),
    )
    EXERCISE_DIFFICULTY_CHOICES = (
        ("Для начинающих", "Для начинающих"),
        ("Средний", "Средний"),
        ("Продвинутый", "Продвинутый"),
    )
    name = models.CharField(max_length=64, verbose_name="Название упражнения")
    description = models.CharField(max_length=500, verbose_name="Описание")
    type_exercise = models.CharField(max_length=50, choices=EXERCISE_TYPE_CHOICES, verbose_name="Тип упражнения")
    difficulty = models.CharField(max_length=50, choices=EXERCISE_DIFFICULTY_CHOICES, verbose_name="Уровень сложности")
    duration = models.CharField(max_length=50, verbose_name="Продолжительность выполнения")
    repeats = models.CharField(max_length=100, verbose_name="Количество повторений и подходов")

    def __str__(self):
        return self.name
