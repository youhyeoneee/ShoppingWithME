from django.db import models

# Create your models here.

class User(models.Model) :
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    name = models.CharField(max_length = 255, primary_key = True)  # 닉네임
    gender = models.CharField("Gender", max_length=80, choices=GENDER_CHOICES, null=True)  # 성별
    height = models.FloatField()  # 키
    weight = models.FloatField()  # 몸무게
    shoe_size = models.IntegerField()  # 신발 사이즈
    body_picture = models.ImageField()  # 전신 사진
    skin_picture = models.ImageField()  # 피부색 사진
    preferred_color = models.JSONField()  # 선호 색상
    non_preffered_color = models.JSONField()  # 비선호 색상
