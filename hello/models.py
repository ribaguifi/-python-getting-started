from django.db import models


class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)
    
    def __str__(self):
        return f"Greeting {self.when}"

    def foo(self):
        return 3 + 4

    def bar(self):
        raise NotImplementedError("Boom!")
