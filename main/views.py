import json
import os.path
from itertools import chain

from django.db.models import Q
from django.http import JsonResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views import generic
from django.core.paginator import Paginator
from .models import *
from .forms import ContactForm, CommentForm
import datetime
from egypt.settings import EMAIL_HOST_USER


# Create your views here.

class HomeView(generic.TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # cart items
        if self.request.user.is_authenticated:
            customer = self.request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitem_set.all()
            cartItems = order.get_cart_items
        else:
            items = []
            order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
            cartItems = order['get_cart_items']

        context['cartItems'] = cartItems
        # end cart items

        context['exhibition'] = Exhibition.objects.order_by('-created')[:3]
        context['exhibitions'] = Exhibition.objects.order_by('id')[:3]
        context['discover'] = DiscoverTheCollection.objects.filter(is_active=True).order_by('-created')[:3]
        context['teamdirectors'] = TeamDirectors.objects.all()
        return context


class HomeView_second(generic.TemplateView):
    template_name = 'pages/index-2.html'


class AboutView(generic.TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teamdirectors'] = TeamDirectors.objects.all()
        return context


class TeamView(generic.TemplateView):
    template_name = 'pages/team.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teamdirectors'] = TeamDirectors.objects.all()
        context['teamstaff'] = TeamStaff.objects.all()
        return context


class VenuesView(generic.TemplateView):
    template_name = 'pages/venues.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['country'] = Country.objects.all()
        return context


class VenuesMuseumView(generic.DetailView):
    model = Country
    template_name = 'pages/venues-museum.html'


class ContactView(generic.FormView):
    template_name = 'pages/contact.html'
    form_class = ContactForm

    def post(self, *args, **kwargs):
        if self.request.method == 'POST':
            first_name = self.request.POST['first_name']
            last_name = self.request.POST['last_name']
            email = self.request.POST['email']
            phone = self.request.POST['phone']
            subject = self.request.POST['subject']
            message = self.request.POST['message']
            message = f"From: {first_name} {last_name} \n email: {email} \n phone: {phone} \n theme: {subject} message: {message}"
            send_mail(subject, message, email, ['mirfayziyev5@gmail.com'],
                      fail_silently=False)
            messages.success(self.request, "Your feedback is accepted!")

        else:
            messages.error(self.request, "At this time we cannot receive your request")

        return redirect(self.request.path)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['country'] = Country.objects.all()
        return context


class VisitView(generic.DetailView):
    model = CountryMuseum
    template_name = 'pages/request-visit.html'


class VisitStaticView(generic.DetailView):
    model = CountryMuseum
    template_name = 'pages/request-visit.html'


class CollectionsView(generic.TemplateView):
    template_name = 'pages/collection-antiquties.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['antiquities'] = Antiquities.objects.all()
        return context


class AntiquitiesView(generic.DetailView):
    model = Antiquities
    template_name = 'pages/antiquities-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['antiquities'] = Antiquities.objects.order_by('-created')[:3]
        return context


class CollectionDetailsView(generic.TemplateView):
    model = DiscoverTheCollection
    template_name = 'pages/collection-details.html'

    def download(request, path):
        file_path = os.path.join(settings.MEDIA_ROOT, path)
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type='application/adminupload')
                response['Content-Disposition'] = 'inline;filename=' + os.path.basename(file_path)
                return response
        raise Http404


class CollectionStaticDetailsView(generic.DetailView):
    model = DiscoverTheCollection
    template_name = 'pages/collection-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['colldet'] = DiscoverTheCollection.objects.order_by('-created')[:3]
        return context


class CollectionCulturalView(generic.ListView):
    model = DiscoverTheCollection
    template_name = 'pages/collection-cultural.html'
    context_object_name = 'discover'
    paginate_by = 6

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context[''] = DiscoverTheCollection.objects.all()
    #     return context


class CollectionDrawingView(generic.TemplateView):
    template_name = 'pages/collection-drawing.html'


class CollectionPaintingView(generic.TemplateView):
    template_name = 'pages/collection-painting.html'


class CollectionSculptureView(generic.ListView):
    model = Sculpture
    template_name = 'pages/collection-sculpture.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sculptures'] = Sculpture.objects.all()
        return context


class SculptureView(generic.DetailView):
    model = Sculpture
    template_name = 'pages/sculpture-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sculpture'] = Sculpture.objects.order_by('-created')[:3]
        return context


class BlogDetailView(generic.TemplateView):
    template_name = 'pages/blog-details.html'


class BlogGridView(generic.TemplateView):
    template_name = 'pages/blog-grid.html'


class BlogLargeView(generic.TemplateView):
    template_name = 'pages/blog-large.html'


class BlogMasonryView(generic.TemplateView):
    template_name = 'pages/blog-masonry.html'


class MyAccountView(generic.TemplateView):
    template_name = 'pages/my-account.html'


class DonationView(generic.TemplateView):
    template_name = 'pages/donation.html'


class FaqView(generic.TemplateView):
    template_name = 'pages/faq.html'


class MembershipView(generic.TemplateView):
    template_name = 'pages/memebership.html'


class ExbitionView(generic.TemplateView):
    template_name = 'pages/exhibhition.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exhibition'] = Exhibition.objects.all()
        return context


class EventDetailsView(generic.TemplateView):
    template_name = 'pages/event-details.html'


class EventStaticDetailView(generic.DetailView):
    model = Exhibition
    template_name = 'pages/event-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gallery'] = ExhibitionGallery.objects.all()
        return context

class Event1DetailView(generic.DetailView):
    model = Event
    template_name = 'pages/event-1-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gallery'] = EventGallery.objects.all()
        return context


class Event1View(generic.ListView):
    model = Event
    template_name = 'pages/event-1.html'
    context_object_name = 'events'
    paginate_by = 6


class Event2View(generic.TemplateView):
    template_name = 'pages/event-2.html'


class SearchResultView(generic.ListView):
    model = Exhibition
    template_name = 'pages/search-results.html'

    def get_queryset(self):
        query = self.request.GET.get('search')
        Exhibitions = Exhibition.objects.filter(
            Q(title__icontains=query, organizer__icontains=query)
        )
        Discover = DiscoverTheCollection.objects.filter(
            Q(title__icontains=query)
        )

        return Exhibitions, Discover


class BookingView(generic.CreateView):
    model = OnlineBooking
    template_name = 'pages/online-booking.html'
    fields = ['exhibition', 'event', 'name', 'email', 'number', 'children', 'description']

# Shopping Part

class ProductView(generic.ListView):
    model = Products
    template_name = 'pages/proudcts.html'
    paginate_by = 12
    context_object_name = 'comment'


    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        category = self.request.GET.get('category')
        if self.request.user.is_authenticated:
            customer = self.request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitem_set.all()
            cartItems = order.get_cart_items
        else:
            items = []
            order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
            cartItems = order['get_cart_items']


        if category == None:
            context['products'] = Products.objects.all()
        elif category == 'upcoming':
            context['products'] = Products.objects.order_by('-created')
        else:
            context['products'] = Products.objects.filter(category__name=category)
        context['category'] = CategoryProduct.objects.all()
        context['cartItems'] = cartItems
        return context


class ProductDetailView(generic.DetailView):
    model = Products
    template_name = 'pages/product-details.html'
    context_object_name = 'produc'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        post = get_object_or_404(Products, pk=1)

        comments = post.comments.filter(active=True)
        new_comment = None
        # Comment posted
        if self.request.method == 'POST':
            comment_form = CommentForm(data=self.request.POST)
            if comment_form.is_valid():
                # Create Comment object but don't save to database yet
                new_comment = comment_form.save(commit=False)
                # Assign the current post to the comment
                new_comment.post = post
                # Save the comment to the database
                new_comment.save()
        else:
            comment_form = CommentForm()


        if self.request.user.is_authenticated:
            customer = self.request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitem_set.all()
            cartItems = order.get_cart_items
        else:
            items = []
            order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
            cartItems = order['get_cart_items']

        context['items'] = items
        context['comment_form'] = comment_form
        context['comments'] = comments
        context['order'] = order
        context['cartItems'] = cartItems
        context['products'] = Products.objects.all()

        return context


def comment(request, pk):
    post = get_object_or_404(Products, id=pk)
    template_name = 'pages/comment-add.html'

    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})






class CartView(generic.TemplateView):
    template_name = 'pages/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            customer = self.request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitem_set.all()
            cartItems = order.get_cart_items
        else:
            items = []
            order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
            cartItems = order['get_cart_items']
        context['items'] = items
        context['order'] = order
        context['cartItems'] = cartItems
        return context


# Function for shopping

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('ProductId', productId)

    customer = request.user.customer
    product = Products.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    elif action == 'delete':
        orderItem.quantity = 0

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == order.get_cart_total_shipping:
            order.complete = True
        order.save()

        if order.shipping == True:
            ShippingAddress.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                zipcode=data['shipping']['zipcode'],
            )
    else:
        print('user is not legged in')

    return JsonResponse('Payment complete!', safe=False)


class CheckOutView(generic.TemplateView):
    template_name = 'pages/checkhout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            customer = self.request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitem_set.all()
            cartItems = order.get_cart_items
        else:
            items = []
            order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
            cartItems = order['get_cart_items']
        context['items'] = items
        context['order'] = order
        context['cartItems'] = cartItems
        return context


# END Shopping Views
