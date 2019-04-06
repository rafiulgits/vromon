from django.shortcuts import render, redirect, HttpResponse


def single(request, uid):
	return HttpResponse('Single place working')


def all(request):
	return HttpResponse('all place working')