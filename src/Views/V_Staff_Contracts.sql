CREATE VIEW IF NOT EXISTS V_Staff_Contracts
AS 
select t.TeamName,
		sest.Name,
		substr(scd.FirstName, 26, length(scd.FirstName) - 26) as FirstName,
		CASE substr(scd.LastName, -2, 1)
		WHEN '1' THEN substr(scd.LastName, 20, length(scd.LastName) - 21) 
		ELSE substr(scd.LastName, 20, length(scd.LastName) - 20)
		END as LastName,
		sc.PosInTeam,
		sc.Salary,
		scd.StaffType,
		sc.StaffID,
		t.TeamID
from Staff_CommonData scd left join Staff_Contracts sc on (scd.StaffID = sc.StaffID)
	 join Staff_Enum_StaffType sest on (sest.StaffType = scd.StaffType)
	 left join Teams t on (sc.TeamID = t.TeamID);