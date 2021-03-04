from django.shortcuts import render, redirect
from patient.forms import *
from django.contrib.auth import authenticate, logout,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from patient.models import Profile
from django.db import transaction
from patient.models import *
# Create your views here.

from django.shortcuts import render, HttpResponse
import requests

from Health.forms import *
from api.models import Disease
from api import diseaseml
# from . import heart
from patient.heart import pred_heart
from patient.Diabetes import pred
from patient.pneumonia import pred1
from api.diseaseml import pred
from .models import Image
from django.contrib.auth.models import Group

from django.db.models import Q
# Pagination import 
# from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required(login_url='patient_login')
#for Pnemonia check
def showimage(request):  
	# lastimage= Image.objects.last()
	# if lastimage == None:
	# 	lastimage = ''
	# else:
	# imagefile= lastimage.imagefile
	form= ImageForm(request.POST or None, request.FILES or None)
	contex={'form': form}
	if form.is_valid():
		form.save()
		lastimage= Image.objects.last()
		imagefile= lastimage.imagefile
		print(imagefile)
		sur=pred1(imagefile)
		context= {
			'imagefile':imagefile,
			'form': form,
			'sur':sur,
			}
		return render(request, 'patient/image.html', context)
	sur = ' '
	imagefile = ''
	context= {
		'imagefile':imagefile,
		'form': form,
		'sur':sur,
		}
	return render(request, 'patient/image.html', context)
	
@login_required(login_url='patient_login')
#For Diabetes Disease Prediction
def Diabetes(request):
	if request.method=="GET":
		diabetes_form=DiabetesForm()
		contex={
			'diabetes_form':diabetes_form
		}
		return render(request,'patient/diabetes.html', contex)
	elif  request.method=="POST":
		diabetes_form=DiabetesForm(request.POST)
		if diabetes_form.is_valid:
			diabetes_form.save()
			from patient.models import Diabetes
			ob=Diabetes.objects.latest('id')
			print(ob)
			sur=pred(ob)
			sur=", ".join( repr(e) for e in sur).strip("''")
			if sur== '1':
				name= "Yes, You are suffering  from Diabetes problems"
				disease_name="Diabetes"
				# saving  user information who predict disease and suggesting doctors
				predict=WhoPredictDisease(predict_by=request.user.profile,predicted_disease=disease_name)
				predict.save()
				disease=Disease1.objects.filter(name__icontains=disease_name)
				listDoctorID=[]
				for d in disease:
					listDoctorID.append(d.doctor.id)
				disease_doctor_list=DoctorInfo.objects.filter(Q(id__in=listDoctorID))
				context={
					'sur':'You are suffering from diabetes problem',
					'disease_doctor_list':disease_doctor_list,
				}
			elif sur=='0':
				 context={
					'sur':'You are not suffering from diabetes problem',
					# 'disease_doctor_list':disease_doctor_list
				}
			return render(request,'patient/diabetes_results.html', contex)
		# else:
		#     return render(request,'patient/diabetes.html',context)
		#     pass



@login_required(login_url='patient_login')
# For heart Disease predicton
def heart(request):
	if request.method=="GET":
		heart_form=HeartForm()
		contex={
			'heart_form':heart_form
		}
		return render(request,'patient/heart.html', contex)
	elif  request.method=="POST":
		heart_form=HeartForm(request.POST)

		if heart_form.is_valid:
			heart_form.save()
			ob=Heart.objects.latest('id')
			sur=pred_heart(ob)
			sur=", ".join( repr(e) for e in sur).strip("''")

			if sur== '1':
				name= "Yes, You are suffuring from heart problem"
			elif sur=='0':
				name="You are not suffuring from heart problme"
				
			contex={
				'sur':name,
			}
			return render(request,'patient/heart_results.html', contex)


@login_required(login_url='patient_login')
#Disease prediction as well dashboard !!
def dashboard(request):
	if request.method =="POST":
		contex = {}
		if request.POST.get('value1'):
			disease = Disease()
			value1 = request.POST.get('value1')
			
			value2 = request.POST.get('value2')
			
			value3 = request.POST.get('value3')
			
			value4 = request.POST.get('value4')
			
			value5 = request.POST.get('value5')
			
			value6 = request.POST.get('value6')

			disease.value_1 = value1
			disease.value_2 = value2
			disease.value_3 = value3
			disease.value_4 = value4
			disease.value_5 = value5
			disease.value_6 = value6
			disease.save()
			ob = Disease.objects.latest('id')
			sur = pred(ob)
			predicted_disease_name = sur[0][0]
			symptoms = sur[1]
		
			value1 = symptoms[0]
			value2 = symptoms[1]
			value3 = symptoms[2]
			value4 = symptoms[3]
			value5 = symptoms[4]
			value6 = symptoms[5]
			
			# patient who predrict disease is save in now database
			predict=WhoPredictDisease(predict_by=request.user.profile,predicted_disease=predicted_disease_name)
			predict.save()
			disease=Disease1.objects.filter(name__icontains=predicted_disease_name)
			listDoctorID=[]
			for d in disease:
				listDoctorID.append(d.doctor.id)
			disease_doctor_list=DoctorInfo.objects.filter(Q(id__in=listDoctorID))
						
		   

		return render(request, 'patient/showDisease.html', context = {"Predicted_disease":predicted_disease_name,'disease_doctor_list':disease_doctor_list,"value1": value1, 		"value2":value2, "value3":value3, "value4": value4, "value5":value5, "value6": value6})

	else:
		return render(request, 'patient/dashboard.html')
	

@login_required(login_url='patient_login')

def form(request):
	pass

@login_required(login_url='patient_login')
def feedback(request):
	page=request.GET.get('page',1)
	feedbacks=Feedback.objects.filter(Q(uploaded_by=request.user.profile)).order_by('-id')
	paginator=Paginator(feedbacks,8)
	try:
		feedbacks=paginator.page(page)
	except PageNotAnInteger:
		feedbacks=paginator.page(1)
	except EmptyPage:
		feedbacks=paginator.page(paginator.num_pages)
	context={
		'feedbacks':feedbacks
	}
	return render(request,'patient/feedback.html',context)

@login_required(login_url='patient_login')
def feedback_detail(request,pk):
	feedback=Feedback.objects.get(id=pk,uploaded_by=request.user.profile)
	print(feedback)
	context={
		"feedback":feedback
	}
	return render(request,'patient/feedback_detail.html',context)

@login_required(login_url='patient_login')
def feedback_delete(request,pk):
	try:
		feedback=Feedback.objects.get(id=pk,uploaded_by=request.user.profile)
	except:
		return redirect('feedback')
	feedback.delete()
	return redirect('feedback')

@login_required(login_url='patient_login')
def feedback_edit(request,pk):
	try:
		feedback=Feedback.objects.get(id=pk,uploaded_by=request.user.profile)
	except:
		return redirect('feedback')
	if request.method=='POST':   
		feedback_edit_form=FeedbackForm(request.POST or None,request.FILES,instance=feedback)
		if feedback_edit_form.is_valid():
			update=feedback_edit_form.save(commit=False)
			update.uploaded_by=request.user.profile
			update.save()
			return redirect('feedback')
		else:
			context={
				'feedback_edit_form':feedback_edit_form,
				'feedback':feedback
			}
			return render(request,'patient/feedback_edit_form.html',context)
	else:
		feedback_form=FeedbackForm(request.POST or None,request.FILES,instance=feedback)
		context={
			'feedback_form':feedback_form,
			'feedback':feedback
		}
		return render(request,'patient/feedback_edit_form.html',context)

@login_required(login_url='patient_login')
def feedback_add(request):
	if request.method=='POST':
		feedback_add_form=FeedbackForm(request.POST or None,request.FILES or None)
		if feedback_add_form.is_valid():
			add_feedback=feedback_add_form.save(commit=False)
			add_feedback.uploaded_by=request.user.profile
			add_feedback.save()
			return redirect('feedback')
		else:
			context={
				'feedback_add_form':feedback_add_form
			}
			return render(request,'patient/feedback_add_form.html',context)
	else:
		feedback_add_form=FeedbackForm()
		context={
			'feedback_add_form':feedback_add_form
		}
		return render(request,'patient/feedback_add_form.html',context)

@login_required(login_url='patient_login')
def search_doctor(request):
	context={}
	if request.method=="POST":
		search_term=request.POST.get('term')
		disease=Disease1.objects.filter(name__icontains=search_term)
		if search_term==None:
			search_term=""
		doctorID=[]
		for d in disease:
			doctorID.append(d.doctor.id)
		# print(doctor_name)
		# doctors=DoctorInfo.objects.filter(Q())
		doctors=DoctorInfo.objects.filter(id__in=doctorID) or DoctorInfo.objects.filter(Q(user__first_name__icontains=search_term)|Q(user__last_name__icontains=search_term)|Q(department__icontains=search_term))
		context={
			'doctors':doctors,
			# 'count':count
		}
		return render(request,'patient/search_doctor.html',context)
	# else:
	else:
		doctors=[]
		context={
			"doctors":doctors,
			# "count":count
		}
		return render(request,'patient/search_doctor.html',context)

@login_required(login_url='patient_login')
def doctor_profile(request,pk):
	doctor=DoctorInfo.objects.get(id=pk)
	# print(doctor.__dict__)
	context={
		'doctor':doctor,
	}
	return render(request,'patient/doctor_profile.html',context)


@login_required(login_url='patient_login')
def my_profile(request):
	return render(request,'patient/my_profile.html')



@login_required(login_url='patient_login')
def home(request):
	# if request.method=='GET':
	page=request.GET.get('page',1)
	search_term=request.GET.get('term')
	if search_term==None:
		search_term=""
	doctors=DoctorInfo.objects.filter(Q(user__first_name__icontains=search_term) |Q(user__last_name__icontains=search_term)|Q(address__icontains=search_term)| Q(department__icontains=search_term))
	# doctors=DoctorInfo.objects.all()
	paginator=Paginator(doctors,8)
	try:
		doctors=paginator.page(page)
	except PageNotAnInteger:
		doctors=paginator.page(1)
	except EmptyPage:
		doctors=paginator.page(paginator.num_pages)
	context={
		'doctors':doctors,
	} 
	return render(request,'patient/home.html',context)
	# elif request.method=='POST':
	#     search_term=request.POST.get('term')
	#     if search_term==None:
	#         search_term=""
	#     doctors=DoctorInfo.objects.filter(Q(name__icontains=search_term) | Q(address__icontains=search_term))
	#     context={
	#         'doctors':doctors
	#     }
	#     return render(request,'patient/home.html',context)




def patient_register(request):
	patient_register=UserForm()
	if request.method == 'POST':
		patient_register= UserForm(request.POST)
		if patient_register.is_valid():
			user=patient_register.save()
			my_patient_group=Group.objects.get_or_create(name="PATIENT")
			my_patient_group[0].user_set.add(user)
			return redirect("patient_login")
		else:
			contex={
				'patient_register':patient_register
			}
			print("in valid inputs")
			return render(request, 'patient/register.html', contex)
	else:     
		patient_register=UserForm()
		contex={
			'patient_register':patient_register,
		}
		return render(request, 'patient/register.html', contex)





@login_required(login_url='patient_login') 
@transaction.atomic   
def patient_profile(request):
	if request.method=='POST':
		user_form=UpdateForm(request.POST,instance=request.user)
		patient_profile=ProfileForm(request.POST ,request.FILES ,instance=request.user.profile)
		if user_form.is_valid() and patient_profile.is_valid():
			user_form.save()
			patient_profile.save()
			return redirect("my_profile")
		else:
			context={
				'user_form':user_form,
				'patient_profile':patient_profile
			}
			print('invalid inputs')
			return render(request,'patient/profile.html',context)

	else:
		user_form=UpdateForm(instance=request.user)
		patient_profile=ProfileForm(instance=request.user.profile)
		context={
			'user_form':user_form,
			'patient_profile':patient_profile,
		}
		return render(request,'patient/profile.html',context)


def patient_login(request):
	if request.method=="POST":
		username = request.POST.get('username')       
		password = request.POST.get('password') 
		user =authenticate(request, username=username, password=password)
		if user is not None:
			login(request,user)
			return redirect('home')
		else:
			messages.info(request, "Please enter valid credentials")
			# messages.info(request, "Invalid username or password")
			return render(request, 'patient/login.html')
	else:
		return render(request, 'patient/login.html')

def logoutpatient(request):
	print("logout user")
	logout(request)
	return redirect("/")
