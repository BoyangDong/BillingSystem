from app.main.models import MONTHS

class YearMonth(object):

    def __eq__(self, other):
        if self.Year == other.Year and self.Month == other.Month:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.Year < other.Year:
            return True
        if self.Year > other.Year:
            return False

        if MONTHS.index(self.Month) < MONTHS.index(other.Month):
            return True
        else:
            return False
    def __gt__(self, other):
        if self.Year < other.Year:
            return False
        if self.Year > other.Year:
            return True

        if MONTHS.index(self.Month) > MONTHS.index(other.Month):
            return True
        else:
            return False
            
    def __le__(self, other):
        if not self.__gt__(other):
            return True
        else:
            return False
    def __ge__(self, other):
        if not self.__lt__(other):
            return True
        else:
            return False
