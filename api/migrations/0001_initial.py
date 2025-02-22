# Generated by Django 5.1.2 on 2024-10-29 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Programer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('nickname', models.CharField(max_length=50)),
                ('age', models.PositiveSmallIntegerField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
