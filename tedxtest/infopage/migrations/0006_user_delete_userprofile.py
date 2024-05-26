# Generated by Django 5.0.6 on 2024-05-24 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infopage', '0005_delete_user_userprofile_email_userprofile_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('city', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
