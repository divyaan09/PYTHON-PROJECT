# <<<-----------------  LOVE CALCULATOR  ------------------->>


name1=input("Whats his Name? ")
name2=input("Whats is her Name? ")
print(" 'aries' , 'taurus' , 'gemini' , 'cancer'")
print(" 'leo' , 'virgo' , 'libra' , 'scorpio' ") 
print(" 'sagittarius' , 'capricorn' , 'aquarius' , 'pisces' ")
zodiac1 = input("What's his Zodiac Sign? ")
zodiac2 = input("What's her Zodiac Sign? ")

combine_string=name1+name2
lower_case_string=combine_string.lower()

t=lower_case_string.count('t')
r=lower_case_string.count('r')
u=lower_case_string.count('u')
e=lower_case_string.count('e')
true=t+r+u+e

l=lower_case_string.count('l')
o=lower_case_string.count('o')
v=lower_case_string.count('v')
e=lower_case_string.count('e')
love=l+o+v+e

love_score=str(true)+str(love)

compatible_zodiacs = {
    'aries': ['leo', 'sagittarius'],
    'taurus': ['virgo', 'capricorn'],
    'gemini': ['libra', 'aquarius'],
    'cancer': ['scorpio', 'pisces'],
    'leo': ['aries', 'sagittarius'],
    'virgo': ['taurus', 'capricorn'],
    'libra': ['gemini', 'aquarius'],
    'scorpio': ['cancer', 'pisces'],
    'sagittarius': ['aries', 'leo'],
    'capricorn': ['taurus', 'virgo'],
    'aquarius': ['gemini', 'libra'],
    'pisces': ['cancer', 'scorpio']
}

zod1 = zodiac1.lower()
zod2 = zodiac2.lower()

compatible_signs = compatible_zodiacs.get(zod2, [])

if zod1 in compatible_signs:
    print("\nYour Zodiac signs are compatible!")
else:
    print("\nYour Zodiac signs are not compatible.")


print("\nyour love score is: "+str(love_score)+" percent")

print("\nTHERE ARE 7 STAGES OF LOVE ")

if int(love_score)<=20:
    print("You are on the 1st stage: 'Attraction' (Dilkashi | لذیذ)\n")
elif int(love_score)>20 and int(love_score)<=40:
    print("You are on the 2nd stage: 'Attachment' (Oons | اونس)\n")
elif int(love_score)>40 and int(love_score)<=60:
    print("You are on the 3rd stage: 'Love' (Mohabbat | محبت)\n")
elif int(love_score)>60 and int(love_score)<=75:
    print("You are on the 4th stage: 'Trust' (Akidat | عقیدت)\n")
elif int(love_score)>75 and int(love_score)<=85:
    print("You are on the 5th stage: 'Worship' (Ibadat | عبادت)\n")
elif int(love_score)>85 and int(love_score)<=95:
    print("You are on the 6th stage: 'Obsession' (Junoon | جنون)\n")
else:
    print("Now, You are on the LAST stage: 'Death' (Maut | موت)\n")

