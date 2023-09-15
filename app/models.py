from django.db import models
from django.contrib.auth.models import User

# Create your models here.

news_type_CHOICES = (
    ('Mua bán', 'Mua bán'),
    ('Nhà đất bán', 'Nhà đất bán'),
    ('Cần bán', 'Cần bán'),
)

direction_CHOICES = (
    ('Đông', 'Đông'),
    ('Tây', 'Tây'),
    ('Nam', 'Nam'),
    ('Bắc', 'Bắc'),
    ('Đông Nam', 'Đông Nam'),
    ('Tây Nam', 'Tây Nam'),
    ('Đông Bắc', 'Đông Bắc'),
    ('Tây Bắc', 'Tây Bắc'),

)

balcony_direction_CHOICES = (
    ('Đông', 'Đông'),
    ('Tây', 'Tây'),
    ('Nam', 'Nam'),
    ('Bắc', 'Bắc'),
    ('Đông Nam', 'Đông Nam'),
    ('Tây Nam', 'Tây Nam'),
    ('Đông Bắc', 'Đông Bắc'),
    ('Tây Bắc', 'Tây Bắc'),

)

legal_CHOICES = (
    ('Đã có sổ', 'Đã có sổ'),
    ('Đang chờ sổ', 'Đang chờ sổ'),
    ('Sổ hồng', 'Sổ hồng'),
    ('Sổ đỏ', 'Sổ đỏ'),
    ('Giấy tờ hợp lệ', 'Giấy tờ hợp lệ'),
    ('Hợp đồng mua bán', 'Hợp đồng mua bán'),
    ('Sổ đỏ/ Sổ hồng', 'Sổ đỏ/ Sổ hồng'),
)

price_CHOICES = (
    ('Nhỏ hơn 500000000', 'Nhỏ hơn 500000000'),
    ('Từ 500000000 đến 1000000000', 'Từ 500000000 đến 1000000000'),
    ('Từ 1000000000 đến 5000000000', 'Từ 1000000000 đến 5000000000'),
    ('Lớn hơn 5000000000', 'Lớn hơn 5000000000'),
)

size_CHOICES = (
    ('Nhỏ hơn 50', 'Nhỏ hơn 50'),
    ('Từ 50 đến 100', 'Từ 50 đến 100'),
    ('Từ 100 đến 500', 'Từ 100 đến 500'),
    ('Lớn hơn 500', 'Lớn hơn 500'),
)


class BDS(models.Model):
    # BDSid=models.IntegerField('ID',blank=True, null=True)
    news_type = models.TextField(
        'Loại tin', max_length=50, choices=news_type_CHOICES,  blank=True, null=True)
    price = models.FloatField('Giá',  blank=True, null=True)
    size = models.FloatField('Diện tích (mét vuông)',  blank=True, null=True)
    direction = models.TextField(
        'Hướng nhà', max_length=50, choices=direction_CHOICES, blank=True, null=True)
    balcony_direction = models.TextField('Hướng ban công', max_length=50,
                                         choices=balcony_direction_CHOICES, blank=True, null=True)
    legal = models.TextField(
        'Giấy tờ pháp lý', max_length=50, choices=legal_CHOICES,  blank=True, null=True)
    width = models.TextField('Chiều ngang', blank=True, null=True)
    length = models.TextField('Chiều dài', blank=True, null=True)
    bedrooms = models.TextField('Số phòng ngủ', blank=True, null=True)
    toilets = models.TextField('Số toilets', blank=True, null=True)
    floors = models.TextField('Tầng', blank=True, null=True)
    furniture = models.TextField(
        'Nội thất', max_length=200,  blank=True, null=True)
    url = models.TextField('URL',  blank=True, null=True)
    location = models.TextField(
        'Địa chỉ', max_length=200,  blank=True, null=True)
    description = models.TextField('Mô tả',  blank=True, null=True)
    range_price = models.TextField(
        'Khoảng giá', choices=price_CHOICES, default=price_CHOICES[0][0],  blank=True, null=True)
    range_size = models.TextField(
        'Khoảng diện tích', choices=size_CHOICES, default=size_CHOICES[0][0], blank=True, null=True)
    city = models.TextField('Thành phố', max_length=200,
                            default="Unknown", blank=True, null=True)

    def __str__(self):
        return self.ID
