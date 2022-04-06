# Generated by Django 4.0.3 on 2022-04-06 21:13

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
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/media')),
                ('text', models.TextField()),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('featured', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('draft', 'draft'), ('published', 'published')], default='draft', max_length=25)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('published_at', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'article',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Manual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True, unique=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('description', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Manuals',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('approved_comment', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='knowledge.article')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='manual',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='knowledge.manual'),
        ),
        migrations.AlterIndexTogether(
            name='article',
            index_together={('manual', 'title')},
        ),
    ]