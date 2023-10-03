# Generated by Django 4.2.5 on 2023-10-03 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inv_manager', '0002_components_alter_typeitem_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemIP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.GenericIPAddressField()),
            ],
            options={
                'verbose_name': 'Endereços IP',
                'verbose_name_plural': 'Endereços IP',
            },
        ),
        migrations.CreateModel(
            name='ItemMemory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Memória',
                'verbose_name_plural': 'Memórias',
            },
        ),
        migrations.CreateModel(
            name='ItemModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Modelo',
                'verbose_name_plural': 'Modelos',
            },
        ),
        migrations.CreateModel(
            name='ItemOS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Sistema Operacional',
                'verbose_name_plural': 'Sistema Operacional',
            },
        ),
        migrations.CreateModel(
            name='ItemProcessor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Processador',
                'verbose_name_plural': 'Processadores',
            },
        ),
        migrations.CreateModel(
            name='ItemSector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Setor',
                'verbose_name_plural': 'Setores',
            },
        ),
        migrations.CreateModel(
            name='ItemType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Tipo',
                'verbose_name_plural': 'Tipos',
            },
        ),
        migrations.RenameModel(
            old_name='TypeItem',
            new_name='ItemBrand',
        ),
        migrations.RenameModel(
            old_name='Sector',
            new_name='ItemDisk',
        ),
        migrations.RenameModel(
            old_name='Processor',
            new_name='ItemLocalization',
        ),
        migrations.AlterModelOptions(
            name='invitem',
            options={'verbose_name': 'Itens Inventário', 'verbose_name_plural': 'Itens Inventário'},
        ),
        migrations.AlterModelOptions(
            name='itembrand',
            options={'verbose_name': 'Marca', 'verbose_name_plural': 'Marcas'},
        ),
        migrations.AlterModelOptions(
            name='itemdisk',
            options={'verbose_name': 'Disco de Armazenamento', 'verbose_name_plural': 'Discos de Armazenamento'},
        ),
        migrations.AlterModelOptions(
            name='itemlocalization',
            options={'verbose_name': 'Localização', 'verbose_name_plural': 'Localizações'},
        ),
        migrations.RemoveField(
            model_name='invitem',
            name='components',
        ),
        migrations.RemoveField(
            model_name='invitem',
            name='typei',
        ),
        migrations.AddField(
            model_name='invitem',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inv_manager.itembrand', verbose_name='Marca'),
        ),
        migrations.AddField(
            model_name='invitem',
            name='disk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inv_manager.itemdisk', verbose_name='Disco'),
        ),
        migrations.AddField(
            model_name='invitem',
            name='localization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inv_manager.itemlocalization', verbose_name='Localização'),
        ),
        migrations.DeleteModel(
            name='Components',
        ),
        migrations.AddField(
            model_name='invitem',
            name='ipitem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inv_manager.itemip', verbose_name='IP'),
        ),
        migrations.AddField(
            model_name='invitem',
            name='memory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inv_manager.itemmemory', verbose_name='Memória'),
        ),
        migrations.AddField(
            model_name='invitem',
            name='modelitem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inv_manager.itemmodel', verbose_name='Modelo'),
        ),
        migrations.AddField(
            model_name='invitem',
            name='os',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inv_manager.itemos', verbose_name='Sistema Operacional'),
        ),
        migrations.AddField(
            model_name='invitem',
            name='processor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inv_manager.itemprocessor', verbose_name='Processador'),
        ),
        migrations.AddField(
            model_name='invitem',
            name='typeitem',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inv_manager.itemtype', verbose_name='Tipo'),
        ),
        migrations.AlterField(
            model_name='invitem',
            name='sector',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inv_manager.itemsector', verbose_name='Setor'),
        ),
    ]