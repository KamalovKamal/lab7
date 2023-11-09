import re
f = open("raw.txt", "r")
file = f.read()

# task 1
pattern = r'ab*'
match = re.search(pattern, file)
match = re.findall(pattern, file)
print(match)

# task 2
pattern = r'ab{2,3}|abc{1,2}'
matches = re.findall(pattern, file)
print(matches)

# task 3 
pattern = r'[a-z]+_[a-z]+'
matches = re.findall(pattern, file)
print(matches)

# task 4
pattern = r'a.*b$'
matches = re.findall(pattern, file, re.DOTALL)
print(matches)

# task 5
pattern = r'[A-Z][a-z]+'
matches = re.findall(pattern, file)
print(matches)

# task 6
new_file = re.sub(r' ', ';', file)
print(new_file)  

# task 7
pattern = r'_(\w)'
uppered = re.sub(pattern, lambda x: x.group(0).upper(), file)
res = re.sub(r'_','',uppered)
print(res)

# task 8
split_data = re.split(r'[A-Z]', file)
print(split_data) 

# task 9
new_text = re.sub(r'([a-z])([A-Z])',r'\1 \2', file)
print(new_text) 

# task 10
def camel_snake(file):
    words = re.findall(r'[A-Z][a-z]*', file)
    return '_'.join(word.lower() for word in words)
result = camel_snake(file)
print(result) 

