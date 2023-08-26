select * from Parts_Enum_Type;

-- Powertrain Parts
update Parts_Enum_Type
set BaseManufactureCost = 2000000
where Name = 'Engine';

update Parts_Enum_Type
set BaseManufactureCost = 1500000
where Name = 'ERS';

update Parts_Enum_Type
set BaseManufactureCost = 1000000
where Name = 'Gearbox';

-- Aerodynamic Parts
update Parts_Enum_Type
set BaseManufactureCost = 450000,
    BaseDesignCost = 700000,
    BaseManufactureWork = 2000
where Name = 'Body';

update Parts_Enum_Type
set BaseManufactureCost = 225000,
    BaseDesignCost = 1300000,
    BaseManufactureWork = 500
where Name = 'FrontWing';

update Parts_Enum_Type
set BaseManufactureCost = 275000,
    BaseDesignCost = 1150000,
    BaseManufactureWork = 500
where Name = 'RearWing';

update Parts_Enum_Type
set BaseManufactureCost = 300000,
    BaseDesignCost = 700000,
    BaseManufactureWork = 1000
where Name = 'SidePods';

update Parts_Enum_Type
set BaseManufactureCost = 400000,
    BaseDesignCost = 1200000,
    BaseManufactureWork = 1500
where Name = 'Floor';

update Parts_Enum_Type
set BaseManufactureCost = 250000,
    BaseDesignCost = 1000000,
    BaseManufactureWork = 1000
where Name = 'Suspension';