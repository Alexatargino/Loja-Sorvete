from django.db import models


class Sorvete(models.Model):

    sabor_creme = (
        ('Aç', 'Açai'),
        ('Cup', 'Cupuaçu')
    )

    sabor = models.CharField(
        max_length=3,
        choices=sabor_creme,
        default='Aç',
    )

    sabor_cobertura = (
        ('cho', 'Chocolate'),
        ('mor', 'Morango'),
        ('car', 'Caramelo'),
        ('leC', 'Leite condensado')
    )

    cobertura = models.CharField(
        max_length=3,
        choices=sabor_cobertura,
        default='leC',
    )

    tipo_tamanho = (
        ('peq', 'Pequeno'),
        ('med', 'Médio'),
        ('grd', 'Grande'),
        ('brc', 'Barca')
    )

    tamanho = models.CharField(
        max_length=3,
        choices=tipo_tamanho,
        default='med',
    )


    def __str__(self):
        return self.sabor