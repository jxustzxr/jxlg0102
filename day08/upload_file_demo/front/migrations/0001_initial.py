# Generated by Django 2.0 on 2019-06-20 02:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('thumbnail', models.FileField(upload_to='%Y/%m/%d', validators=[django.core.validators.FileExtensionValidator(['txt', 'jpg'], message='缩略图必须是txt，jpg格式的文件')])),
            ],
        ),
    ]