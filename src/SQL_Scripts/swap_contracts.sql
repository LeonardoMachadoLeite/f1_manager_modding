select *
from V_Staff_Contracts
where StaffTypeName = 'Driver'
and TeamID in (3, 8);
-- 3 = Red Bull
-- 8 =  Alphatauri


select * from Staff_Contracts
where StaffID in (10, 17, 15, 81);

update Staff_Contracts
set TeamID = 8
where StaffID in (10, 17);

update Staff_Contracts
set TeamID = 3
where StaffID in (15, 81);