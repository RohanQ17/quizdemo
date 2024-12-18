from django.core.management.base import BaseCommand
from quiz.models import Question


class Command(BaseCommand):
    help = 'Load predefined questions into the database'

    def handle(self, *args, **kwargs):
        # Optional: Clear existing questions
        Question.objects.all().delete()

        # Define your questions
        questions_data = [
            {
                "text": "What is the capital of France?",
                "correct_answer": "Paris",
                "option_two": "London",
                "option_three": "Berlin",
                "option_four": "Madrid"
            },
            {
                "text": "Which nation won the football world cup in 2010?",
                "correct_answer": "spain",
                "option_two": "france",
                "option_three": "netherlands",
                "option_four": "portugal"
            },
            {
                "text": "Which planet is known as the Red Planet?",
                "correct_answer": "Mars",
                "option_two": "Venus",
                "option_three": "Jupiter",
                "option_four": "Saturn"
            },
            {
                "text": "Which of these is not a space constellation?",
                "correct_answer": "Proxima B",
                "option_two": "Ursa Major",
                "option_three": "Orion",
                "option_four": "Big Dipper"
            },
            {
                "text": "Capital city of Japan is",
                "correct_answer": "Tokyo",
                "option_two": "Osaka",
                "option_three": "Kyoto",
                "option_four": "Sapporo"
            }
            # Add more questions here
        ]

        # Create questions
        created_count = 0
        for question_info in questions_data:
            Question.objects.create(**question_info)
            created_count += 1

        # Provide feedback
        self.stdout.write(
            self.style.SUCCESS(f'Successfully loaded {created_count} questions')
        )