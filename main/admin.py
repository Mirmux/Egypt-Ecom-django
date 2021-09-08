from django.contrib import admin
from .models import *


# Register your models here.

class ExhibitionGalleryAdmin(admin.StackedInline):
    model = ExhibitionGallery


class CommentInline(admin.TabularInline):
    model = Comment


@admin.register(Exhibition)
class ExhibitionAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['title', 'created', 'updated']
    inlines = [ExhibitionGalleryAdmin]

    class Meta:
        model = Exhibition


@admin.register(DiscoverTheCollection)
class DiscoverTheCollectionAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['title', 'created', 'updated']


@admin.register(TeamDirectors)
class TeamDirectorsAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['name', 'job', 'created', 'updated']


@admin.register(TeamStaff)
class TeamStaffAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['name_staff', 'job_staff', 'created', 'updated']


class CountryMuseumInline(admin.StackedInline):
    model = CountryMuseum


class CountryMuseumPhotoInline(admin.StackedInline):
    model = CountryMuseumPhotos


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['name']
    inlines = [CountryMuseumInline]


@admin.register(CountryMuseum)
class CoutryMuseumAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['name', 'post']
    inlines = [CountryMuseumPhotoInline]

    class Meta:
        model = CountryMuseum


@admin.register(Antiquities)
class AntiquitiesAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['title', 'created', 'updated', 'museum']


@admin.register(Sculpture)
class SculptureAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['name', 'created', 'updated', 'object_number']


admin.site.register(CategoryProduct)


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    ordering = ['id']
    inlines = [CommentInline]
    list_display = ['name', 'categories', 'created', 'updated']


admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(ShippingAddress)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['id', 'product', ]


@admin.register(Comment)
class CommenAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['name']

@admin.register(OnlineBooking)
class OnlineBookingAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['name', 'exhibition']


class EventGalleryInline(admin.StackedInline):
    model = EventGallery

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['organizer', 'created', 'updated']

    inlines = [EventGalleryInline]

