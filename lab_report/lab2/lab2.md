# Objectives:
1) intitializing the product_module.
2) making different modules suitable as per needs and regestiring to database.

# Introduction:


# Procedure:
1. in 'models.py' create a model for brands

        code:
        class Brand(models.Model):
        name = models.CharField(max_length=200)
        is_active = models.BooleanField()

2. add the brand table to the database by

        python manage.py makemigrations
        python manage.py migrate

3. in the 'admin.py' which add the content ot the admin panel add the following code :

        from .models import Brand
        admin.site.register(Brand)

4. run the server and verify the table by performing the CRUDE operation.
        
        python manage.py runserver

5. in the 'models.py' edit the code for the brand model with the following code:

        class Brand(models.Model):
            name = models.CharField(max_length=200)
            is_active = models.BooleanField()

6. in the same edit the code for the category model 

        code:
        class Category(models.Model):
            name = models.CharField(max_length=200)
            is_active = models.BooleanField()
            class Meta:
             verbose_name_plural = "Categories"
7. add the necessary fields  to the product model  

        code:
        class Product(models.Model):
            name = models.CharField(max_length=200)
            price = models.FloatField()
            quantity = models.IntegerField()
            image_url = models.CharField(max_length=500)
            color_code = models.CharField(max_length=20)
            brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
            category = models.ForeignKey(Category, on_delete=models.CASCADE)
            registered_on = models.DateTimeField()
            is_active = models.BooleanField()
8. save the changes to the database.

9. to enable the category and product models in the admin interface, add the following code in 'admin.py'

        from .models import Brand, Category, Product
        admin.site.register(Brand)
        admin.site.register(Category)
        admin.site.register(Product)

10. run the project server and verify the CRUD operations for brand, category and product respectively

        python manage.py runserver   

# Output:

![image of brand model](https://github.com/pradhan21/ecommerce/blob/master/lab_report/lab2/Screenshot%20(41).png)
