# Generated by Django 5.1.4 on 2024-12-18 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('correct_answer', models.CharField(max_length=255)),
                ('option_two', models.CharField(max_length=255)),
                ('option_three', models.CharField(max_length=255)),
                ('option_four', models.CharField(max_length=255)),
            ],
        ),
    ]
