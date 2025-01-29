from django.db import models

class Response(models.Model):
    prompt = models.TextField()
    response_text = models.TextField()
    model_used = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)
    processing_time = models.FloatField()

    def _str_(self):
        return f"Response {self.id}: {self.prompt[:50]}"