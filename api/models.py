from django.db import models
from django.core.files import File
from urllib.parse import urlparse
from api.util.file import download, get_buffer_ext
import os
# Create your models here.


class User(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    name = models.CharField(max_length= 255, primary_key= True)  # 닉네임
    gender = models.CharField("Gender", max_length=80, choices=GENDER_CHOICES, null=True)  # 성별
    height = models.FloatField()  # 키
    weight = models.FloatField()  # 몸무게
    shoe_size = models.IntegerField()  # 신발 사이즈
    body_picture = models.ImageField()  # 전신 사진
    skin_picture = models.ImageField()  # 피부색 사진
    # preferred_color = models.JSONField()  # 선호 색상
    preferred_color = models.CharField(max_length= 255)
    # non_preffered_color = models.JSONField()  # 비선호 색상
    non_preffered_color = models.CharField(max_length= 255)



class Item(models.Model) :
    link = models.CharField(max_length= 255, primary_key = True)
    img_link = models.CharField(max_length= 400)
    img = models.ImageField(upload_to='items')
    brand = models.CharField(max_length= 255)
    title = models.CharField(max_length= 255)
    price = models.CharField(max_length= 255)
    # size_list = models.JSONField()
    size_list = models.CharField(max_length= 255)


    def save(self, *args, **kwargs):
        # ImageField에 파일이 없고, url이 존재하는 경우에만 실행
        if self.img_link and not self.img:

            if self.img_link:
                temp_file = download(self.img_link)
                print(temp_file)
                file_name = '{urlparse}.{ext}'.format(
                    # url의 마지막 '/' 내용 중 확장자 제거
                    # ex) url = 'https://~~~~~~/bag-1623898_960_720.jpg'
                    #     -> 'bag-1623898_960_720.jpg'
                    #     -> 'bag-1623898_960_720'
                    urlparse=urlparse(self.img_link).path.split('/')[-1].split('.')[0],
                    ext=get_buffer_ext(temp_file)
                )
                with open(f'./.media/items/{file_name}', "wb") as f:
                    f.write(temp_file.getbuffer())
                self.img.save(file_name, File(temp_file))
                super().save()
            else:
                super().save()