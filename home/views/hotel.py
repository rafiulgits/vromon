from django.shortcuts import render, redirect, HttpResponse


def single(request, uid):
	return HttpResponse('Single Hotel working')


def all(request):
	return HttpResponse('all hotel working')