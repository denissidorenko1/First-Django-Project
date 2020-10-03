# Generated by Django 3.1.1 on 2020-10-02 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0002_contributors'),
    ]

    operations = [
        migrations.AddField(
            model_name='contributors',
            name='contributor_id',
            field=models.IntegerField(default=0, verbose_name='id'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contributors',
            name='bio',
            field=models.TextField(verbose_name='БИО'),
        ),
    ]
