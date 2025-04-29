# Ways to remove keys from dictionary

# Printing Dictionary
a = {
    'name': 'pedd',
    'age': 25,
    'year':2025,
    'studied': 'btech agrochemicals',
    'combined': {
        'subjects' : {
            'subjects1': 'telugu',
            'subjects2': 'Hindi',
            'subjects3': 'English',
            'subjects4': 'Maths',
        },
        'marks': {
            'telugu' : 27,
            'hindi' : 45,
            'english': 75,
            'maths' : 98
        }


    }
    }
print(a)
print(a.keys())
print(a.values())
value2 = a['combined']['marks']
print(value2)

for k,v in a.items():
    print(k ,':', v)
    