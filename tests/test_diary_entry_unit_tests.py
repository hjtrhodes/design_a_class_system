from lib.diary_entry import *

def test_word_count_returns():
    test_diary_entry = DiaryEntry("Monday13th","today was a sad day, i was paired with harry, he was too smart for me")
    assert test_diary_entry.word_count == 16

def test_return_a_reading_time():
    test_diary_entry = DiaryEntry("Monday13th","today was a sad day, i was paired with harry, he was too smart for me")
    result = test_diary_entry.reading_time(3)
    assert result == 5