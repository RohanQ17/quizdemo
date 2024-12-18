# models.py
from django.db import models
import random


class Question(models.Model):
    text = models.TextField()
    correct_answer = models.CharField(max_length=255)
    option_two = models.CharField(max_length=255)
    option_three = models.CharField(max_length=255)
    option_four = models.CharField(max_length=255)

    def get_shuffled_options(self):
        """
        Returns a list of all options in a random order
        """
        options = [
            self.correct_answer,
            self.option_two,
            self.option_three,
            self.option_four
        ]
        random.shuffle(options)
        return options


    @classmethod
    def get_random_questions(cls, num_questions=5):
        """
        Use Django's built-in random ordering
        """
        return list(cls.objects.order_by('?')[:num_questions])

    def __str__(self):
        return self.text[:50]