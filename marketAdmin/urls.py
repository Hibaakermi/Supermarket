
from django.urls import path
from . import views as p_view
from .views import SearchView, contact_us


urlpatterns = [

  
    # for the user 
    path('vegs/',p_view.VegitableList.as_view(),name='vegs'),
    path('groc/',p_view.GroceryList.as_view(),name='groce'),
    path('search/',SearchView.as_view(), name='search'),
    path('contact/',contact_us, name='contact_us')


]
