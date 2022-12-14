# Generated by Django 4.0.6 on 2022-08-08 08:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0007_alter_author_author_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='author_name',
        ),
        migrations.RemoveField(
            model_name='author',
            name='date_of_registration',
        ),
        migrations.AlterField(
            model_name='newsarticles',
            name='author',
            field=models.ForeignKey(blank=True, help_text='Select the author', null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Author'),
        ),
    ]
