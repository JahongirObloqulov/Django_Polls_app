from django.shortcuts import render, HttpResponse, redirect
from .models import Question, Options


def question_list(request):
    questions = Question.objects.all()
    context = {
        "questions": questions
    }
    return render(request, 'questions.html', context)


def question_detail(request, question_id):
    ques = Question.objects.get(id=question_id)
    options = Options.objects.filter(question=ques)
    print(question_id, ques)
    print(options)
    context = {
        "question": ques,
        "options": options
    }

    return render(request, "detail.html", context)


def question_vote(request, question_id):
    print(question_id)
    option_id = request.GET.get('option')
    print(option_id)
    option = Options.objects.get(id=int(option_id))
    option.votes += 1
    option.save()
    return redirect('result', question_id)

def question_result(request, question_id):
    ques = Question.objects.get(id=question_id)
    options = Options.objects.filter(question=ques)
    context = {
        "question": ques,
        "options": options
    }

    return render(request, "result.html", context)

