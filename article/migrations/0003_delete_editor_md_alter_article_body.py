# Generated by Django 4.1.7 on 2023-04-07 15:41

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_editor_md'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Editor_MD',
        ),
        migrations.AlterField(
            model_name='article',
            name='body',
            field=mdeditor.fields.MDTextField(verbose_name='正文'),
        ),
    ]