from django.shortcuts import render,redirect
from .forms import ContactForm
from .models import Todo, Category

# Create your views here.
def display_todos (request):
    return render(request,'display_all.html', {'todo':Todo.objects.all()})

def display_single_todo(request,id):
    print(id)
    return render(request, 'display_single_task.html', {'todo': Todo.objects.get(id=id)})

def todo(request):
    context = {
        'page_title': "Homepage",
        'form': ContactForm,
    }

    if request.method=="POST":
        form=ContactForm(request.POST)
        print("data",form.data)
        if form.is_valid():
            form_title = form.cleaned_data['title']
            form_details = form.cleaned_data['details']
            form_category = form.cleaned_data['category']
            context['formInfo'] = {
                'title': form_title,
                'details': form_details,
                'category': form_category
            }
            #context['btnFormHidden'] = True  # To hide the button is the form is successfully submitted
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
