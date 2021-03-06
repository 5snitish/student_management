# Generated by Django 3.0.6 on 2021-04-04 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('users', '0005_auto_20210404_2058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_student',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_super_admin',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_teacher',
        ),
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.Group'),
            preserve_default=False,
        ),
    ]
