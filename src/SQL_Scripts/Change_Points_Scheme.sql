select *
from Regulations_Enum_Changes
where ChangeID = 7;

update Regulations_Enum_Changes
set CurrentValue = 4, MaxValue = 4
where ChangeID = 7;

--delete from Regulations_NonTechnical_PointSchemes
--where PointScheme = 1;
insert into Regulations_NonTechnical_PointSchemes
values
    (4, 1, 25),
    (4, 2, 18),
    (4, 3, 15),
    (4, 4, 12),
    (4, 5, 10),
    (4, 6, 8),
    (4, 7, 7),
    (4, 8, 6),
    (4, 9, 5),
    (4, 10, 3),
    (4, 11, 2),
    (4, 12, 1);-- Maximum is 12th*/

select *
from Regulations_NonTechnical_PointSchemes
where PointScheme = 4;