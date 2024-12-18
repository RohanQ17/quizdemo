from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .models import Question

# Create your views here.
def home(request):
    return render(request,'home.html')




def start_quiz(request):
    """
    Initialize the quiz session
    """
    # Get 5 random questions
    questions = list(Question.get_random_questions())

    # Store quiz details in session
    request.session['quiz_questions'] = [q.id for q in questions]
    request.session['current_question_index'] = 0
    request.session['user_answers'] = []

    # Redirect to first question
    return redirect('quiz_question')


def quiz_question(request):
    """
    Display current quiz question
    """
    # Retrieve quiz details from session
    quiz_question_ids = request.session.get('quiz_questions', [])
    current_index = request.session.get('current_question_index', 0)

    # Check if quiz is complete
    if current_index >= len(quiz_question_ids):
        return redirect('quiz_result')

    # Get current question
    current_question = Question.objects.get(id=quiz_question_ids[current_index])
    options = current_question.get_shuffled_options()

    return render(request, 'quiz_question.html', {
        'question': current_question,
        'options': options,
        'question_number': current_index + 1,
        'total_questions': len(quiz_question_ids)
    })


@require_http_methods(["POST"])
def submit_answer(request):
    """
    Process answer submission
    """
    # Retrieve quiz details from session
    quiz_question_ids = request.session.get('quiz_questions', [])
    current_index = request.session.get('current_question_index', 0)
    user_answers = request.session.get('user_answers', [])

    # Get current question
    current_question = Question.objects.get(id=quiz_question_ids[current_index])

    # Get user's answer
    selected_answer = request.POST.get('answer')

    # Store user's answer
    user_answers.append({
        'question_id': current_question.id,
        'selected_answer': selected_answer,
        'correct_answer': current_question.correct_answer,
        'is_correct': selected_answer == current_question.correct_answer
    })

    # Update session
    request.session['user_answers'] = user_answers
    request.session['current_question_index'] = current_index + 1

    # Move to next question or result
    if current_index + 1 < len(quiz_question_ids):
        return redirect('quiz_question')
    else:
        return redirect('quiz_result')


def quiz_result(request):
    """
    Display quiz results
    """
    # Retrieve user answers from session
    user_answers = request.session.get('user_answers', [])

    # Calculate score
    correct_answers = sum(1 for answer in user_answers if answer['is_correct'])
    total_questions = len(user_answers)
    score_percentage = (correct_answers / total_questions) * 100 if total_questions > 0 else 0

    # Prepare detailed results
    results = []
    for answer in user_answers:
        question = Question.objects.get(id=answer['question_id'])
        results.append({
            'question_text': question.text,
            'selected_answer': answer['selected_answer'],
            'correct_answer': answer['correct_answer'],
            'is_correct': answer['is_correct']
        })

    # Clear session
    request.session.flush()

    return render(request, 'quiz_result.html', {
        'correct_answers': correct_answers,
        'total_questions': total_questions,
        'score_percentage': score_percentage,
        'results': results
    })

