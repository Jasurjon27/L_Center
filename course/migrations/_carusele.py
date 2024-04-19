from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_teacher_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carusele',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='carusele')),
                ('title', models.CharField(max_length=212)),
                ('content', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]