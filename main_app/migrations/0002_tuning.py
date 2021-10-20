# Generated by Django 3.2.8 on 2021-10-20 02:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tuning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('tune', models.CharField(choices=[('D', 'Drop D'), ('C', 'Drop C'), ('G', 'Open G')], default='D', max_length=1)),
                ('guitar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.guitar')),
            ],
        ),
    ]