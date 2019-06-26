from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.db import connection
# Create your views here.
def get_cursor():
    return connection.cursor()


def index(request):
    cursor = get_cursor()
    cursor.execute("select * from book")
    books= cursor.fetchall()
    return render(request,'index.html',context={"books":books})

def add_book(request):
    #第一步渲染页面
    if request.method == 'GET':
        return render(request,'add_book.html')
    #第二步提交表单数据
    else:
        name = request.POST.get('bookname')
        author = request.POST.get('author')
        cursor = get_cursor()
        if cursor.execute("insert into book(name,author) values('%s','%s') " % (name,author)):
            return redirect(reverse('index'))
        else:
            return HttpResponse("添加失败")
def book_detail(request,book_id):
    cursor = get_cursor()
    cursor.execute("select * from book where id=%s" % book_id)
    books = cursor.fetchone()
    return render(request, 'book_detail.html', context={"books": books})


def delete_book(request):
    #接收提交过来的 book id
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        cursor = get_cursor()
        if cursor.execute("delete * from book where id=%s" % book_id):
            return redirect(reverse('index'))
        else:
            raise RuntimeError("您还没有删除的权限请联系91wangfan")


