from django.urls import path
from . import views
	
urlpatterns = [
	    #Routes in Express, URLs in Django
	    # '' means its route
	    path('',views.home, name = 'home'),
        path('about/',views.about, name ='about' ),
        path('finches/', views.finches_index, name ='index' ),
    path('finches/<int:finch>', views.finch_detail, name='detail'),
    path('finches/create/', views.FinchCreate.as_view(), name='finches_create'),
    path('finches/<int:pk>/update', views.FinchUpdate.as_view(), name='finches_update'), 
    path('finches/<int:pk>/delete', views.FinchDelete.as_view(), name='finches_delete'),
    path('finches/<int:finch>/add_feeding' , views.add_feeding , name='add_feeding'),

# URLs for Toys CRUD Operations
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/<int:pk>', views.ToyDetail.as_view(), name='toys_detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),

    #Associate a toy with a finch (M:M)
    path('finches/<int:finch>/assoc_toy/<int:toy_id>', views.assoc_toy, name='assoc_toy'),

    # Unassociate a toy from a finch(M:M)
    path('finches/<int:finch>/unassoc_toy/<int:toy_id>', views.unassoc_toy, name='unassoc_toy'),

    path('accounts/signup', views.signup, name = 'signup')
]

