# Generated by Django 5.0.3 on 2024-04-02 17:00

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitoblar', '0003_comment_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Til',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(default=1, upload_to='book_images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='stars_given',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='ega',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ega',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='ega',
            name='gender',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='ega',
            name='phone',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='tillar',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='til', to='kitoblar.til'),
            preserve_default=False,
        ),
    ]
