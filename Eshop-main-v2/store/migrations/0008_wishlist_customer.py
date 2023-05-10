# Generated by Django 3.2.5 on 2023-05-09 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_wishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='customer',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='store.customer'),
            preserve_default=False,
        ),
    ]