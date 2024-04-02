from django.shortcuts import render
from django.views import View
from .models import Book


class  BookListView(View):
    def get(self,request):
        books=Book.objects.all()
        return render(request,'kitoblar/book_list.html',{'books':books})

# def detail(request,id):
#     book=Book.objects.get(id=id)
#     return render(request,'kitoblar/detail.html',{'book':book})
