# Generated by Django 2.0 on 2018-01-28 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raiseapp', '0002_reward_timeframe'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reward',
            options={'ordering': ['amount']},
        ),
        migrations.AddField(
            model_name='pledge',
            name='comments',
            field=models.TextField(blank=True),
        ),
    ]
