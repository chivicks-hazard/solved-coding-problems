my_array = ['Pete', 'Jones', 'Lisa', 'Bob', 'Siri']
my_hash_set = [
    [None],
    ['Jones'],
    [None],
    ['Lisa'],
    [None],
    ['Bob'],
    [None],
    ['Siri'],
    ['Pete'],
    [None]
]

def hash_function(value):
    return sum(ord(char) for char in value) % 10
    
def add(value):
    index = hash_function(value)
    bucket = my_hash_set[index]
    if value not in bucket:
        bucket.append(value)
    
def contains(value):
    index = hash_function(value)
    bucket = my_hash_set[index]
    return value in bucket
    
# print("'Bob' has hash code: ", hash_function("Bob"))
# print("'Pete' is in the Hash Set: ", contains("Pete"))

add('Stuart')
print(my_hash_set)
print("Contains Stuart: ", contains('Stuart'))