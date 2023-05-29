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
and TrackID not in (1, 2, 9, 10, 11, 13, 14, 19, 20, 22);
--*/
