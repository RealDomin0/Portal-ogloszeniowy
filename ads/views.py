from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from .models import Ad,AdImage

def list_of_ads(request):
    ads = Ad.objects.all().order_by('-created_at')
    return render(
        request,
        'ads/list.html',
        {'ads': ads}
    )

def ads_detail(request, id):
    ad = get_object_or_404(Ad, id=id)
    return render(
        request,
        'ads/detail.html',
        {'ad': ad})

