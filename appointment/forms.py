from django import forms
from django.forms.widgets import DateInput
from appointment.models import AppointmentDetails,BookedAppointment

class AddAppointmentForm(forms.ModelForm):

	class Meta:
		model=AppointmentDetails
		fields=('appointment_date','appointment_day','appointment_start_time','appointment_end_time')
		widgets = {
			'appointment_date': DateInput(attrs={'type': 'date'}),
			'appointment_start_time' :  DateInput(attrs={'type': 'time'}),
			'appointment_end_time' :  DateInput(attrs={'type': 'time'}),

		}
		label={
			'appointment_date':'Appointment Date',
			'appointment_day':'Appointment Day',
			'appointment_start_time':'Start Time',
			'appointment_start_time':'End Time',


		}
	def __init__(self,*args,**kwargs):
		super(AddAppointmentForm,self).__init__(*args,**kwargs)
		self.fields['appointment_day'].error_messages.update({'required':'Please select a day'})
		self.fields['appointment_start_time'].error_messages.update({'required':'Please mention a start time'})
		self.fields['appointment_end_time'].error_messages.update({'required':'Please mention a end time'})
		self.fields['appointment_date'].error_messages.update({'required':'Please select a date'})


class BookedAppointmentForm(forms.ModelForm):

	class Meta:
		model=BookedAppointment
		fields=('reason',)
	def __init__(self,*args,**kwargs):
		super(BookedAppointmentForm,self).__init__(*args,**kwargs)
		self.fields['reason'].error_messages.update({'required':'Please mention a reason for appoinment,at most 100 characters'})
