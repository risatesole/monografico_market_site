from django.db import models

class Product(models.Model):

    CATEGORY_CHOICE = [
        # Grocery-style
        ("FRUITS_AND_VEGETABLES", "Frutas y vegetales"),
        ("LACTEOUS", "Lacteos"),
        ("GROCERY_AND_GOURMET", "Grocery & Gourmet Food"),

        # General retail
        ("ELECTRONIC_AND_TECH", "Electronics & Tech"),
        ("CLOTHING", "Clothing"),
        ("SHOES", "Shoes"),
        ("JEWELRY", "Jewelry"),

        # Home
        ("HOME_AND_KITCHEN", "Home & Kitchen"),
        ("TOOLS_AND_HOME_IMPROVEMENT", "Tools & Home Improvement"),
        ("FURNITURE", "Furniture"),

        # Media
        ("BOOKS", "Books"),
        ("VIDEO_GAMES", "Video Games"),
        ("MUSIC", "Music"),
        ("MOVIES_AND_TV", "Movies & TV"),

        # Lifestyle
        ("BEAUTY_AND_PERSONAL_CARE", "Beauty & Personal Care"),
        ("HEALTH_AND_HOUSEHOLD", "Health & Household"),

        # Kids & family
        ("TOYS_AND_GAMES", "Toys & Games"),
        ("BABY_PRODUCTS", "Baby Products"),

        # Outdoors & vehicles
        ("SPORTS_AND_OUTDOORS", "Sports & Outdoors"),
        ("AUTOMOTIVE", "Automotive"),

        # Other common Amazon categories
        ("PET_SUPPLIES", "Pet Supplies"),
        ("OFFICE_PRODUCTS", "Office Products"),
        ("INDUSTRIAL_AND_SCIENTIFIC", "Industrial & Scientific"),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(
        max_length=40,
        choices=CATEGORY_CHOICE
    )
    image = models.ImageField(upload_to="products/", null=True, blank=True)

    def __str__(self):
        return self.name
