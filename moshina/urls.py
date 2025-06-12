from  django.urls import path
from  .views import main, moshina_lst, moshina_info
urlpatterns = [
    path('', main, name='main'),
    path('moshina_lst/', moshina_lst, name='moshina_lst'),
    path('moshina_info/<int:id>', moshina_info, name='moshina_info'),
]