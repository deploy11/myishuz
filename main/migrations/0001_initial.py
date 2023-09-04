# Generated by Django 4.2.4 on 2023-09-02 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='Ism va Familiya Kiriting')),
                ('age', models.IntegerField(verbose_name='Yoshingiz')),
                ('portfolio_website', models.CharField(default='none', max_length=500, verbose_name='Agar Portfolio web sitegiz bo`lsa urlni kiriting')),
                ('telegram', models.CharField(default='none', max_length=500, verbose_name='Telegram nomingiz yoki telefon raqamingizni qoldiring')),
                ('instagram', models.CharField(default='none', max_length=500, verbose_name='Instagram nomingiz yoki telefon raqamingizni qoldiring')),
                ('preum', models.BooleanField(max_length=500)),
                ('image', models.ImageField(upload_to='ramlar/', verbose_name='rasmingizni joylang')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category', verbose_name='categoriya tanlang')),
            ],
        ),
    ]
