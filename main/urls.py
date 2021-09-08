from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home-url'),
    path('home2/', views.HomeView_second.as_view(), name='home2'),
    path('about/', views.AboutView.as_view(), name='about-url'),
    path('team/', views.TeamView.as_view(), name='team-url'),
    path('contact/', views.ContactView.as_view(), name='contact-url'),
    path('venues/', views.VenuesView.as_view(), name='venues-url'),
    path('venues-museum/<int:pk>/', views.VenuesMuseumView.as_view(), name='venues-museum-url'),
    path('visit/1', views.VisitView.as_view(), name='visit-url'),
    path('visit/<int:pk>/', views.VisitStaticView.as_view(), name='visits-url'),
    path('collections/', views.CollectionsView.as_view(), name='collection-url'),
    path('collection-details/1', views.CollectionDetailsView.as_view(), name='collection_detail-url'),
    path('collection-details/<int:pk>/', views.CollectionStaticDetailsView.as_view(), name='collection_details-url'),
    path('antiquities-details/<int:pk>/', views.AntiquitiesView.as_view(), name='antiquities-details-url'),
    path('collection-cultural/', views.CollectionCulturalView.as_view(), name='collection-cultural-url'),
    path('collection-drawing/', views.CollectionDrawingView.as_view(), name='collection-drawing-url'),
    path('collection-painting/', views.CollectionPaintingView.as_view(), name='collection-painting-url'),
    path('collection-sculpture/', views.CollectionSculptureView.as_view(), name='collection-sculpture-url'),
    path('sculpture-details/<int:pk>/', views.SculptureView.as_view(), name='sculpture-details-url'),
    path('blog-details/', views.BlogDetailView.as_view(), name='blog-detail-url'),
    path('blog-grid/', views.BlogGridView.as_view(), name='blog-grid-url'),
    path('blog-large/', views.BlogLargeView.as_view(), name='blog-large-url'),
    path('blog-masonry/', views.BlogMasonryView.as_view(), name='blog-masonry-url'),
    path('products/', views.ProductView.as_view(), name='product-url'),
    path('product-details/<int:pk>/', views.ProductDetailView.as_view(), name='product-details-url'),
    path('cart/', views.CartView.as_view(), name='cart-url'),
    path('checkout/', views.CheckOutView.as_view(), name='checkout-url'),
    path('update-item/', views.updateItem, name='update-item'),
    path('process-order/', views.processOrder, name='process-order'),
    path('myaccount/', views.MyAccountView.as_view(), name='myaccount-url'),
    path('donation/', views.DonationView.as_view(), name='donation-url'),
    path('faq/', views.FaqView.as_view(), name='faq-url'),
    path('membership/', views.MembershipView.as_view(), name='membership-url'),
    path('exbition/', views.ExbitionView.as_view(), name='exbition-url'),
    path('event-details/', views.EventDetailsView.as_view(), name='event-detail-url'),
    path('event-details/<int:pk>/', views.EventStaticDetailView.as_view(), name='eventstatic-detail-url'),
    path('comment-add/<int:pk>/', views.comment, name='comment-url'),
    path('search-results/', views.SearchResultView.as_view(), name='search-results-url'),
    path('online-booking/<int:pk>/', views.BookingView.as_view(), name='booking-url'),
    path('event-1/', views.Event1View.as_view(), name='event-1-url'),
    path('event-2/', views.Event2View.as_view(), name='event-2-url'),
    path('event-1-details/<int:pk>/', views.Event1DetailView.as_view(), name='event1-details-url'),






]
