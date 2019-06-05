from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404

from django.conf import settings

from blog.models import BlogPage


def like(request, page_id):
    page = get_object_or_404(BlogPage, pk=page_id)
    page.likes += 1
    page.save()

    response_data = {}
    response_data['likes'] = page.likes

    response = JsonResponse(response_data)
    response.set_signed_cookie('plike_' + str(page.id), True, settings.SECRET_KEY, max_age=31536000)

    return response


def unlike(request, page_id):
    page = get_object_or_404(BlogPage, pk=page_id)
    page.likes -= 1
    page.save()
    
    response_data = {}
    response_data['likes'] = page.likes

    response = JsonResponse(response_data)
    response.delete_cookie('plike_' + str(page.id))

    return response
