from django.db import models


class Skillset(models.Model):
    Skill = models.CharField(max_length=100)
    Rateing = models.IntegerField()

    def __str__(self):
        return self.Skill


from rest_framework import serializers

class SkillInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skillset
        fields = '__all__'
