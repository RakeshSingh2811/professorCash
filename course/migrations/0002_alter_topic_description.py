# Generated by Django 4.0.8 on 2023-09-21 12:42

from django.db import migrations
import django_editorjs.fields


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='description',
            field=django_editorjs.fields.EditorJsField(),
        ),
    ]