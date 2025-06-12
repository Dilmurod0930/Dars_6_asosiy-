from  django.urls import path
from  .views import main, moshina_lst

urlpatterns = [
    path('', main, name='main'),
    path('moshina/', moshina_lst, name='moshina_lst'),
]