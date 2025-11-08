from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20251108_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='modalidade',
            field=models.CharField(
                max_length=50,
                choices=[('Presencial', 'Presencial'), ('EAD', 'Educação a Distância'), ('Híbrido', 'Híbrido')],
                default='Presencial',
                help_text='Selecione a modalidade do curso'
            ),
        ),
        migrations.AddField(
            model_name='curso',
            name='habilitacao',
            field=models.CharField(
                max_length=100,
                blank=True,
                null=True,
                help_text='Ex: Bacharelado, Licenciatura, Tecnólogo'
            ),
        ),
    ]
