"""day01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path,include  #主url 包裹 应用的url 先把include导入归来
# from jxlg01.views import book
# from jxlg02.views import index
# from django.http import HttpResponse
from jxlg01 import views

# def test(request):
#     return HttpResponse('直接在主url中写视图,这种方式不建议用，代码太冗余')

urlpatterns = [
    # path('book/',views.book),
    # path('book_detail/',views.book_detail),
    # path('books_detail/<uuid:book_id>/<path:category_id>/',views.books_detail),
    # path('',index),
    # path('test/',test),
    path('book/',include('jxlg01.urls'))
    #访问的时候  该模块的前缀

]
