# Generated by Django 4.0.6 on 2022-07-17 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drug_code', models.IntegerField()),
                ('medicine_name', models.CharField(max_length=100)),
                ('unit_size', models.IntegerField()),
                ('mrp', models.IntegerField()),
            ],
        ),
    ]
