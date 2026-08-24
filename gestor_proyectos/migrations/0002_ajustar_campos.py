from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gestor_proyectos", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="proyecto",
            name="descripcion",
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name="proyecto",
            name="duracion",
            field=models.PositiveIntegerField(),
        ),
    ]
