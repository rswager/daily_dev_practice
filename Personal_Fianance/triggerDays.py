from copy import deepcopy
from datetime import date
from dateutil.relativedelta import relativedelta
from enumType import FrequencyType
from typing import List

class TriggerDays:
    def __init__(self, frequency_in: FrequencyType) -> None:
        self._trigger_days: List[date] = []
        self._frequency:FrequencyType = frequency_in

    @property
    def trigger_days(self) -> list:
        return deepcopy(self._trigger_days)

    def date_triggered(self, processed_day:date) -> bool:
        if processed_day in self._trigger_days:
            # We will remove the trigger day
            self._trigger_days.remove(processed_day)
            # now add the next date
            self._add_next_trigger_date(processed_day)
            return True
        return False

    def add_trigger_date(self, new_trigger_date:date) -> None:
        if new_trigger_date.day not in self._trigger_days:
            self._trigger_days.append(new_trigger_date)

    def _add_next_trigger_date(self, current_trigger_date:date) -> None:
        # We make a payment 1 time a month
        if self._frequency == FrequencyType.MONTHLY:
            current_trigger_date = current_trigger_date + relativedelta(months=1)
        # Bi weekly payment
        elif self._frequency == FrequencyType.BI_WEEKLY:
            current_trigger_date = current_trigger_date + relativedelta(weeks=2)
        # Weekly payments
        elif self._frequency == FrequencyType.WEEKLY:
            current_trigger_date = current_trigger_date + relativedelta(weeks=1)
        self.add_trigger_date(current_trigger_date)

if __name__ == '__main__':
    trigger_day = TriggerDays(FrequencyType.MONTHLY)
    trigger_day.add_trigger_date(date(2025,1,30))
    print(trigger_day.trigger_days)
    trigger_day.date_triggered(date(2025,1,30))
    print(trigger_day.trigger_days)
