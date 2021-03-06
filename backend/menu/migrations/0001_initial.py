# Generated by Django 4.0.5 on 2022-06-20 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dish', '0001_initial'),
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish', models.ManyToManyField(related_name='menu', to='dish.dish', verbose_name='Блюдо')),
                ('restaurant', models.ManyToManyField(related_name='menu', to='restaurant.restaurants', verbose_name='Ресторан')),
            ],
            options={
                'verbose_name': 'Меню',
                'verbose_name_plural': 'Меню',
            },
        ),
    ]
