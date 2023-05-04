from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Book


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'Books/book_detail.html', {'book': book})



def demo(request):
    return HttpResponse("This is demo page")