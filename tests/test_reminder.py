import pytest
from lib.reminder import Reminder






def test_reminder_to_do_task():
    reminder = Reminder('Khalifa')
    reminder.remind_me_to("do the laundry")
    result = reminder.remind()
    assert result == "do the laundry, Khalifa!"

def test_reminder_check_task_is_none():
    reminder = Reminder('Khalifa')
    with pytest.raises(Exception) as err:
        reminder.remind()
    erro_message = str(err.value)
    assert erro_message== "no reminder set!"