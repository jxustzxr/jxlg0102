from django.db import models

# Create your models here.

class FrontUser(models.Model):
    username = models.CharField(max_length=100)
    def __str__(self):
        return "<FrontUser:(id:%s,username:%s)>" %(self.id,self.username)
class UserExtension(models.Model):
    school = models.CharField(max_length=100)
    user = models.OneToOneField("FrontUser",on_delete=models.CASCADE,related_name='extension')


    def __str__(self):
        return "<UserExtension:(id:%s,school:%s,user_id:%s)>" % (self.id, self.school,self.user_id)



# class Category(models.Model):
#     name=models.CharField(max_length=100)
# class Tag(models.Model):
#     name=models.CharField(max_length=20)
#     articles=models.ManyToManyField("Article",related_name="tags")
#
# class Article(models.Model):
#     title=models.CharField(max_length=100)
#     content=models.TextField()
#     category=models.ForeignKey("Category",on_delete=models.CASCADE,null=True,related_name="articles")
#     author=models.ForeignKey("frontuser.FrontUser",on_delete=models.CASCADE,null=True)
#
#     def __str__(self):
#         return "<Article:(id:%s,title:%s)>"%(self.id,self.title)
