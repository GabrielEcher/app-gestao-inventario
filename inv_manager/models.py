from django.db import models
from django.contrib.auth.models import User


class ItemType(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'

    def __str__(self) -> str:
        return self.name


class ItemProcessor(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Processador'
        verbose_name_plural = 'Processadores'

    def __str__(self) -> str:
        return self.name


class ItemDisk(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Disco de Armazenamento'
        verbose_name_plural = 'Discos de Armazenamento'

    def __str__(self) -> str:
        return self.name


class ItemOS(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Sistema Operacional'
        verbose_name_plural = 'Sistema Operacional'

    def __str__(self) -> str:
        return self.name


class ItemMemory(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Memória'
        verbose_name_plural = 'Memórias'

    def __str__(self) -> str:
        return self.name


class ItemLocalization(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Localização'
        verbose_name_plural = 'Localizações'

    def __str__(self) -> str:
        return self.name


class ItemSector(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Setor'
        verbose_name_plural = 'Setores'

    def __str__(self) -> str:
        return self.name


class ItemBrand(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self) -> str:
        return self.name


class ItemModel(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Modelo'
        verbose_name_plural = 'Modelos'

    def __str__(self) -> str:
        return self.name


class ItemIP(models.Model):
    name = models.GenericIPAddressField(max_length=30)

    class Meta:
        verbose_name = 'Endereços IP'
        verbose_name_plural = 'Endereços IP'

    def __str__(self) -> str:
        return self.name


class InvItem(models.Model):
    cod_patrimonio = models.PositiveIntegerField(
        verbose_name='Código Patrimônio')
    user = models.CharField(max_length=55, verbose_name='Usuário')
    typeitem = models.ForeignKey(
        ItemType, on_delete=models.SET_NULL, blank=False, null=True, verbose_name='Tipo')
    name = models.CharField(max_length=30, verbose_name='Nome')
    sector = models.ForeignKey(
        ItemSector, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Setor')
    processor = models.ForeignKey(
        ItemProcessor, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Processador')
    disk = models.ForeignKey(
        ItemDisk, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Disco')
    os = models.ForeignKey(ItemOS, on_delete=models.SET_NULL,
                           blank=True, null=True, verbose_name='Sistema Operacional')
    memory = models.ForeignKey(
        ItemMemory, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Memória')
    localization = models.ForeignKey(
        ItemLocalization, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Localização')
    brand = models.ForeignKey(
        ItemBrand, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Marca')
    modelitem = models.ForeignKey(
        ItemModel, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Modelo')
    ipitem = models.ForeignKey(
        ItemIP, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='IP')

    class Meta:
        verbose_name = 'Itens Inventário'
        verbose_name_plural = 'Itens Inventário'

    def __str__(self) -> str:
        return f'{self.name}'
