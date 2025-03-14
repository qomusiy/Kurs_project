# Generated by Django 5.1.7 on 2025-03-11 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('teacher', models.CharField(max_length=50)),
                ('teacher_id', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('stars', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('made_date', models.DateField()),
                ('language', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to='course_img')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
