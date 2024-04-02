from django .shortcuts import  render
from kitoblar.models import Book
def landing_page(request):
    kitob=Book.objects.all()
    return render(request, 'landing.html',context={'books':kitob})
