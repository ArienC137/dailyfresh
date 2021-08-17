from django.db import models

# Create your models here.
class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40) # 存储加密后的长度40
    uemail = models.CharField(max_length=30)
    # 收货人地址
    uaddr = models.CharField(max_length=20)
    # 收货人详细地址
    uaddress = models.CharField(max_length=100)
    # 邮编
    uyoubian = models.CharField(max_length=6)
    uphone = models.CharField(max_length=11)