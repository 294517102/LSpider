# Generated by Django 3.0.1 on 2020-04-02 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubDomainList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scanid', models.IntegerField()),
                ('subdomain', models.CharField(max_length=50)),
                ('lastscan', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='UrlTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=200)),
            ],
        ),
    ]
