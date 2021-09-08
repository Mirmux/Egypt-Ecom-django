from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db.models import OneToOneField
from django.urls import reverse


class Exhibition(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(default='Can you describe your Museum?')
    image = models.ImageField(upload_to='Exhibition', blank=False, verbose_name='Image to Exhibition')
    cost_adults = models.IntegerField(default=0)
    cost_children = models.IntegerField(default=0)

    organizer = models.CharField(max_length=60)
    address = models.CharField(max_length=200, default='')
    phone = models.CharField(max_length=80, default='')
    email = models.EmailField(max_length=250, default='')
    image_galery = models.FileField(upload_to='Exhibition/gallery/', blank=False,
                                    verbose_name='Image gallery for Museum')

    created = models.DateTimeField(auto_now_add=False)
    updated = models.DateTimeField(auto_now=True)

    start_time = models.TimeField(verbose_name='Start-Time', null=True)
    end_time = models.TimeField(verbose_name='End-Time', null=True)

    def __str__(self):
        return self.title


class ExhibitionGallery(models.Model):
    post = models.ForeignKey(Exhibition, default=None, on_delete=models.CASCADE, related_name='galleries')
    images = models.FileField(upload_to='ExhibitGallery/')

    def __str__(self):
        return self.post.title


class DiscoverTheCollection(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='DiscoverTheCollection', blank=False, verbose_name='Collection Images')
    description = models.TextField(default='About collection . . .')

    is_active = models.BooleanField(default=False, verbose_name='Is Active')

    # need enter highlights

    artist = models.CharField(max_length=20)
    year = models.CharField(max_length=15)
    style = models.CharField(max_length=20)
    material = models.CharField(max_length=30)
    dimension = models.CharField(max_length=40)
    type = models.CharField(max_length=25)
    object_number = models.IntegerField(default='')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # About Artist

    artist_name = models.CharField(max_length=40)
    image_artist = models.ImageField(upload_to='DiscoverTheCollection/artist', blank=False)
    come_from = models.CharField(max_length=30)
    description_artist = models.TextField(default='About artist . . . ')


class TeamDirectors(models.Model):
    # Board of Directors
    image = models.ImageField(upload_to='team/directors', blank=False, verbose_name='Director`s Picture')
    name = models.CharField(max_length=30, verbose_name='Director`s name')
    job = models.CharField(max_length=30, verbose_name='Director`s job')
    description = models.TextField()
    country = models.CharField(max_length=30, verbose_name='Director`s country')

    facebook = models.CharField(max_length=80, blank=True, default='e.g. @mirfayziyev', verbose_name='Facebook account')
    twitter = models.CharField(max_length=80, blank=True, default='e.g. @mirfayziyev', verbose_name='Twitter account')
    linkedin = models.CharField(max_length=80, blank=True, default='e.g. @mirfayziyev', verbose_name='LinkedIn account')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class TeamStaff(models.Model):
    # Museum Staff
    image_staff = models.ImageField(upload_to='team/staff', blank=True, verbose_name='Staff`s Picture')
    name_staff = models.CharField(max_length=30, blank=True, verbose_name='Staff`s name')
    job_staff = models.CharField(max_length=30, blank=True, verbose_name='Staff`s job')
    phone_staff = models.CharField(max_length=50, blank=True, verbose_name='Phone staff')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_staff


class Country(models.Model):
    # Country Model
    name = models.CharField(max_length=100, verbose_name='Country name')
    phone = models.CharField(max_length=300, verbose_name='Phone')
    image = models.ImageField(upload_to='country/country', verbose_name='Image Country')
    email = models.EmailField(max_length=100, verbose_name='Emails')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Countries'


class CountryMuseum(models.Model):
    post = models.ForeignKey(Country, default=None, on_delete=models.CASCADE, related_name='museum')

    # Option
    name = models.CharField(max_length=100, verbose_name='Museum name')
    address = models.CharField(max_length=200, verbose_name='Address')
    phone = models.CharField(max_length=300, verbose_name='Phone')
    image = models.ImageField(upload_to='country/museum', verbose_name='Image Museum')

    # Museum works time
    work_t = models.CharField(max_length=100, verbose_name='Saturday until Thursday works time')
    work_t2 = models.CharField(max_length=100, verbose_name='Friday works time')

    # Museum story works time
    work_st = models.CharField(max_length=100, blank=True, verbose_name='Saturday until Thursday works time')
    work_st2 = models.CharField(max_length=100, blank=True, verbose_name='Friday works time')

    # Museum costs
    adults_cost = models.CharField(max_length=30, blank=True, verbose_name='Adults cost')
    Student_cost = models.CharField(max_length=30, blank=True, verbose_name='Student cost')
    Senior_cost = models.CharField(max_length=30, blank=True, verbose_name='Senior 60+ cost')
    children_cost = models.CharField(max_length=30, blank=True, verbose_name='Age 6 and under 10 cost')

    # Transposrt
    metro = models.CharField(max_length=300, blank=True, verbose_name='Metro')
    bus = models.CharField(max_length=300, blank=True, verbose_name='Bus')
    electric_train = models.CharField(max_length=300, blank=True, verbose_name='Electric Train')
    bike_car = models.CharField(max_length=300, blank=True, verbose_name='Bike and Car')

    created = models.DateTimeField(auto_now_add=False)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post.name

    class Meta:
        verbose_name_plural = 'Country Museum Photos'


class CountryMuseumPhotos(models.Model):
    posts = models.ForeignKey(CountryMuseum, default=None, on_delete=models.CASCADE, related_name='photos')

    images = models.ImageField(upload_to='country/museum/photos', verbose_name='Images for Museum')

    def __str__(self):
        return self.posts.name



class Antiquities(models.Model):
    place = models.CharField(max_length=100, verbose_name='Antiquities Place')
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='DiscoverTheCollection', blank=False, verbose_name='Antiquities Images')
    description = models.TextField(default='About collection . . .')

    # need enter highlights

    museum = models.CharField(max_length=200, verbose_name='Museum name')
    year = models.CharField(max_length=15, verbose_name='Year')
    style = models.CharField(max_length=20, verbose_name='Style')
    material = models.CharField(max_length=30, verbose_name='Material')
    dimension = models.CharField(max_length=40, verbose_name='Dimension')
    type = models.CharField(max_length=25, verbose_name='Type')
    object_number = models.IntegerField(default='', verbose_name='Antiquities number')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # About Artist

    museum_name = models.CharField(max_length=40)
    image_museum = models.ImageField(upload_to='DiscoverTheCollection/museum', blank=False)
    situated_museum = models.CharField(max_length=30)
    description_museum = models.TextField(default='About museum . . . ')


class Sculpture(models.Model):
    name = models.CharField(max_length=50, verbose_name='Sculpture`s Name')
    image = models.ImageField(upload_to='DiscoverTheCollection', blank=False, verbose_name='Sculpture Images')
    description = models.TextField(default='About Sculpture . . .')

    # need enter highlights

    year = models.CharField(max_length=30, verbose_name='Year Sculpture')
    style = models.CharField(max_length=50, verbose_name='Style Sculpture')
    material = models.CharField(max_length=50, verbose_name='Material Sculpture')
    dimension = models.CharField(max_length=50, verbose_name='Dimension Sculpture')
    type = models.CharField(max_length=45, verbose_name='Type Sculpture')
    object_number = models.IntegerField(default='', verbose_name='Number of Sculpture')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # About Artist

    artist_name = models.CharField(max_length=40, verbose_name='Artist Name')
    image_artist = models.ImageField(upload_to='DiscoverTheCollection/artist', blank=False, verbose_name='Image Artist')
    come_from = models.CharField(max_length=30, verbose_name='Country of Artist')
    description_artist = models.TextField(default='About artist . . . ', verbose_name='About Artist')

    # Social networks

    facebook = models.CharField(max_length=80, blank=True, default='e.g. @mirfayziyev', verbose_name='Facebook account')
    twitter = models.CharField(max_length=80, blank=True, default='e.g. @mirfayziyev', verbose_name='Twitter account')
    linkedin = models.CharField(max_length=80, blank=True, default='e.g. @mirfayziyev', verbose_name='LinkedIn account')


# SHOPPING MODELS

class CategoryProduct(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Category ...for... shopping'

class Products(models.Model):
    category = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, blank=False, null=True)

    name = models.CharField(max_length=100, verbose_name='Name of Product')
    image = models.ImageField(upload_to='shop/products/%Y/%m/%d', verbose_name='Image of Product')
    description = models.TextField(default='Describe your Product', verbose_name='Description of Product')
    price = models.FloatField(max_length=20, verbose_name='Price of Product')
    shipping = models.FloatField(max_length=20, default=0, blank=False, null=True, verbose_name='Shipping of Product')
    categories = models.CharField(max_length=60, verbose_name='Category of Product')
    availability = models.CharField(max_length=50, verbose_name='Availability of Product')
    digital = models.BooleanField(default=False, null=True, blank=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Products ...for... shopping'

    @property
    def get_comment_total(self):
        comment = self.comments.all()
        total = sum([item.get_comments for item in comment])
        return total


class Customer(models.Model):
    user = OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = 'Customer ...for... shopping'


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

    @property
    def get_cart_total_shipping(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total_shipping for item in orderitems])
        return total

    @property
    def get_shipping(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_shipping for item in orderitems])
        return total

    class Meta:
        verbose_name_plural = 'Orders ...for... shopping'


class OrderItem(models.Model):
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

    @property
    def get_total_shipping(self):
        total = (self.product.price * self.quantity) + self.product.shipping
        return total

    @property
    def get_shipping(self):
        total = self.product.shipping
        return total

    class Meta:
        verbose_name_plural = 'OrdersItems ...for... shopping'


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name_plural = 'ShippingAddress ...for... shopping'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    post = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True, blank=True, related_name='comments')

    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.TextField()
    email = models.EmailField(max_length=250, default='')
    quantity = models.IntegerField(default=1, blank=True, null=True)

    image = models.ImageField(upload_to='comments', blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    active = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('product-url')

    def __str__(self):
        return self.name

    @property
    def get_comments(self):
        total = self.quantity
        return total


class Event(models.Model):
    organizer = models.CharField(max_length=60, verbose_name='Organizer Name')
    description = models.TextField(default='Can you describe your Museum?')
    image = models.ImageField(upload_to='Event', blank=False, verbose_name='Image to Event')
    cost_adults = models.IntegerField(default=0)
    cost_children = models.IntegerField(default=0)

    address = models.CharField(max_length=200, default='')
    phone = models.CharField(max_length=80, default='')
    email = models.EmailField(max_length=250, default='')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    start_time = models.TimeField(verbose_name='Start-Time', null=True)
    end_time = models.TimeField(verbose_name='End-Time', null=True)

    def __str__(self):
        return self.organizer


class OnlineBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, blank=True)
    exhibition = models.ForeignKey(Exhibition, on_delete=models.CASCADE, null=True, blank=True)

    name = models.CharField(max_length=200, verbose_name='Booker`s name')
    email = models.EmailField(verbose_name='Email')
    number = models.IntegerField(default=0, verbose_name='How many ticket')
    children = models.IntegerField(default=0, verbose_name='How many children')
    description = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home-url')

    class Meta:
        verbose_name_plural = 'Online Bookings'



class EventGallery(models.Model):
    post = models.ForeignKey(Event, default=None, on_delete=models.CASCADE, related_name='galleries')
    images = models.FileField(upload_to='Event/gallery/')

    def __str__(self):
        return self.post.organizer
