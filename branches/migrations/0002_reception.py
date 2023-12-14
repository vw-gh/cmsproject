# Generated by Django 4.2.5 on 2023-10-02 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('branches', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reception',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('printer', models.CharField(max_length=50)),
                ('scaner', models.CharField(max_length=50)),
                ('scan_folder', models.CharField(max_length=50)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='branches.branch')),
            ],
        ),
    ]
