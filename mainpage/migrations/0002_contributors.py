# Generated by Django 3.1.1 on 2020-10-02 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contributors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='ФИО')),
                ('bio', models.TextField()),
            ],
        ),
    ]
