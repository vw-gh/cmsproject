# Generated by Django 4.2.5 on 2023-10-02 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branches', '0004_reception_printer'),
    ]

    operations = [
        migrations.AddField(
            model_name='reception',
            name='scaner',
            field=models.ManyToManyField(related_name='receptions_scanned', to='branches.periphery'),
        ),
        migrations.AlterField(
            model_name='reception',
            name='printer',
            field=models.ManyToManyField(related_name='receptions_printed', to='branches.periphery'),
        ),
    ]
