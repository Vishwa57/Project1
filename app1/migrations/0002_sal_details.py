# Generated by Django 4.2.2 on 2023-07-01 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sal_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.IntegerField()),
                ('emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.employee')),
            ],
        ),
    ]
