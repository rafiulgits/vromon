from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, HttpResponse

from generic.variables import LOGIN_URL

from tourguide.forms import (GuideProfileForm, SpotGuideForm, SpotGuideUpdateForm,
                        SpotGuideMediaForm)
from tourguide.models import GuideProfile, SpotGuide, Spot, SpotGuideMedia


@login_required(login_url=LOGIN_URL)
def join(request):
    if request.user.is_guide:
        guide_profile = GuideProfile.objects.get(account_id=request.user.id)
        return redirect('/guide/' + str(guide_profile.uid) + '/')
    context = {}
    if request.method == 'POST':
        form = GuideProfileForm(request.POST, user=request.user)
        if form.is_valid():
            description = form.cleaned_data['description']
            guide_profile = GuideProfile(account=request.user)
            guide_profile.description = description
            guide_profile.save()

            request.user.is_guide = True
            request.user.save()

            return HttpResponse('Profile Created')

    form = GuideProfileForm(user=request.user)
    context['form'] = form

    return render(request, 'home/guide/join.html', context)


@login_required(login_url=LOGIN_URL)
def update(request):
    pass


def dashboard(request, uid):
    try:
        context = {}
        guide = GuideProfile.objects.get(uid=uid)
        spots = SpotGuide.objects.filter(guide=guide)

        context['guide'] = guide
        context['profile'] = guide.account
        context['spots'] = spots

        return render(request, 'home/guide/dashboard.html', context)
    except ObjectDoesNotExist as e:
        return HttpResponse('<h1 align="center">' +
                            'Guide Profile Not Found</h1>')


@login_required(login_url=LOGIN_URL)
def new_page(request, uid):
    try:
        guide_profile = GuideProfile.objects.get(uid=uid)
        if guide_profile.account_id == request.user.id:
            context = {}

            if request.method == 'POST':
                form = SpotGuideForm(request.POST, request.FILES, guide=guide_profile)
                if form.is_valid():
                    spot = form.cleaned_data['spot']
                    details = form.cleaned_data['details']
                    logo = form.cleaned_data['logo']

                    SpotGuide.objects.create(guide=guide_profile, spot=spot, details=details,
                                             logo=logo)

                    return redirect('/guide/' + uid + '/')

            form = SpotGuideForm(guide=guide_profile)
            context['form'] = form

            return render(request, 'home/guide/new_page.html', context)

    except ObjectDoesNotExist as e:
        pass

    return HttpResponse('Invalid request')


def page(request, uid, name):
    try:
        spot_id = Spot.objects.get(name__iexact=name).uid
        page = SpotGuide.objects.get(guide_id=uid, spot_id=spot_id)
        media = SpotGuideMedia.objects.filter(spot_guide_id=page.uid)

        context = {}

        if page.guide.account == request.user:
            form = SpotGuideMediaForm()
            context['form'] = form

        context['page'] = page
        context['media'] = media

        return render(request, 'home/guide/page.html', context)
    except ObjectDoesNotExist as e:
        pass

    return HttpResponse('request not found')


@login_required(login_url=LOGIN_URL)
def page_update(request, uid, name):
    try:
        spot_id = Spot.objects.get(name__iexact=name).uid
        page = SpotGuide.objects.get(guide_id=uid, spot_id=spot_id)

        if request.user != page.guide.account:
            return HttpResponse('Invalid request')
        context = {}

        if request.method == 'POST':
            form = SpotGuideUpdateForm(request.POST, guide=page.guide, spot_guide=page)
            if form.is_valid():
                page.details = form.cleaned_data['details']
                page.spot = form.cleaned_data['spot']
                page.save()

                return redirect('/guide/' + uid + '/' + 'spot/' + name + '/')

        form = SpotGuideUpdateForm(guide=page.guide, spot_guide=page)
        context['form'] = form

        return render(request, 'home/guide/page_update.html', context)
    except ObjectDoesNotExist as e:
        pass

    return HttpResponse('request not found')


@login_required(login_url=LOGIN_URL)
def upload_image(request, uid, name):
    try:
        spot_id = Spot.objects.get(name__iexact=name).uid
        page = SpotGuide.objects.get(guide_id=uid, spot_id=spot_id)

        if request.user != page.guide.account:
            return HttpResponse('Invalid request')
        context = {}

        if request.method == 'POST':
            form = SpotGuideMediaForm(request.POST, request.FILES)
            if form.is_valid():
                media = SpotGuideMedia(spot_guide=page)
                media.image = form.cleaned_data['image']
                media.save()

                return redirect('/guide/' + uid + '/' + 'spot/' + name + '/')

    except ObjectDoesNotExist as e:
        pass

    return HttpResponse('request not found')