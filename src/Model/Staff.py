class StaffContract(object):
    def __init__(self, StaffId, StaffType, FirstName, LastName, Nationality, DOB_ISO, UnspentXP, Morale, RetirementAge, Retired):
        self.StaffId = StaffId
        self.StaffType = StaffType
        self.FirstName = FirstName
        self.LastName = LastName
        self.Nationality = Nationality
        self.DOB_ISO = DOB_ISO
        self.UnspentXP = UnspentXP
        self.Morale = Morale
        self.RetirementAge = RetirementAge
        self.Retired = Retired