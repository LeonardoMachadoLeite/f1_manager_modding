select * from Races_Tracks;
update Races_Tracks
set Laps = round(Laps/2);

--
select * from Tyres;
update Tyres
set Durability = 1.225
where Name = 'C1';
update Tyres
set Durability = 1.05
where Name = 'C2';
update Tyres
set Durability = 0.7623
where Name = 'C3';
update Tyres
set Durability = 0.5131
where Name = 'C4';
update Tyres
set Durability = 0.4046
where Name = 'C5';
update Tyres
set Durability = 0.875
where Name = 'Intermediate';
update Tyres
set Durability = 1.575
where Name = 'Wet';
/**/

select * from V_Staff_Contracts;

/**/
select r.RaceID, r.SeasonID, r.Day, t.TrackID, t.Name, t.Country, t.Laps
from Races r inner join Races_Tracks t on (r.TrackID = t.TrackID)
where r.SeasonID = 2022
order by r.RaceID;

select r.RaceID, r.SeasonID, r.Day, t.TrackID, t.Name, t.Country, t.Laps
from Races r inner join Races_Tracks t on (r.TrackID = t.TrackID)
where r.SeasonID = 2022
and t.TrackID in (1, 2, 9, 10, 11, 13, 14, 19, 20, 22)
/*
and t.Name in ('Bahrain', 'AlbertPark', 'CircuitOfTheAmericas', 'Miami', 'Monza',
               'Silverstone', 'Jeddah', 'RedBullRing', 'SpaFrancorchamps', 'Interlagos')--*/
order by r.RaceID;

/*
delete from Races
where SeasonID = 2022
and TrackID in (7);
--*/