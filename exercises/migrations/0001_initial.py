# Generated by Django 5.0.3 on 2024-04-01 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название упражнения')),
                ('description', models.CharField(max_length=500, verbose_name='Описание')),
                ('type_exercise', models.CharField(choices=[('Кардио', 'Кардио'), ('Силовые', 'Силовые'), ('Растяжка', 'Растяжка'), ('Аэробика', 'Аэробика')], max_length=50, verbose_name='Тип упражнения')),
                ('difficulty', models.CharField(choices=[('Для начинающих', 'Для начинающих'), ('Средний', 'Средний'), ('Продвинутый', 'Продвинутый')], max_length=50, verbose_name='Уровень сложности')),
                ('duration', models.CharField(max_length=50, verbose_name='Продолжительность выполнения')),
                ('repeats', models.CharField(max_length=100, verbose_name='Количество повторений и подходов')),
            ],
        ),
    ]