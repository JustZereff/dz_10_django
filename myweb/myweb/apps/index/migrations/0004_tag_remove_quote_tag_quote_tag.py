# Generated by Django 4.1.13 on 2024-05-09 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_author_message_sent_alter_quote_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tags', models.CharField(max_length=150)),
            ],
        ),
        migrations.RemoveField(
            model_name='quote',
            name='tag',
        ),
        migrations.AddField(
            model_name='quote',
            name='tag',
            field=models.ManyToManyField(to='index.tag'),
        ),
    ]
