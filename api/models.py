from django.db import models

# Create your models here.
class Disease(models.Model):
    value_1 = models.CharField(max_length = 50)
    value_2 = models.CharField(max_length = 50)
    value_3 = models.CharField(max_length = 50)
    value_4 = models.CharField(max_length = 50)
    value_5 = models.CharField(max_length = 50)
    value_6 = models.CharField(max_length = 50)


    def to_dict(self):
        return{
            'value_1': self.value_1,
            'value_2': self.value_2,
            'value_3': self.value_3,
            'value_4': self.value_4,
            'value_5': self.value_5,
            'value_6': self.value_6
        }
    # receiving_blood_transfusion=models.CharField(max_length=50)
    # family_history=models.CharField(max_length=50)
    # headache=models.CharField(max_length=50)
    # receiving_unsterile_injections=models.CharField(max_length=50)
    # diarrhoea=models.CharField(max_length=50)
    # weakness_of_one_body_side=models.CharField(max_length=50)
    # coma=models.CharField(max_length=50)
    # stomach_bleeding=models.CharField(max_length=50)
    # ulcers_on_tongue=models.CharField(max_length=50)
    # lack_of_concentration=models.CharField(max_length=50)
    # chills=models.CharField(max_length=50)
    # loss_of_balance=models.CharField(max_length=50)
    # muscle_weakness=models.CharField(max_length=50)
    # unsteadiness=models.CharField(max_length=50)
    # back_pain=models.CharField(max_length=50)
    # dizziness=models.CharField(max_length=50)
    # blackheads=models.CharField(max_length=50)
    # shivering=models.CharField(max_length=50)
    # breathlessness=models.CharField(max_length=50)
    # continuous_sneezing=models.CharField(max_length=50)
    # abnormal_menstruation=models.CharField(max_length=50)
    # red_sore_around_nose=models.CharField(max_length=50)
    # fast_heart_rate=models.CharField(max_length=50)
    # pain_behind_the_eyes=models.CharField(max_length=50)
    # sweating=models.CharField(max_length=50)
    # mucoid_sputum=models.CharField(max_length=50)
    # urination=models.CharField(max_length=50)
    # sunken_eyes=models.CharField(max_length=50)
    # spotting_urination=models.CharField(max_length=50)
    # nausea=models.CharField(max_length=50)
    # dischromic_patches=models.CharField(max_length=50)
    # dehydration=models.CharField(max_length=50)
    # loss_of_appetite=models.CharField(max_length=50)
    # abdominal_pain=models.CharField(max_length=50)
    # stomach_pain=models.CharField(max_length=50)
    # yellowish_skin=models.CharField(max_length=50)
    # altered_sensorium=models.CharField(max_length=50)
    # chest_pain=models.CharField(max_length=50)
    # muscle_wasting=models.CharField(max_length=50)
    # mild_fever=models.CharField(max_length=50)
    # vomiting=models.CharField(max_length=50)
    # high_fever=models.CharField(max_length=50)
    # red_spots_over_body=models.CharField(max_length=50)
    # dark_urine=models.CharField(max_length=50)
    # itching=models.CharField(max_length=50)
    # yellowing_of_eyes=models.CharField(max_length=50)
    # fatigue=models.CharField(max_length=50)
    # joint_pain=models.CharField(max_length=50)
    # muscle_pain=models.CharField(max_length=50)


    # def to_dict(self):
    #     return{
    #         'receiving_blood_transfusion':self.receiving_blood_transfusion,
    #         'family_history':self.family_history,
    #         'headache':self.headache,
    #         'receiving_unsterile_injections':self.receiving_unsterile_injections,
    #         'diarrhoea':self.diarrhoea,
    #         'weakness_of_one_body_side':self.weakness_of_one_body_side,
    #         'coma':self.coma,
    #         'stomach_bleeding':self.stomach_bleeding,
    #         'ulcers_on_tongue':self.ulcers_on_tongue,
    #         'lack_of_concentration':self.lack_of_concentration,
    #         'chills':self.chills,
    #         'loss_of_balance':self.loss_of_balance,
    #         'muscle_weakness':self.muscle_weakness,
    #         'unsteadiness':self.unsteadiness,
    #         'back_pain':self.back_pain,
    #         'dizziness':self.dizziness,
    #         'blackheads':self.blackheads,
    #         'shivering':self.shivering,
    #         'breathlessness':self.breathlessness,
    #         'continuous_sneezing':self.continuous_sneezing,
    #         'abnormal_menstruation':self.abnormal_menstruation,
    #         'red_sore_around_nose':self.red_sore_around_nose,
    #         'fast_heart_rate':self.fast_heart_rate,
    #         'pain_behind_the_eyes':self.pain_behind_the_eyes,
    #         'sweating':self.sweating,
    #         'mucoid_sputum':self.mucoid_sputum,
    #         'urination':self.urination,
    #         'sunken_eyes':self.sunken_eyes,
    #         'spotting_urination':self.spotting,
    #         'nausea':self.nausea,
    #         'dischromic_patches':self.dischromic_patches,
    #         'dehydration':self.dehydration,
    #         'loss_of_appetite':self.loss_of_appetite,
    #         'abdominal_pain':self.abdominal_pain,
    #         'stomach_pain':self.stomach_pain,
    #         'yellowish_skin':self.yellowish_skin,
    #         'altered_sensorium':self.altered_sensorium,
    #         'chest_pain':self.chest_pain,
    #         'muscle_wasting':self.muscle_wasting,
    #         'mild_fever':self.mild_fever,
    #         'vomiting':self.vomiting,
    #         'high_fever':self.high_fever,
    #         'red_spots_over_body':self.red_spots_over_body,
    #         'dark_urine':self.dark_urine,
    #         'itching':self.itching,
    #         'yellowing_of_eyes':self.yellowing_of_eyes,
    #         'fatigue':self.fatigue,
    #         'joint_pain':self.joint_pain,
    #         'muscle_pain':self.muscle_pain,
    #     }
