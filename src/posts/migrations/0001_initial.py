# Generated by Django 4.2.5 on 2023-10-01 10:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='titre')),
                ('slug', models.SlugField(blank=True, max_length=255)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateField(blank=True, null=True)),
                ('published', models.BooleanField(default=False, verbose_name='Publié')),
                ('content', models.TextField(blank=True, verbose_name='Contenu')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Article',
                'ordering': ['-created_on'],
            },
        ),
    ]
