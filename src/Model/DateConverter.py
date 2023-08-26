import datetime as dt

START_DATE = dt.datetime.strptime('30/12/1899', '%d/%m/%Y').date()

class DateConverter(object):

    def __init__(self, date):
        if type(date) == int:
            self.date_raw = date
        if type(date) == dt.date:
            self.date_raw = (date - START_DATE).days
    
    def get_date(self):
        return START_DATE + dt.timedelta(days=self.date_raw)
    
    def get_date_raw(self):
        return self.date_raw
    
    def get_reference_date():
        return START_DATE
    
    def __str__(self):
        return self.get_date().strftime('%d/%m/%Y')
    
    def __repr__(self):
        return self.get_date().strftime('%d/%m/%Y')
    
    def desc_as_row(self):
        return f'{self.__str__()}\t{self.date_raw}'
    
    def get_all_weekdays_in_year(year, target_day):
        start_date = dt.date(year, 1, 1) 
        end_date = dt.date(year, 12, 31)

        delta = end_date - start_date
        ans = []

        for i in range(delta.days + 1):
            day = start_date + dt.timedelta(days=i)
            if day.isoweekday() == target_day:
                ans.append(DateConverter(day))
        
        return ans
