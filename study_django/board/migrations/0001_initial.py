# Generated by Django 4.2.3 on 2023-07-29 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boardTitle', models.CharField(max_length=150)),
                ('boardContent', models.CharField(max_length=1000)),
            ],
        ),
    ]