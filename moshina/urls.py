from  django.urls import path
from  .views import main, moshina_lst, moshina_info, moshina_update
urlpatterns = [
    path('', main, name='main'),
    path('moshina/', moshina_lst, name='moshina_lst'),
    path('moshina/<int:id>/', moshina_info, name='moshina_info'),
    path('moshina_update/<int:id>/', moshina_update, name='moshina_update'),

]