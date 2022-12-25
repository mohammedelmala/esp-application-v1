# Generated by Django 4.1.4 on 2022-12-24 06:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(db_index=True, max_length=30, unique=True)),
                ('name', models.CharField(db_index=True, max_length=60, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, default='/no_image-1', null=True, upload_to='')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('createdBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='brands', to=settings.AUTH_USER_MODEL)),
                ('updatedBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='update_brands', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(db_index=True, max_length=30, unique=True)),
                ('name', models.CharField(db_index=True, max_length=60, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, default='/no_image-1', null=True, upload_to='')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('createdBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categories', to=settings.AUTH_USER_MODEL)),
                ('updatedBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='update_categories', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(db_index=True, max_length=30, unique=True)),
                ('name', models.CharField(db_index=True, max_length=60, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, default='/no_image-1', null=True, upload_to='')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=11, null=True)),
                ('countInStock', models.IntegerField(default=0)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='products', to='inv.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='products', to='inv.category')),
                ('createdBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to=settings.AUTH_USER_MODEL)),
                ('updatedBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='update_products', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]