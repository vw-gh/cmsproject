# Generated by Django 4.2.5 on 2023-10-23 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branches', '0007_alter_qa_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qa',
            name='question',
            field=models.CharField(max_length=100),
        ),
    ]
