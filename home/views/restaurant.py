from django.shortcuts import render, redirect, HttpResponse


def single(request, uid):
	return HttpResponse('Single restaurant working')


def all(request):
	return HttpResponse('all restaurant working')