from django.shortcuts import render
from django import forms
from .models import studentData
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
class MyStudentForm(forms.Form):
	name = forms.CharField()
	email = forms.CharField()

def index(request):
	return render(request, 'app/index.html',{
			"forms":MyStudentForm,
			"records": studentData.objects.all()
		})

def create(request):
	if request.method == "POST":
		name = request.POST['name']
		email = request.POST['email']
		student = studentData(name=name, email=email)
		student.save()

	return HttpResponseRedirect(reverse('index'))

def delete(request):
	if request.method == "POST":
		studentId = request.POST['delete']
		studentData.objects.get(pk=studentId).delete()

	return HttpResponseRedirect(reverse('index'))

def update(request):
	if request.method == "POST":
		studentId = request.POST['studentId']
		name = request.POST['user'] 
		email = request.POST['email']
		studentData.objects.filter(pk=studentId).update(name=name, email=email)

		return HttpResponseRedirect(reverse('index'))


	studentId = request.GET.get('sId')

	return render(request, 'app/update.html',{
			"record":studentData.objects.get(pk=studentId)

		})