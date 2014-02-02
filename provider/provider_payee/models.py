from django.db import models

class credmast(models.Model):
    ProviderId = models.AutoField(primary_key=True)
    SocSecNbr = models.CharField(max_length=9, null=True)
    LastName = models.CharField(max_length=20, null=True)
    FirstName = models.CharField(max_length=20, null=True)
    MiddleName = models.CharField(max_length=20, null=True)
    MaidenName = models.CharField(max_length=20, null=True)
    NickName = models.CharField(max_length=20, null=True)
    DOB = models.DateField(null=True)
    PlaceofBirth = models.CharField(max_length=50, null=True)
    Gender = models.CharField(max_length=9, null=True, choices=(('M', 'Male'),('F', 'Female')))
    Degree = models.CharField(max_length=20, null=True)
    Network = models.CharField(max_length=1, null=True, choices=(('Y', 'Yes'),('N', 'No')))
    CredIP = models.CharField(max_length=1, null=True, choices=(('Y', 'Yes'),('N', 'No')))
    ProviderType = models.CharField(max_length=1, null=True, choices=(('F', 'Facility'),('S', 'Single')))
    Emergency= models.CharField(max_length=1, null=True, choices=(('Y', 'Yes'),('N', 'No')))
    Child = models.CharField(max_length=1, null=True, choices=(('Y', 'Yes'),('N', 'No')))
    Teen = models.CharField(max_length=1, null=True, choices=(('Y', 'Yes'),('N', 'No')))
    Adult = models.CharField(max_length=1, null=True, choices=(('Y', 'Yes'),('N', 'No')))
    Geriatric = models.CharField(max_length=1, null=True, choices=(('Y', 'Yes'),('N', 'No')))
    Accredited = models.CharField(max_length=1, null=True, choices=(('Y', 'Yes'),('N', 'No')))
    CredentialDate = models.DateField(null=True)
    ReCredDate = models.DateField(null=True)
    AttestDate = models.DateField(null=True)
    TermDate = models.DateField(null=True)
    Status = models.CharField(max_length=1, null=True)
    StatusDate = models.DateField(null=True)
    UPIN = models.CharField(max_length=9, null=True)
    NPI = models.CharField(max_length=9, null=True)
    DegreeLevel = models.CharField(max_length=3, null=True, choices=(('CMD', 'Child MD'),('MD', 'MD'), ('PHD', 'PHD'), ('CLC', 'Clinician'), ('MAS', 'Masters'),('FAC', 'Facility')))
    DEA = models.CharField(max_length=9, null=True)
    BoardCert = models.CharField(max_length=1, null=True, choices=(('Y', 'Yes'),('N', 'No')))
    DateEntered = models.DateField(null=True)

    def __unicode__(self):
        return self.ProviderId

