from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, db_index=True)

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('store:filtered_products', args=[self.slug])
    
    def __str__(self):
        return self.name
 

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    # created_by
    title = models.CharField(max_length=255)
    desciption= models.TextField(max_length=1000, blank=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse("store:single_product", kwargs={
            'category_slug': self.category.slug,
            'product_slug': self.slug})
        # return "%s/%s" % (self.category.slug, self.slug)

    def __str__(self):
        return self.title
        