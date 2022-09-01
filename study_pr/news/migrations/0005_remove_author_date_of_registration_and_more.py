# Generated by Django 4.0.6 on 2022-08-08 05:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0004_author_rubric_newsarticles_author_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='date_of_registration',
        ),
        migrations.AlterField(
            model_name='newsarticles',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Author'),
        ),
    ]