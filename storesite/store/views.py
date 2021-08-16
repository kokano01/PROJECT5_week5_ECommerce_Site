from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.core.mail import EmailMessage, message
from django.conf import settings
from django.template.loader import render_to_string

from .forms import UserForm, CartForm
from .models import Item, Cart


# Create your views here.

def index(request):
    products = [
        {   
            'image': 'https://c1.neweggimages.com/ProductImageCompressAll1280/11-139-164-V21.jpg',
            'name': 'CORSAIR 5000D Tempered Glass Mid-Tower ATX PC Case, Black',
            'price': 149.99,
            'description': 'Clean and Cool \nSolid Steel Front Panel \nCORSAIR RapidRoute Cable Management System \nTwo Included 120mm Fans \nMotherboard Tray with Customizable Fan Mounts'
        },
        {
            'image': 'https://c1.neweggimages.com/ProductImageCompressAll300/14-126-510-V14.jpg?ex=2',
            'name': 'ASUS TUF Gaming NVIDIA GeForce RTX 3080 Ti Graphics Card',
            'price': 2079.49,
            'description': '12GB 384-Bit GDDR6X \OC mode: 1695 MHz (Boost Clock) /Gaming mode: 1665 MHz (Boost Clock) /2 x HDMI 2.1 3 x DisplayPort 1.4a /10240 CUDA Cores /PCI Express 4.0 x16'
        },
        {
            'image': 'https://c1.neweggimages.com/ProductImageCompressAll1280/19-118-122-V16.jpg',
            'name': "Intel Core i9-10900K Comet Lake 10-Core 3.7 GHz LGA 1200 125W",
            'price': 539.99,
            'description': '14nm 125W /20MB L3 Cache /Intel UHD Graphics 630 /Compatible with Intel 500 Series Boards'
        },
        {   
            'image': 'https://c1.neweggimages.com/ProductImageCompressAll300/13-119-372-01.jpg?ex=2',
            'name': 'ASUS PRIME Z590-P LGA 1200 Intel Z590 SATA 6Gb/s Motherboard',
            'price': 189.99,
            'description': 'Intel Z590 xSupports 11th Gen / 10th Gen Intel Core Processors xSupports Intel Pentium Gold and Celeron Processors'
        },
    
        {   
            'image': 'https://c1.neweggimages.com/ProductImageCompressAll1280/17-438-092-01.jpg',
            'name': 'EVGA SuperNOVA 850 G3, 220-G3-0850-X1',
            'price': 139.99,
            'description': 'ATX12V / EPS12V xFull Modular x80 PLUS GOLD Certified x100 - 240 V 50 - 60 Hz'
        },
    
        {   
            'image': 'https://c1.neweggimages.com/ProductImageCompressAll1280/20-236-708-V02.jpg',
            'name': 'CORSAIR Vengeance RGB Pro SL 32GB (2 x 16GB)',
            'price': 172.99,
            'description': 'DDR4 3600 (PC4 28800) /Timing 18-22-22-42 /CAS Latency 18 /Voltage 1.35V'
        },
    
        
    ]
    context = {'product': products, 'page_title': 'STORE'}
    return render(request, 'store/index.html', context)

def productPage(request):
    items = Item.objects.all()
    context = {
        'product': items,
        'page_title': 'SHOP'
    }
    return render(request, 'store/productpage.html', context)

def individualItem(request, item_id):
    item = Item.objects.get(id=item_id)
    context = {'p': item}
    return render(request, 'store/viewproduct.html', context)


@login_required(login_url='store-login')
def addtoCart(request):
    cart = CartForm(request.POST)
    if cart.is_valid():
        cart.save()
    messages.success(request, "Added to cart")

    return redirect('store-productpage')

# def myCart(request):
#     if request.method == "POST":
#         product = request.POST.get("product") # comes from the name attribute in the html tag
#         username = request.POST.get("username")
#     return render(request, 'store/cart.html')



def myCart(request, item_id):
    post = Item.objects.get(id=item_id)
    form = CartForm(request.POST, instance=post)
    if request.method == "POST":
        form = CartForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "success")
        return redirect('store-viewinfo', item_id=item_id)

    context = {'form': form, 'p': post}        
    return render(request, 'store/cart.html', context)
    


def registerPage(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()

        user = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")

        context = {'username': user}
        template = render_to_string('store/emailtemplate.html', context)


        email_message = EmailMessage(
            'Welcome to the store',
            template,
            settings.EMAIL_HOST_USER,
            [email]
        )

        email_message.fail_silently = False
        email_message.send()

        messages.success(request, "Account was created for " + user)



        return redirect('store-login')
    context = {
        'form': form
    }
    return render(request, 'store/register.html', context)

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username") # comes from the name attribute in the html tag
        password = request.POST.get("password1")

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            # print(f'{user} is logged in')
            messages.success(request, "Welcome")
            return redirect('store-productpage')
            
        messages.info(request, "Incorrect username or password")
    return render(request, 'store/login.html')

@login_required(login_url='store-login')
def logoutUser(request):
    logout(request)
    messages.success(request, "Logged out")
    return redirect('store-login')