from django.db import models

class SoldierPersonalData(models.Model):
    name = models.CharField(max_length=255, null=True)
    dob = models.CharField(max_length=10, null=True)
    doe = models.CharField(max_length=10, null=True)
    civ_edn = models.CharField(max_length=255, null=True)
    blood_gp = models.CharField(max_length=10, null=True)
    i_card_no = models.CharField(max_length=255, null=True)
    indl_acct_no = models.CharField(max_length=255, null=True)
    part_order = models.CharField(max_length=255, null=True)
    jt_acct_no = models.CharField(max_length=255, null=True)
    aadhar_card = models.CharField(max_length=255, null=True)
    pan_card = models.CharField(max_length=255, null=True)
    email_id = models.CharField(max_length=255, null=True)
    mobile_no = models.CharField(max_length=20, null=True)
    father = models.CharField(max_length=255, null=True)
    mother = models.CharField(max_length=255, null=True)
    son = models.CharField(max_length=255, null=True)
    daughter = models.CharField(max_length=255, null=True)
    home_address = models.CharField(max_length=255, null=True)
    vill_house_no = models.CharField(max_length=255, null=True)
    post_office = models.CharField(max_length=255, null=True)
    teh = models.CharField(max_length=255, null=True)
    police_stn = models.CharField(max_length=255, null=True)
    dist = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=255, null=True)
    pin_code = models.CharField(max_length=10, null=True)
    promotion_cadre = models.CharField(max_length=255, null=True)
    upgradation_cadre = models.CharField(max_length=255, null=True)
    mil_edn = models.CharField(max_length=255, null=True)
    course = models.CharField(max_length=255, null=True)
    sports = models.CharField(max_length=255, null=True)
    ere = models.CharField(max_length=255, null=True)
    award = models.CharField(max_length=255, null=True)
    med = models.CharField(max_length=255, null=True)
    red_entry = models.CharField(max_length=255, null=True)
    misc = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'soldier_soldierpersonaldata'

    def __str__(self):
        return self.name
