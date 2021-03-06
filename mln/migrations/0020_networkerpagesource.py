# Generated by Django 2.2 on 2019-08-09 14:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mln', '0019_unique_constraints'),
    ]

    operations = [
        migrations.CreateModel(
            name='NetworkerPageSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.TextField()),
                ('networker', models.OneToOneField(limit_choices_to={'profile__is_networker': True}, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
