from django.db import models

class Sorvete(models.Model):
    # Opções de sabor de sorvete
    SABOR_CHOICES = (
        ('Mor', 'Morango'),
        ('Cho', 'Chocolate'),
        ('Bau', 'Baunilha'),
        ('Lim', 'Limão'),
        ('Mam', 'Mamão'),
        ('Abc', 'Abacaxi'),
    )

    # Opções de cobertura para o sorvete
    COBERTURA_CHOICES = (
        ('cho', 'Chocolate'),
        ('mor', 'Morango'),
        ('car', 'Caramelo'),
        ('leC', 'Leite condensado'),
        ('amn', 'Amendoim'),
        ('frt', 'Frutas'),
    )

    # Opções de tamanho do sorvete
    TAMANHO_CHOICES = (
        ('peq', 'Pequeno'),
        ('med', 'Médio'),
        ('grd', 'Grande'),
        ('brc', 'Barca'),
        ('cas', 'Casquinha'),
        ('cop', 'Copo'),
    )

    # Campos do modelo Sorvete
    sabor = models.CharField(
        max_length=3,
        choices=SABOR_CHOICES,
        default='Mor',
    )

    cobertura = models.CharField(
        max_length=3,
        choices=COBERTURA_CHOICES,
        default='leC',
    )

    tamanho = models.CharField(
        max_length=3,
        choices=TAMANHO_CHOICES,
        default='med',
    )

    def __str__(self):
        return self.sabor
