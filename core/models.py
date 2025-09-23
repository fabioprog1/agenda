from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name="Data do Evento")
    data_criacao = models.DateTimeField(auto_now=True)
    local = models.TextField(blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.titulo

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y %H:%M Hrs')

    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')

    def get_evento_atrasado(self):
        dt_evento = self.data_evento.date()
        hr_evento = self.data_evento.strftime('%H:%M')
        if dt_evento < date.today():
            if hr_evento < datetime.now().strftime("%H:%M"):
                return True
            else:
                return False
#        if self.data_evento < datetime.now():
#            return True
#        else:
#            return False

    def get_evento_futuro(self):
        dt_evento = self.data_evento.date()
        if dt_evento > date.today():
            return True
        else:
            return False
