# Generated by Django 4.2.20 on 2025-03-06 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name')),
                ('image', models.ImageField(blank=True, null=True, upload_to='workers/')),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='Age')),
                ('phone', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='Phone')),
                ('gender', models.CharField(blank=True, max_length=255, null=True, verbose_name='Gender')),
                ('payment_type', models.CharField(blank=True, choices=[('naqd', 'Naqd'), ('karta', 'Karta'), ('barchasi', 'Barchasi')], default='barchasi', max_length=255, null=True, verbose_name='Payment Type')),
                ('daily_payment', models.IntegerField(blank=True, null=True, verbose_name='Daily Payment')),
                ('languages', models.CharField(blank=True, max_length=255, null=True, verbose_name='Languages')),
                ('skills', models.TextField(blank=True, max_length=255, null=True, verbose_name='Skills')),
                ('location', models.CharField(blank=True, max_length=255, null=True, verbose_name='Location')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(choices=[(1, '1 - Very Bad'), (2, '2 - Bad'), (3, '3 - Neutral'), (4, '4 - Good'), (5, '5 - Excellent')], default=1)),
                ('text', models.TextField(blank=True, max_length=255, null=True, verbose_name='Text')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workers.user')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workers.worker')),
            ],
        ),
    ]
