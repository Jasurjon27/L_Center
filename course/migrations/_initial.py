import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=212)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=212)),
                ('surname', models.CharField(max_length=212)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('experience', models.CharField(max_length=212)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=212)),
                ('description', models.TextField()),
                ('price', models.PositiveIntegerField(default=0)),
                ('course_image', models.ImageField(upload_to='course')),
                ('tags', models.ManyToManyField(to='course.tag')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.teacher')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]