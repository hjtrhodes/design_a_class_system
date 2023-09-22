from lib.diary_todo_parent_class import *
from lib.phone_number_finder import *

def test_add_todo_list_return_incomplete():  
    todo1 = Todo("cooking")
    todo2 = Todo("cleaning")
    todo3 = Todo("walk dog")  
    todo_list = DiaryTodoParent()  
    todo_list.add_todo(todo1)
    todo_list.add_todo(todo2)
    todo_list.add_todo(todo3)
    assert todo_list.print_incomplete_to_dos() == ["cooking", "cleaning", "walk dog"]


def test_add_todo_list_return_incomplete_when_complete_present():
    todo1 = Todo("cooking")
    todo2 = Todo("cleaning")
    todo3 = Todo("walk dog")  
    todo_list = DiaryTodoParent()  
    todo_list.add_todo(todo1)
    todo_list.add_todo(todo2)
    todo_list.add_todo(todo3)
    todo1.mark_complete()
    assert todo_list.print_incomplete_to_dos() == ["cleaning", "walk dog"]


def test_add_todo_list_return_complete_when_complete_present():
    todo1 = Todo("cooking")
    todo2 = Todo("cleaning")
    todo3 = Todo("walk dog")  
    todo_list = DiaryTodoParent() 
    todo_list.add_todo(todo1)
    todo_list.add_todo(todo2)
    todo_list.add_todo(todo3)
    todo1.mark_complete()
    assert todo_list.print_complete_todos() == ["cooking"]


def test_give_up_return_all_as_complete():
    todo1 = Todo("cooking")
    todo2 = Todo("cleaning")
    todo3 = Todo("walk dog")  
    todo_list = DiaryTodoParent()
    todo_list.add_todo(todo1)
    todo_list.add_todo(todo2)
    todo_list.add_todo(todo3)
    todo_list.give_up_all_todos()
    assert todo_list.print_complete_todos() == ["cooking", "cleaning", "walk dog"]


def test_add_and_return_diary_entries():
    test_diary_entry = DiaryEntry("Monday13th","today was a sad day, i was paired with harry, he was too smart for me")
    test_diary_entry_01 = DiaryEntry("tuesday","stuff happened today")
    test_diary_entry_02 = DiaryEntry("friday","more stuff that happened today")
    parent_class = DiaryTodoParent()
    parent_class.add_diary_entry(test_diary_entry)
    parent_class.add_diary_entry(test_diary_entry_01)
    parent_class.add_diary_entry(test_diary_entry_02)
    result = parent_class.retrieve_all_diary_entries()
    assert result == ["today was a sad day, i was paired with harry, he was too smart for me", "stuff happened today", "more stuff that happened today"]

def test_return_best_diary_entry_for_reading_time():
    test_diary_entry = DiaryEntry("Monday13th","today was a sad day, i was paired with harry, he was too smart for me")
    test_diary_entry_01 = DiaryEntry("tuesday","stuff happened today stuff happened today stuff happened today stuff happened today stuff happened today stuff happened today stuff happened")
    test_diary_entry_02 = DiaryEntry("friday","more stuff that happened")
    test_diary_entry.reading_time(4)
    test_diary_entry_01.reading_time(4)
    test_diary_entry_02.reading_time(4)
    parent_class = DiaryTodoParent()
    parent_class.add_diary_entry(test_diary_entry)
    parent_class.add_diary_entry(test_diary_entry_01)
    parent_class.add_diary_entry(test_diary_entry_02)
    result = parent_class.find_best_diary_entry_for_reading_time(1)
    assert result == "more stuff that happened"
    
def test_search_diary_content_for_phone_numbers_and_store():
    test_diary_entry = DiaryEntry("Monday13th", 'Hey how is it going? my phone number is: 07895363837')
    test_diary_entry_01 = DiaryEntry("tuesday","stuff happened today stuff happened today 07797746177 stuff happened today stuff happened today stuff happened today stuff happened today stuff happened")
    phone_number = PhoneNumberFinder()
    phone_number = PhoneNumberFinder()
    phone_number.store_phone_number(test_diary_entry)
    phone_number.store_phone_number(test_diary_entry_01)
    result = phone_number.return_phone_numbers()
    assert result == [["07895363837"], ["07797746177"]]



def test_no_duplicate_phone_numbers():
    test_diary_entry = DiaryEntry("Monday13th", 'Hey how is it going? my phone number is: 07895363837')
    test_diary_entry_01 = DiaryEntry("tuesday","stuff happened today stuff happened today 07895363837 stuff happened today stuff happened today stuff happened today stuff happened today stuff happened")
    phone_number = PhoneNumberFinder()
    phone_number.store_phone_number(test_diary_entry)
    phone_number.store_phone_number(test_diary_entry_01)
    result = phone_number.return_phone_numbers()
    assert result == [["07895363837"]]


