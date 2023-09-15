# Generated by Django 4.2.5 on 2023-09-15 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_bds_delete_listing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bds',
            name='balcony_direction',
            field=models.TextField(blank=True, choices=[('Đông', 'Đông'), ('Tây', 'Tây'), ('Nam', 'Nam'), ('Bắc', 'Bắc'), ('Đông Nam', 'Đông Nam'), ('Tây Nam', 'Tây Nam'), ('Đông Bắc', 'Đông Bắc'), ('Tây Bắc', 'Tây Bắc')], max_length=50, null=True, verbose_name='Hướng ban công'),
        ),
        migrations.AlterField(
            model_name='bds',
            name='bedrooms',
            field=models.IntegerField(verbose_name='Số phòng ngủ'),
        ),
        migrations.AlterField(
            model_name='bds',
            name='description',
            field=models.TextField(verbose_name='Mô tả'),
        ),
        migrations.AlterField(
            model_name='bds',
            name='direction',
            field=models.TextField(blank=True, choices=[('Đông', 'Đông'), ('Tây', 'Tây'), ('Nam', 'Nam'), ('Bắc', 'Bắc'), ('Đông Nam', 'Đông Nam'), ('Tây Nam', 'Tây Nam'), ('Đông Bắc', 'Đông Bắc'), ('Tây Bắc', 'Tây Bắc')], max_length=50, null=True, verbose_name='Hướng nhà'),
        ),
        migrations.AlterField(
            model_name='bds',
            name='floors',
            field=models.IntegerField(blank=True, null=True, verbose_name='Tầng'),
        ),
        migrations.AlterField(
            model_name='bds',
            name='furniture',
            field=models.TextField(max_length=200, verbose_name='Nội thất'),
        ),
        migrations.AlterField(
            model_name='bds',
            name='legal',
            field=models.TextField(choices=[('Đã có sổ', 'Đã có sổ'), ('Đang chờ sổ', 'Đang chờ sổ'), ('Sổ hồng', 'Sổ hồng'), ('Sổ đỏ', 'Sổ đỏ'), ('Giấy tờ hợp lệ', 'Giấy tờ hợp lệ'), ('Hợp đồng mua bán', 'Hợp đồng mua bán'), ('Sổ đỏ/ Sổ hồng', 'Sổ đỏ/ Sổ hồng')], max_length=50, verbose_name='Giấy tờ pháp lý'),
        ),
        migrations.AlterField(
            model_name='bds',
            name='length',
            field=models.IntegerField(blank=True, null=True, verbose_name='Chiều dài'),
        ),
        migrations.AlterField(
            model_name='bds',
            name='location',
            field=models.TextField(max_length=200, verbose_name='Địa chỉ'),
        ),
        migrations.AlterField(
            model_name='bds',
            name='news_type',
            field=models.TextField(choices=[('Mua bán', 'Mua bán'), ('Nhà đất bán', 'Nhà đất bán'), ('Cần bán', 'Cần bán')], max_length=50, verbose_name='Loại tin'),
        ),
        migrations.AlterField(
            model_name='bds',
            name='price',
            field=models.IntegerField(verbose_name='Giá'),
        ),
        migrations.AlterField(
            model_name='bds',
            name='size',
            field=models.IntegerField(verbose_name='Diện tích'),
        ),
        migrations.AlterField(
            model_name='bds',
            name='toilets',
            field=models.IntegerField(verbose_name='Số toilets'),
        ),
        migrations.AlterField(
            model_name='bds',
            name='url',
            field=models.TextField(verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='bds',
            name='width',
            field=models.IntegerField(blank=True, null=True, verbose_name='Chiều ngang'),
        ),
    ]