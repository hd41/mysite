from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.http import JsonResponse

from .models import Question, Choice
# Create your views here.

def main_index(request):
    return render(request, 'polls/index.html', context)

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def jsonResp(request):
    if request.method == 'POST':
        question = get_object_or_404(Question, pk=int(request.POST.get('param')))
        if True:
            selected_choice = question.choice_set.get(pk=request.POST['opt'])
            print(selected_choice)
            selected_choice.votes += 1
            selected_choice.save()
            context={}
            for ch in question.choice_set.all():
                context[ch.choice_text]=ch.votes
            return JsonResponse(context)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def addQuestion(request):
    return render(request,'polls/question_insertion.html')

def submitForm(request):
    if request.method == 'POST':
        question_text = request.POST.get('ques')
        q = Question(question_text= question_text, pub_date= timezone.now())
        q.save()
        n_choice  = request.POST.get('choice_n')
        print ('n_choice ',n_choice)
        for i in range(int(n_choice)):
            if request.POST.get('ip'+str(i+1)):
                q.choice_set.create(choice_text=request.POST.get('ip'+str(i+1)))

    return HttpResponseRedirect(reverse('polls:index'))
