# Generated by Django 4.2.11 on 2024-04-29 02:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0005_item_learning_objective_alter_item_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='question',
            new_name='stem',
        ),
    ]
