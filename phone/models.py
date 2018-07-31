from django.db import models


# Create your models here.

# 用户表
class User(models.Model):
    id = models.IntegerField(primary_key=True)  # 用户ID
    email = models.EmailField(max_length=32)  # 邮箱
    username = models.CharField(max_length=10, unique=True)  # 用户名
    password_hash = models.CharField(max_length=128)  # 密码（哈希后）
    registration_time = models.DateTimeField(auto_now_add=True)  # 注册时间
    description = models.TextField()  # 个人描述


# 手机品牌表
class Maker(models.Model):
    id = models.IntegerField(primary_key=True)  # 品牌ID
    maker_name = models.CharField(max_length=16)  # 品牌名称


# 手机信息表
class Phone(models.Model):
    id = models.IntegerField(primary_key=True)  # 手机ID
    maker = models.ForeignKey(Maker, on_delete=models.CASCADE)  # 品牌名
    price = models.CharField(max_length=16)  # 价格
    evaluate = models.FloatField(default=0)  # 评分
    time = models.DateField()  # 生产日期
    screen_size = models.CharField(max_length=16)  # 屏幕尺寸
    CPU = models.CharField(max_length=16)  # CPU型号
    RAM = models.CharField(max_length=16)  # 运行内存
    screen_resolution = models.CharField(max_length=16)  # 屏幕分辨率
    ROM = models.CharField(max_length=16)  # 存储内存
    system = models.CharField(max_length=16)  # 操作系统
    camera_rear = models.CharField(max_length=16)  # 后置相机
    camera_secondary = models.CharField(max_length=16)  # 前置相机
    battery_capacity = models.CharField(max_length=16)  # 电池容量


# 手机图片表
class Photo(models.Model):
    id = models.IntegerField(primary_key=True)  # 图片ID
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    description = models.CharField(max_length=20, default='手机图片')
    image = models.CharField(max_length=20)
