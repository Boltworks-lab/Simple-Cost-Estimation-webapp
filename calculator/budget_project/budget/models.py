from django.db import models

# Create your models here.
class budget(models.Model):
    TIME_CHOICES = [
        (1, '1 month'),
        (2, '2 months'),
        (3, '3 months'),
        (4, '4 months'),
        (5, '5 months'),
        (6, '6 months'),
    ]
    USAGE_CHOICES = [
        ('personal', 'Personal Use'),
        ('business', 'Business Use'),
        ('enterprise', 'Enterprise Use'),
        ('non-profit', 'Non-Profit Use')
    ]
    project_name = models.CharField(max_length = 200)
    time_of_completion = models.IntegerField(choices= TIME_CHOICES)
    require_hosting = models.BooleanField(default= False)
    project_use = models.CharField(max_length=20, choices= USAGE_CHOICES)
    require_it_maintenance = models.BooleanField(default= False)

    def calculate_cost(self):
        base_cost = self.time_of_completion * 50

        if self.require_hosting:
            base_cost += 100

        if self.project_use == 'personal':
            base_cost += 50
        elif self.project_use == 'business':
            base_cost += 100
        elif self.project_use == 'enterprise':
            base_cost += 200
        elif self.project_use == 'non-profit':
            base_cost += 30

        if self.require_it_maintenance:
            base_cost += 100

        return base_cost
    
    def __str__(self) -> str:
        return self.project_name
    




