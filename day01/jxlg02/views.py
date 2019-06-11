from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('临渊羡鱼,不如退而抱你')
