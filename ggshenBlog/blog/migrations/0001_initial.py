# Generated by Django 3.0.3 on 2020-02-20 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50, null=True)),
                ('author', models.CharField(max_length=20, null=True)),
                ('read', models.IntegerField(blank=True, null=True)),
                ('like', models.IntegerField(blank=True, null=True)),
                ('category', models.CharField(blank=True, max_length=50, null=True)),
                ('updateTime', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
