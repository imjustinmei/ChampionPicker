# Generated by Django 4.2 on 2024-01-26 18:28

from django.db import migrations, models


def load_data(apps, schema_editor):
    Class = apps.get_model('classes', 'Class')

    classes = [
        {"model": "classes.class", "pk": 1, "fields": {"name": "Fighter",
                                                       "info": "Also commonly known as bruisers, Fighters have both defensive and offensive capabilities, and they are great at drawn out duels."}},
        {"model": "classes.class", "pk": 2, "fields": {"name": "Tank",
                                                       "info": "Tanks have high defensive stats, and are capable of absorbing a lot of damage. However, their damage output is lower."}},
        {"model": "classes.class", "pk": 3, "fields": {"name": "Mage",
                                                       "info": "Mages specialize in dealing magic damage, mainly relying on casting spells to do so."}},
        {"model": "classes.class", "pk": 4, "fields": {"name": "Assassin",
                                                       "info": "Assassins are able to provide a quick burst of damage on a vulnerable threat."}},
        {"model": "classes.class", "pk": 5, "fields": {"name": "Marksman",
                                                       "info": "Marksmen specialize in dealing high, consistent damage and have the highest potential damage output."}},
        {"model": "classes.class", "pk": 6, "fields": {"name": "Support",
                                                       "info": "Supports assist the team, by providing shields, healing, and buffs to their teammates."}}
    ]

    for className in classes:
        Class.objects.create(pk=className['pk'], **className['fields'])


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, unique=True)),
                ('info', models.CharField(max_length=300, null=True, unique=True)),
            ],
        ),
        migrations.RunPython(load_data),
    ]
