# Generated by Django 3.0.8 on 2020-07-07 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heart', '0002_auto_20200705_2337'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='Resumo',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
