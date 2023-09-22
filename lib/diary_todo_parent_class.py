from lib.diary_entry import *
from lib.todo import *

class DiaryTodoParent():
    
    def __init__(self):
        self.diaryentries = []
        self.todo_listings = []
        pass
        
    def add_diary_entry(self, diary_entry):
        self.diaryentries.append(diary_entry)
    
    def retrieve_all_diary_entries(self):
        return [object.contents for object in self.diaryentries]

    def find_best_diary_entry_for_reading_time(self, minutes):
        smallest_difference = 100
        current_best_content_for_read_time = None
        for object in self.diaryentries:
            if  object.read_time - minutes < smallest_difference:
                smallest_difference = object.read_time - minutes
                current_best_content_for_read_time = object
        return current_best_content_for_read_time.contents 

    def add_todo(self, todo):
        self.todo_listings.append(todo)

    def print_incomplete_to_dos(self):
        incompleted_list = []
        for object in self.todo_listings:
            if object.complete == False:
                incompleted_list.append(object.task)
        return incompleted_list

    def print_complete_todos(self):
        completed_list = []
        for object in self.todo_listings:
            if object.complete == True:
                completed_list.append(object.task)
        return completed_list

    def give_up_all_todos(self):
        for object in self.todo_listings:
            if object.complete == False:
                object.complete = True