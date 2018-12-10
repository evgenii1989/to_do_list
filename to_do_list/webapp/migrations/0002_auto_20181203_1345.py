# Generated by Django 2.1.3 on 2018-12-03 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Task')),
                ('status', models.CharField(blank=True, default='Unknown', max_length=200, verbose_name='Status')),
                ('description', models.TextField(max_length=3000, verbose_name='Task description')),
            ],
        ),
        migrations.DeleteModel(
            name='List',
        ),
    ]