from django.urls import path
from .views import BookListView

app_name = 'kitoblar'

urlpatterns = [
    path('list/', BookListView.as_view(), name='book_list'),
]
