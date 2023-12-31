# Generated by Django 4.2.5 on 2023-10-03 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inv_manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Components',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('processor', models.CharField(max_length=30)),
                ('disk', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterModelOptions(
            name='typeitem',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='invitem',
            name='cod_patrimonio',
            field=models.PositiveIntegerField(verbose_name='Código Patrimônio'),
        ),
        migrations.AlterField(
            model_name='invitem',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='invitem',
            name='sector',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inv_manager.sector', verbose_name='Setor'),
        ),
        migrations.AlterField(
            model_name='invitem',
            name='typei',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inv_manager.typeitem', verbose_name='Tipo'),
        ),
        migrations.AlterField(
            model_name='invitem',
            name='user',
            field=models.CharField(max_length=55, verbose_name='Usuário'),
        ),
        migrations.AddField(
            model_name='invitem',
            name='components',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inv_manager.components', verbose_name='Componentes'),
        ),
    ]
