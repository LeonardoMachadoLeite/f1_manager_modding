class StaffContract(object):
    def __init__(self, StaffId, TeamId, PosInTeam, EndSeason, Salary, StartingBonus, RaceBonus, RaceBonusTargetPos):
        self.StaffId = StaffId
        self.TeamId = TeamId
        self.PosInTeam = PosInTeam
        self.EndSeason = EndSeason
        self.Salary = Salary
        self.StartingBonus = StartingBonus
        self.RaceBonus = RaceBonus
        self.RaceBonusTargetPos = RaceBonusTargetPos