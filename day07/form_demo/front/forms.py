from django import forms
from django.core import validators
from .models import  User

class BaseForm(forms.Form):
    def get_errors(self):
        #拿到后台错误信息
        errors=self.errors.get_json_data()
        new_errors={}
        #对错误信息字典中每一个部分进行遍历
        #{'telephone','15236手机号格式错误'
        for key,message_dicts in errors.items():
            messages=[]
           # print(message_dicts)
            for message_dict in message_dicts:
                message=message_dict['message']
                messages.append(message)
            new_errors[key] =messages
        return new_errors


class MessageBoardForm(forms.Form):
    title=forms.CharField(max_length=100,min_length=6,label="标题",error_messages={"min_length":"最少不少于6字符"})
    content=forms.CharField(widget=forms.Textarea,label="内容",error_messages={"required":"必须要写content"})
    email=forms.EmailField(label="邮箱",error_messages={"required":"必须传入email字段"})
    reply=forms.BooleanField(required=False,label="是否回复")

class RegisterForm(BaseForm):
    username=forms.CharField(max_length=100)
    email=forms.CharField(validators=[validators.EmailValidator(message="请输入正确格式邮箱")])
    telephone=forms.CharField(validators=[validators.RegexValidator(r'1[345678]\d9',message="请输入正确的手机格式")])
    pwd1=forms.CharField(max_length=20,min_length=6)
    pwd2=forms.CharField(max_length=20,min_length=6)
    #额外验证手机号
    def clean_telephone(self):
        telephone=self.cleaned_data.get('telephone')
        exists=User.objects.filter(telephone=telephone).exists()
        #exists是否存在 返回值true
        if exists:
            raise  forms.ValidationError(message="%s:已经注册" %telephone)
        return telephone
    #如果走到这里，说明所有的字段验证成功
    def clean(self):
        cleaned_data=super(RegisterForm,self).clean()
        pwd1=cleaned_data.get('pws1')
        pwd2=cleaned_data.get('pws2')
        if pwd1 != pwd2:
            raise  forms.ValidationError(message="两次密码不一致")
        return  cleaned_data

