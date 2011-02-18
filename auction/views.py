from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from auction.models import *

def receipt(request, id):
    person = get_object_or_404(Person,pk=id)
    return render_to_response('receipt.html', {
                'person':person,
                })

