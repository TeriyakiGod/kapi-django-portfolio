from django.forms import formset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from polls.forms import ChoiceForm, QuestionForm
from .models import Question, Choice


def index(request):
    latest_question_list = Question.objects.order_by("created_at")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})


def create(request):
    ChoiceFormSet = formset_factory(ChoiceForm, extra=3)
    if request.method == "POST":
        question_form = QuestionForm(request.POST)
        choice_formset = ChoiceFormSet(request.POST)
        if question_form.is_valid() and choice_formset.is_valid():
            question = question_form.save()
            for choice_form in choice_formset:
                if choice_form.cleaned_data.get("choice_text"):
                    choice = choice_form.save(commit=False)
                    choice.question = question
                    choice.save()
            return redirect("polls:index")
    else:
        question_form = QuestionForm()
        choice_formset = ChoiceFormSet()
    return render(
        request,
        "polls/create.html",
        {
            "question_form": question_form,
            "choice_formset": choice_formset,
        },
    )
