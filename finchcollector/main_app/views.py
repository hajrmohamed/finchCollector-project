from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Finch , Toy # import finch from .models
from django.views.generic.edit import CreateView , DeleteView, UpdateView  # It effect the database so it's written edit 
from django.views.generic import ListView, DetailView  # because they will not effect the database so we don't write edit.
from .forms import FeedingForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
# Import the decorators for functional views only.
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

# class Finch:
#    def __init__(self, name ,description, length, weight):
#       self.name = name
#       self.description = description
#       self.length = length
#       self.weight = weight


# finches = [
#   Finch('Brambling', 'black head, orange breast with white belly', '14cm', '24g'),
#   Finch('Bullfinch', 'grey back, black cap and tail, and bright white rump', '14.5-16.5cm', '21-27g'),
#   Finch('chaffinch', 'white on the wings and white outer tail feathers', '	18-29g', '18-29g'),
#   Finch('siskin', 'streaky yellow-green body and a black crown and bib', '12cm','	12-18g'),
#   Finch('Goldfinch', 'is a highly coloured finch with a bright red face and yellow wing patch', '12cm', '	14-19g'),

#   ]

# Create your views here.
def home(request):
    # res.send in Express
    # return HttpResponse('<h1> finch Collector</h1>')
    return render(request, 'base.html')

def about(request):
  return render(request, 'about.html')

@login_required
def finches_index(request):
   finches =Finch.objects.filter(user=request.user)
   return render(request, 'finches/index.html', {'finches': finches_index})



def finch_detail(request,finch_id):
   # select * from  main_app_finch where id = finch_id
   finch = Finch.objects.get(id=finch_id)
    # Get the toys the finch doesn't have
   toys_finch_doesnt_have = Toy.objects.exclude(id__in = finch.toy.all().values_list('id')) #__in used to check if id exsist or not in finch.toys.all
   feeding_form = FeedingForm()
   return render(request, 'finches/detail.html', {
      'finch': finch,
      'feeding_form': feeding_form,
          # Add the toys to be displayed
      'toys': toys_finch_doesnt_have
      })



class FinchCreate(LoginRequiredMixin,CreateView):
   model = Finch
   fields =['name', 'description','length','weight']

   def form_valid(self, form):
       # self .request.user is logged user
       form.instance.user = self.user
      #  allows CreateView form_valid method to do it's normal work
       return super().form_valid(form)
  

class FinchUpdate(LoginRequiredMixin,UpdateView):
   model =  Finch
   fields = '__all__'

class FinchDelete(LoginRequiredMixin,DeleteView):
  model = Finch
  success_url = '/finches/'

# add_feeding
def add_feeding(request, finch_id):
    form = FeedingForm(request.POST) #request.POST is whatever enterd in the form we r saving it in a variable form.
    if form.is_valid():
        new_feeding = form.save(commit=False) #this save is like in memory only and returning
        new_feeding.finch_id = finch_id
        new_feeding.save() #this save actually saving it in db
    return redirect('detail', finch_id=finch_id)

class ToyList(LoginRequiredMixin,ListView):
    model = Toy

class ToyDetail(LoginRequiredMixin,DetailView):
    model = Toy

class ToyCreate(LoginRequiredMixin,CreateView):
    model = Toy
    fields = '__all__'

class ToyUpdate(LoginRequiredMixin,UpdateView):
    model = Toy
    fields = ['name', 'color']

class ToyDelete(LoginRequiredMixin,DeleteView):
    model = Toy
    success_url = '/toys/'

def assoc_toy(request,finch_id, toy_id):
    Finch.objects.get(id=finch_id).toy.add(toy_id)
    return redirect('detail', finch_id=finch_id)

def unassoc_toy(request,finch_id, toy_id):
    Finch.objects.get(id=finch_id).toy.remove(toy_id)
    return redirect('detail', finch_id=finch_id)


# when user submit the signup form this function will run.
# after signup it will take me direct to login function and then to the home page.
def signup(request):
    error_message = ''
    if request.method =='POST':
        # Make a 'user' form object with the data from the browser
        form = UserCreationForm(request.POST)

        if form.is_valid():
            # save user to DB
            user = form.save()

        # login function but we have to import it
            login(request, user)
            return redirect('index')

        else: 
            error_message = 'Invalid: Please Try Again! '

    # If there's a bad post or get request
    form = UserCreationForm()
    context = {'form': form, 'error_message':error_message}
    return render(request, 'registration/signup.html', context)
        