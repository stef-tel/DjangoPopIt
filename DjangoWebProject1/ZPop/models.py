from django.db import models

class Zlogin(models.Model):
    name = models.CharField(max_length=100)
    sid = models.CharField(max_length=3)
    userName = models.CharField(max_length=100)
    password = models.CharField(max_length=15)
    creationDate = models.DateTimeField(auto_now_add=True, auto_now=False, 
                                verbose_name="Creation Date")
    
    def __str__(self):
        """ 
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que 
        nous traiterons plus tard et dans l'administration
        """
        return self.name
