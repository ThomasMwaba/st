# Generated by Django 5.0.4 on 2024-04-13 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_alter_submit_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submit',
            name='learning',
            field=models.CharField(choices=[('Active Recall', 'Active Recall'), ('Horizontal Learning', 'Horizontal Learning'), ('Vertical Learning', 'Vertical Learning')], max_length=50),
        ),
    ]
