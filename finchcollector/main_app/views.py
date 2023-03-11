from django.shortcuts import render
from django.http import HttpResponse

class Finch:
   def __init__(self, name ,description, length, weight):
      self.name = name
      self.description = description
      self.length = length
      self.weight = weight


finches = [
  Finch('Brambling', 'black head, orange breast with white belly', '14cm', '24g'),
  Finch('Bullfinch', 'grey back, black cap and tail, and bright white rump', '14.5-16.5cm', '21-27g'),
  Finch('chaffinch', 'white on the wings and white outer tail feathers', '	18-29g', '18-29g'),
  Finch('siskin', 'streaky yellow-green body and a black crown and bib', '12cm','	12-18g'),
  Finch('Goldfinch', 'is a highly coloured finch with a bright red face and yellow wing patch', '12cm', '	14-19g'),

  ]

# Create your views here.
def home(request):
    # res.send in Express
    # return HttpResponse('<h1> finch Collector</h1>')
    return render(request, 'base.html')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
   return render(request, 'finches/index.html', {'finches': finches})
