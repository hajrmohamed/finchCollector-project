from django.urls import path
from . import views
	
urlpatterns = [
	    #Routes in Express, URLs in Django
	    # '' means its route
	    path('',views.home, name = 'home'),
        path('about/',views.about, name ='about' ),
        path('finches/', views.finches_index, name ='index' )
]