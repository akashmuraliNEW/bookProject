from django.shortcuts import render,redirect
from .models import *
# Create your views here.



def homePage(request):
    author = Author.objects.all()
    # print('creating ..')
    if request.method =='POST':
        title = request.POST['title']
        price = request.POST['price']
        image = request.FILES['image']
        author_name = request.POST['author']
        author_obj = Author.objects.get(author=author_name)
        obj = Book.objects.create(title=title, price=price, author=author_obj,image=image)
        obj.save()
        # print('done../')
        return redirect('display')
    return render(request, 'admin/home.html', {'author': author})


def display_books(request):
    books = Book.objects.all()
    return render(request,'admin/display_books.html',{'book':books})

def update_books(request,id):
    author = Author.objects.all()
    book = Book.objects.get(id=id)
    # print(book)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.image = request.POST['image']
        print(book.title)
        book.price = request.POST['price']
        author_name = request.POST['author']
        author_obj = Author.objects.get(author=author_name)
        book.author = author_obj
        book.save()
        return redirect('display')
    return render(request, 'admin/update_book.html', {'book': book, 'author': author})


def delete_book(request,id):
    author = Author.objects.all()
    book = Book.objects.get(id=id)
    book.delete()
    
    return render(request,'admin/delete_book.html', {'book':book,'author':author})
    
