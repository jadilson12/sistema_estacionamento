# Generated by Django 2.2 on 2019-05-01 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_movrotativo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensalista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicio', models.DateField()),
                ('valor_mes', models.DecimalField(decimal_places=2, max_digits=5)),
                ('veiculo', models.ForeignKey(on_delete=False, to='core.Veiculo')),
            ],
        ),
    ]
