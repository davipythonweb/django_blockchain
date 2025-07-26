from django.db import models
import hashlib
import time

class Bloco(models.Model):
    index = models.IntegerField()
    dados = models.TextField()
    hash_anterior = models.CharField(max_length=64)
    nonce = models.IntegerField(default=0)
    timestamp = models.FloatField(default=time.time)
    hash = models.CharField(max_length=64)

    def calcula_hash(self):
        conteudo = f"{self.index}{self.dados}{self.hash_anterior}{self.nonce}{self.timestamp}"
        return hashlib.sha256(conteudo.encode()).hexdigest()

    def minera_bloco(self, dificuldade=4):
        alvo = "0" * dificuldade
        while not self.hash.startswith(alvo):
            self.nonce += 1
            self.hash = self.calcula_hash()

    def save(self, *args, **kwargs):
        if not self.hash:
            self.hash = self.calcula_hash()
        super().save(*args, **kwargs)
