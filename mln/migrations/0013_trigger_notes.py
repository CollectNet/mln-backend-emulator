# Generated by Django 2.1 on 2019-04-03 11:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mln', '0012_about_me'),
    ]

    operations = [
        migrations.AddField(
            model_name='networkermessagetrigger',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='about_me', to=settings.AUTH_USER_MODEL),
        ),
    ]
