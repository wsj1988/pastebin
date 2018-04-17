# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from django.shortcuts import render
from django.views import generic
from models import Paste
from forms import PasteForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


class IndexView(generic.ListView):
    model = Paste
    template_name = 'paste/paste_list.html'


class DetailView(generic.DetailView):
    model = Paste
    template_name = 'paste/paste_detail.html'

    
def create_info(request):
    if request.method == 'POST':
        form = PasteForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            success_url = reverse('paste:display_info')
            # print 'in create_info: ', success_url
            return HttpResponseRedirect(success_url)
        else:
            print form.errors
    else:
        form = PasteForm()

    return render(request, 'paste/paste_form.html', {'form': form})
