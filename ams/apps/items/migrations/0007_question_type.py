# Generated by Django 4.2.11 on 2024-04-29 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0006_rename_question_item_stem'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[('STANDARD', 'Standard'), ('NEGATIVE', 'Negative'), ('LIST', 'List'), ('BLANK', 'Blank')], default='STANDARD', max_length=8),
        ),
    ]
