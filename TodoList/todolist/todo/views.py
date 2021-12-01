from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Todo, Category
from datetime import date, datetime, timezone


# Create your views here.
def display_todos(request):
    return render(request, 'display_all.html', {'todo': Todo.objects.all()})


def display_single_todo(request, id):
    msg = deadline_check(id)
    return render(request, 'display_single_task.html', {'todo': Todo.objects.get(id=id), 'msg': msg})


def todo(request):
    context = {
        'page_title': "Homepage",
        'form': ContactForm,
    }

    if request.method == "POST":
        form = ContactForm(request.POST)
        print("data", form.data)
        if form.is_valid():
            form_title = form.cleaned_data['title']
            form_details = form.cleaned_data['details']
            form_category = form.cleaned_data['category']
            context['formInfo'] = {
                'title': form_title,
                'details': form_details,
                'category': form_category
            }
            # context['btnFormHidden'] = True  # To hide the button is the form is successfully submitted
            # print the values to make sure their are correct
            print(context['formInfo'])
            print("cleaned data form is: ", form.cleaned_data)
            td = Todo.objects.create(**form.cleaned_data)
            return render(request, 'display_single_task.html', {'todo': Todo.objects.get(id=td.id)})
        else:
            print("---ERRORS---", form.errors)
            context['form'] = form
            return render(request, 'todo.html', context)
    else:
        # GET, generate blank form
        context['form'] = ContactForm()
    return render(request, 'todo.html', context)


def done_click(request, id, done_clicked):
    todo = Todo.objects.get(id=id)
    if done_clicked:
        todo.has_been_done = True
        todo.date_completion = date.today()
    else:
        todo.has_been_done = False
        todo.date_completion = None
    todo.save()
    return render(request, 'display_single_task.html', {'todo': Todo.objects.get(id=todo.id)})


def category_display(request, category):
    todo = Todo.objects.filter(category__name=category)
    return render(request, 'category_view.html', {'todo': todo})


def deadline_check(id):
    a = Todo.objects.get(id=id)
    msg = ""
    if not a.has_been_done:
        if (((a.deadline_date - datetime.now(timezone.utc)).days) < 0):
            msg="Deadline Elapsed"

        elif (((a.deadline_date - datetime.now(timezone.utc)).days) < 2):
            msg="Deadline approaching in 2 days"

        elif (((a.deadline_date - datetime.now(timezone.utc)).days) > 7):
            msg="Deadline approaching in a week"

    return msg

# print((a.deadline_date-datetime.now(timezone.utc)).days)
# print(a.deadline_date-date.today())
