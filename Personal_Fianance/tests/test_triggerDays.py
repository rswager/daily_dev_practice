import pytest
from datetime import date
from dateutil.relativedelta import relativedelta
from triggerDays import TriggerDays
from enumType import FrequencyType


# --- Fixtures ---

@pytest.fixture
def monthly_trigger():
    return TriggerDays(FrequencyType.MONTHLY)

@pytest.fixture
def biweekly_trigger():
    return TriggerDays(FrequencyType.BI_WEEKLY)

@pytest.fixture
def weekly_trigger():
    return TriggerDays(FrequencyType.WEEKLY)


# --- Tests ---

def test_trigger_days_returns_copy(monthly_trigger):
    """Ensure trigger_days returns a copy, not a reference."""
    monthly_trigger.add_trigger_date(date(2025, 1, 15))
    copy_ref = monthly_trigger.trigger_days
    copy_ref.append(date(2025, 1, 16))
    # The original internal list should remain unchanged
    assert len(monthly_trigger.trigger_days) == 1


def test_add_trigger_date_caps_day_to_28(monthly_trigger):
    """Ensure that days greater than 28 are capped to 28."""
    d = date(2025, 1, 31)
    monthly_trigger.add_trigger_date(d)
    assert monthly_trigger.trigger_days[0].day == 28


def test_add_trigger_date_valid_day(monthly_trigger):
    """Dates <= 28 should be added as-is."""
    d = date(2025, 1, 20)
    monthly_trigger.add_trigger_date(d)
    assert monthly_trigger.trigger_days[0] == d


def test_date_triggered_removes_and_adds_next_monthly(monthly_trigger):
    """When triggered, the current date is removed and next month added."""
    d = date(2025, 1, 15)
    monthly_trigger.add_trigger_date(d)

    # Trigger that date
    result = monthly_trigger.date_triggered(d)
    assert result is True

    # The original date should be removed
    assert d not in monthly_trigger.trigger_days

    # The new date should be one month later, capped to 28
    expected = d + relativedelta(months=1)
    assert monthly_trigger.trigger_days[0].month == expected.month
    assert monthly_trigger.trigger_days[0].day == min(expected.day, 28)


def test_date_triggered_removes_and_adds_next_biweekly(biweekly_trigger):
    """When triggered, it should remove and add +14 days."""
    d = date(2025, 1, 1)
    biweekly_trigger.add_trigger_date(d)

    # Trigger that date
    result = biweekly_trigger.date_triggered(d)
    assert result is True

    # The old date should be removed
    assert d not in biweekly_trigger.trigger_days

    # The new date should be +14 days later
    expected = d + relativedelta(days=14)
    assert biweekly_trigger.trigger_days[0] == expected


def test_date_triggered_removes_and_adds_next_weekly(weekly_trigger):
    """When triggered, it should remove and add +7 days."""
    d = date(2025, 1, 8)
    weekly_trigger.add_trigger_date(d)

    # Trigger that date
    result = weekly_trigger.date_triggered(d)
    assert result is True

    # The old date should be removed
    assert d not in weekly_trigger.trigger_days

    # The new date should be +7 days later
    expected = d + relativedelta(days=7)
    assert weekly_trigger.trigger_days[0] == expected


def test_date_triggered_returns_false_when_not_found(weekly_trigger):
    """Should return False if date not in trigger_days."""
    d = date(2025, 3, 1)
    assert weekly_trigger.date_triggered(d) is False
    # Nothing new should be added
    assert weekly_trigger.trigger_days == []


if __name__ == '__main__':
    pytest.main([__file__])