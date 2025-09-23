from django.contrib import admin
from .models import Product, ProductImage

# Inline for product images
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  # Number of extra blank image slots
    readonly_fields = ('id',)

# Register Product with images inline
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "category", "is_available", "created_at")
    list_filter = ("category", "is_available")
    search_fields = ("name", "description")
    inlines = [ProductImageInline]  # Add images inline

# Optionally register ProductImage separately if you want
@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("product", "image", "is_main")
    list_filter = ("is_main",)
    search_fields = ("product__name",)



