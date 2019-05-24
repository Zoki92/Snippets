from django.utils import timezone
"""
Django offers three options to use model inheritance:
Abstract models: Useful when you want to put some common
 information into several models. No database table is 
 created for the abstract model.
Multi-table model inheritance: Applicable when each model
 in the hierarchy is considered a complete model by itself.
 A database table is created for each model.
Proxy models: Useful when you need to change the behavior of a model, 
 for example, by including additional methods, changing the default manager,
 or using different meta options. No database table is created for proxy 
 models.
"""

# Abstract model

from django.db import models


class BaseContent(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Text(BaseContent):
    body = models.TextField()


"""
To mark a model as abstract, you need to include abstract=True in its Meta 
class. Django will recognize that it is an abstract model and will not create
 a database table for it. To create child models, you just need to subclass 
 the abstract model.In this case, Django would create a table for the Text 
 model only, including the title, created, and body fields.
"""


# Multi-table model inheritance


class BaseContent(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)


class Text(BaseContent):
    body = models.TextField()


"""
In multi-table inheritance, each model corresponds to a database table. 
Django creates a OneToOneField field for the relationship in the child's model
 to its parent. Django would include an automatically generated OneToOneField
  field in the Text model and create a database table for each model.
"""

# Proxy models


class BaseContent(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)


class OrderedContent(BaseContent):
    class Meta:
        proxy = True
        ordering = ['created']

    def created_delta(self):
        return timezone.now() - self.created


"""
Proxy models are used to change the behavior of a model, for example, by
 including additional methods or different meta options. Both models 
 operate on the database table of the original model. To create a proxy 
 model, add proxy=True to the Meta class of the model.
Here, we define an OrderedContent model that is a proxy model for the 
Content model. This model provides a default ordering for QuerySets and 
an additional created_delta() method. Both models, Content and OrderedContent, 
operate on the same database table, and objects are accessible via the ORM 
through either model.
"""
