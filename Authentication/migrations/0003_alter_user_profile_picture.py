# Generated by Django 4.2.7 on 2023-12-15 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0002_user_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(default='Auth/Profile_pics/default', upload_to='Auth/profile_pics/'),
        ),
    ]
