from urllib import request

from . models import User
#get_response是个方法
def from_user_middleware(get_response):
    print("这里是中间件初始化的一些代码")
    def middleware(request):
        print("这里是request到底view之前的代码")
        user_id = request.session.get('user_id')
        if user_id:
            try:
                user = User.objects.get(pk=user_id)
                request.front_user = user
            except:
                request.front_user = None
        # 这是一个界限，
        # #之前是view 之后是response到底浏览器
        response=get_response(request)

        print("这里是response到浏览器执行的代码")
        return  response

    return  middleware
