# Generated by Django 4.2 on 2024-01-26 18:28

from django.db import migrations, models


def load_data(apps, schema_editor):
    Partype = apps.get_model('partypes', 'Partype')

    partypes = [
        {"model": "partypes.partype", "pk": 1, "fields": {"name": "Mana",
                                                          "info": "Champions have a mana pool that is consumed when casting spells. If a champion runs out of mana, they are unable to cast spells until their mana regenerates."}},
        {"model": "partypes.partype", "pk": 2, "fields": {"name": "Manaless",
                                                          "info": "Champions with the 'Manaless' partype do not have a mana pool. They can cast spells without worrying about mana constraints, allowing for more freedom in using abilities."}},
        {"model": "partypes.partype", "pk": 3, "fields": {"name": "Health",
                                                          "info": "The champion's abilities or actions are tied to their health pool. This could involve sacrificing health to perform certain actions or having abilities that scale with the champion's health."}},
        {"model": "partypes.partype", "pk": 4, "fields": {"name": "Energy",
                                                          "info": "Champions with energy regenerate it quickly, but they have a limited pool. Energy is used for casting abilities, and managing it efficiently is crucial for sustained engagements."}},
        {"model": "partypes.partype", "pk": 5, "fields": {"name": "Fury",
                                                          "info": "Fury is generated through certain actions or abilities and is used to enhance or unlock more powerful versions of a champion's skills. It adds an element of timing and resource management to their gameplay."}},
        {"model": "partypes.partype", "pk": 6, "fields": {"name": "Resourceless",
                                                          "info": "Champions with the 'Resourceless' partype do not rely on traditional resources like mana or energy. They may have unique mechanics or cooldown-based systems for their abilities."}},
        {"model": "partypes.partype", "pk": 7, "fields": {"name": "Rage",
                                                          "info": "Rage builds up over time or through specific actions, triggering a transformation or empowering the champion's abilities. Managing rage is essential for utilizing their enhanced state effectively."}},
        {"model": "partypes.partype", "pk": 8, "fields": {"name": "Shield",
                                                          "info": "Champions with the 'Shield' partype have abilities or mechanics that involve the generation and use of shields to absorb damage, providing additional defensive capabilities to themselves or allies."}},
        {"model": "partypes.partype", "pk": 9, "fields": {"name": "Heat",
                                                          "info": "Heat is generated by a champion's actions and abilities. Managing heat levels is crucial, as reaching certain thresholds may lead to overheating, imposing penalties or altering the champion's abilities."}},
        {"model": "partypes.partype", "pk": 10, "fields": {"name": "Style",
                                                           "info": "Champions with the 'Style' partype may have unique mechanics or abilities that change or improve based on the champion's chosen style or stance, adding depth to their gameplay."}},
        {"model": "partypes.partype", "pk": 11, "fields": {"name": "Ferocity",
                                                           "info": "Ferocity is generated through specific actions and is used to empower certain abilities for champions. It adds a layer of decision-making, as players must choose when to use their empowered skills strategically."}},
        {"model": "partypes.partype", "pk": 12, "fields": {"name": "Blood Well",
                                                           "info": "Champions with a 'Blood Well' partype have a secondary resource that stores health, usually gained through their abilities or actions. This stored health can be utilized or enhances certain abilities."}},
        {"model": "partypes.partype", "pk": 13, "fields": {"name": "Flow",
                                                           "info": "Flow is a resource generated through champion actions. It may provide enhanced effects or empower certain abilities, encouraging players to engage in combat to maintain and utilize their flow effectively."}},
        {"model": "partypes.partype", "pk": 14, "fields": {"name": "Moonlight",
                                                           "info": "Moonlight may be associated with specific abilities or mechanics tied to a lunar theme. It could influence the effectiveness or properties of the champion's abilities during certain phases or conditions."}},
        {"model": "partypes.partype", "pk": 16, "fields": {"name": "Grit",
                                                           "info": "Grit is a resource that champions accumulate through actions or abilities. It may enhance defensive capabilities, making the champion more resilient to damage when Grit is high."}},
        {"model": "partypes.partype", "pk": 17, "fields": {"name": "None",
                                                           "info": "Champions with the 'None' partype do not have a mana pool. They can cast spells without worrying about mana constraints, allowing for more freedom in using abilities."}},
        {"model": "partypes.partype", "pk": 18, "fields": {"name": "Courage",
                                                           "info": "Courage is associated with defensive or supportive abilities, providing the champion with enhanced defensive capabilities or support effects when certain conditions are met."}},
        {"model": "partypes.partype", "pk": 19, "fields": {"name": "Crimson Rush",
                                                           "info": "Crimson Rush is a resource or effect associated with specific actions or abilities. It may empower certain abilities or provide additional benefits when activated"}}
    ]

    for partype in partypes:
        Partype.objects.create(pk=partype['pk'], **partype['fields'])


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partype',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('info', models.CharField(max_length=300, null=True, unique=True)),
            ],
        ),
        migrations.RunPython(load_data),
    ]
