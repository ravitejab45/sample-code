from django.shortcuts import render_to_response
from django.template import RequestContext
import cart


def show_cart(request):
  cart_item_count = cart.cart_item_count(request)
  page_title = 'Shopping Cart'
  return render_to_response('cart/cart.html', locals(),
                            context_instance=RequestContext(request))