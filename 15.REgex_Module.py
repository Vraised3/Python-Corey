import re

text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''
Sentence = 'Start a sentence and then bring it to an end'


def MA(matches):
    val = []
    for match in matches:
        val.append(match[0][:-1])
    return val


with open('REgex_Sample.txt', 'r') as REg_Sample:
    Sample = REg_Sample.read()
Nam = re.compile(r'[A-Z][A-Za-z-]+\s[A-Z][A-Za-z-]+\n')
Num = re.compile(r'\d{3}.\d{3}.\d{4}')
Add = re.compile(r'\d{3}.+\d{5}')
Em = re.compile(r'\w*@\w*\.com')

# Name = MA(Nam.finditer(Sample))  # Works count = 100
# Number = MA(Num.finditer(Sample))  # Works count = 100
# Address = MA(Add.finditer(Sample))  # Works count = 100
# Email = MA(Em.finditer(Sample))  # Works count = 100

Name = Nam.findall(Sample)  # Works count = 100
Number = Num.findall(Sample)  # Works count = 100
Address = Add.findall(Sample)  # Works count = 100
Email = Em.findall(Sample)  # Works count = 100


# Dat_list = []
Dat_Dict = {}
for i in range(100):
    # Dat_list.append([Name[i], Number[i], Address[i], Email[i]])
    Dat_Dict[Name[i][:-1]] = [Number[i], Address[i], Email[i]]

print(Dat_Dict)
print(text_to_search[1:4])

sent = re.compile(r'start', re.IGNORECASE)  # Ignores case
sent = sent.search(Sentence)
