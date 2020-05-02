# Generated by Django 3.0.5 on 2020-04-26 18:20

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mptt.fields
import tinymce_4.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seo_h1', models.CharField(blank=True, default='', max_length=255, verbose_name='<h1>')),
                ('seo_title', models.CharField(blank=True, default='', max_length=255, verbose_name='<title>')),
                ('seo_keywords', models.CharField(blank=True, default='', max_length=255, verbose_name='<meta name="keywords">')),
                ('seo_description', models.CharField(blank=True, default='', max_length=255, verbose_name='<meta name="description">')),
                ('seo_prevent_indexing', models.BooleanField(default=False, verbose_name='не индексировать')),
                ('name', models.CharField(max_length=255, verbose_name='название')),
                ('slug', models.CharField(blank=True, default='', max_length=50, verbose_name='псевдоним')),
                ('url', models.CharField(blank=True, max_length=255, verbose_name='URL')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='изображение')),
                ('pub_time', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='время публикации')),
                ('end_pub_time', models.DateTimeField(blank=True, null=True, verbose_name='время окончания публикации')),
                ('is_pub', models.BooleanField(default=True, verbose_name='опубликовано')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='время создания')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='время обновления')),
                ('content', tinymce_4.fields.TinyMCEModelField(blank=True, verbose_name='содержимое')),
                ('processed_content', models.TextField(blank=True, default='', null=True, verbose_name='обработанное содержимое')),
                ('layout', models.IntegerField(choices=[(0, 'главная'), (1, 'статья')], null=True, verbose_name='шаблон')),
                ('preview', models.TextField(blank=True, default='', null=True, verbose_name='Текст превью')),
                ('download_title', models.CharField(blank=True, default='', max_length=255, verbose_name='Подпись к файлу')),
                ('download_file', models.FileField(blank=True, max_length=255, null=True, upload_to='document', verbose_name='Файл')),
                ('likes', models.PositiveIntegerField(default=0, verbose_name='Likes')),
                ('dislikes', models.PositiveIntegerField(default=0, verbose_name='Dislikes')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='ursamajor.Page', verbose_name='раздел')),
            ],
            options={
                'verbose_name': 'страница',
                'verbose_name_plural': 'страницы',
            },
        ),
    ]