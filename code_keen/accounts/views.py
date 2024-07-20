from django.shortcuts import render
from rest_framework_simplejwt.tokens import RefreshToken
from  .tasks import add
# Create your views here.
from .tasks import add
from django.views.decorators.csrf import csrf_exempt
def home(request):
    add.delay(2,3)
    return render(request,'index.html')
def success(request):
    return render(request,'success.html')
def cancel(request):
    return render(request,'cancel.html')

def landing(request,id):
    data=Product.objects.get(id=id)
    return render(request,'landing_page.html',{"data":data})
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    res=add.delay(2,3)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


import stripe
from django.conf import settings
from django.http import JsonResponse
from keen_app.models import Product
stripe.api_key = 'sk_test_51PZuCnRxvTbd21DG0X52ncxCaTY25LmSxBmwJKS0h9SicunQM2aeorLnxnifrzos28KqFSq4BLUZAU0uaHI9galM00qOZvTui2'
from django.http import HttpResponse

@csrf_exempt
def my_webhook_view(request):
  payload = request.body
  sig_header = request.META['HTTP_STRIPE_SIGNATURE']
  event = None

  try:
    event = stripe.Webhook.construct_event(
      payload, sig_header, endpoint_secret
    )
  except ValueError as e:
    # Invalid payload
    return HttpResponse(status=400)
  except stripe.error.SignatureVerificationError as e:
    # Invalid signature
    return HttpResponse(status=400)

  # Passed signature verification
  return HttpResponse(status=200)
  if event['type'] == 'checkout.session.completed':
    session = event['data']['object']

  return HttpResponse(status=200)
def create_checkout_session(request, id):
    print(id,type(id),'====================')
    p_data = Product.objects.get(id=id)
    print(p_data.price)
    YOUR_DOMAIN = 'https://127.0.0.1:8000'  
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',  # Replace with your currency
                        'product_data': {
                            'name': p_data.p_name,  # Assuming Product model has a 'name' field
                        },
                        'unit_amount': p_data.price,  # Assuming price is in the smallest currency unit, e.g., cents for USD
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=f'{YOUR_DOMAIN}/accounts/success',
            cancel_url=f'{YOUR_DOMAIN}/accounts/cancel',
        )
    except Exception as e:
        print(e,'=====================')

    return JsonResponse({'id': checkout_session.id})