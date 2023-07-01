from django import forms
from soldier.models import SoldierPersonalData

class SoldierPersonalDataForm(forms.ModelForm):
    class Meta:
        model = SoldierPersonalData
        fields = '__all__'
        labels = {
            'blood_gp': 'Blood Group',
            'i_card_no': 'I Card No',
            'indl_acct_no': 'Indl Acct No',
            'part_order': 'Part Order',
            'jt_acct_no': 'Jt Acct No',
            'aadhar_card': 'Aadhar Card',
            'pan_card': 'PAN Card',
            'email_id': 'Email Id',
            'mobile_no': 'Mobile No',
            'family_detail': 'Family Detail',
            'home_address': 'Home Address',
            'vill_house_no': 'Vill/House No',
            'post_office': 'Post office',
            'police_stn': 'Police Stn',
            'promotion_cadre': 'Promotion Cadre',
            'upgradation_cadre': 'Up-Gradation Cadre',
            'mil_edn': 'Mil Edn',
            'red_entry': 'RED Entry',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['upgradation_cadre'].label = 'Up-Gradation Cadre'  # Update the label
