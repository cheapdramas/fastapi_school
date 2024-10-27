from random import randint
from fastapi import HTTPException,status
import re
from datetime import date 
import datetime

def check_name(name:str):
        """Check if all characters in string is ukrainian and return first letter uppercase"""

        pattern_all_letters_is_ukrainian = r'^[А-ЩЬЮЯЄІЇҐа-щьюяєіїґ]+$'
        
        is_all_letters_ukrainian = bool(re.match(pattern=pattern_all_letters_is_ukrainian,string=name))

        if not is_all_letters_ukrainian:
            raise ValueError('All characters must be ukrainian')
        return f'{name[0].upper()}{name[1:]}'




class SchoolModelDependencies():
    global hints
    hints ={
        'first':'Заклад',
        'towns':
            [
                'М.Чернігів',
                'М.Гайсин',
                'М.Львів',
                'М.Вінниця',
                'М.Київ',
                'М.Ужгород'
            ],
        'type_school':
            [
                "загальної середньої освіти",
                'хуй пойми',
                'якась хуйня пока не придумав',
                'гітлер по моєму залупа',
                'пустун колупається в сраці'
            ]
        
    }
    
    @staticmethod
    def generate_random_fullname() -> str:
        """Generating random fullname for school"""
        random_type_school = hints['type_school'][randint(0,len(hints['type_school'])-1)]
        random_town = hints['towns'][randint(0,len(hints['towns'])-1)]

        fullname_hint = '{first} {type_school} {town}'.format(
            first=hints['first'],
            type_school=random_type_school,
            town=random_town
        )
        return fullname_hint
    

class ClassesModelDependencies:

    @staticmethod
    def checkName(name:str):
        """Check if value = 1-A, 2-A, 3-B ..."""
        pattern = r"^(1[0-1]|[1-9])-([А-ЩЬЮЯЄІЇҐа-щьюяєіїґ])$"
        assert re.match(pattern, name) != None
        return '-'.join([name.split('-')[0],name.split('-')[1].upper()])
            
            
    
            

class StudentsModelDependencies:

    @staticmethod
    def check_age(student_bdate:date):
        """Checking if student age > 5"""
        
        def get_age_diff_between_dates():
            server_date = datetime.datetime.now(datetime.timezone.utc).date()

            difference = server_date -student_bdate
            difference_in_years = difference.days // 365
            return difference_in_years
        
        difference_in_years = get_age_diff_between_dates()

        if difference_in_years < 6:
            raise ValueError('student must be older than 6')

        return student_bdate
    
    
    
    






        
