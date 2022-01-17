from django.urls import path
from .views import Booklist,Post_Booklist,Update_Booklist,Delete_Booklist

urlpatterns = [
    path('',Booklist),
    path('add/',Post_Booklist),
    path('update/<int:id>/',Update_Booklist),
    path('delete/<int:id>',Delete_Booklist),
]