# Generated by Django 4.1 on 2022-08-18 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0003_likepost'),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowersCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.CharField(max_length=200)),
                ('user', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'FollowersCount',
            },
        ),
        migrations.AlterModelOptions(
            name='likepost',
            options={'verbose_name_plural': 'LikePost'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name_plural': 'Post'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name_plural': 'Profile'},
        ),
    ]
