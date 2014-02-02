# Create your views here.

from django.http import HttpResponse
from questionsandanswers.models import Question
from django.shortcuts import get_object_or_404, render_to_response

def index(request):
    questions = Question.objects.all()
#    response_string = "Questions <br/>"
#    response_string += '<br/>'.join(["id: %s, subject: %s" % (q.id, q.subject) for q in questions]) 
    return render_to_response('questionsandanswers/index.html', {'questions': questions})

def question_detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render_to_response('questionsandanswers/question_detail.html', {'question': question})
