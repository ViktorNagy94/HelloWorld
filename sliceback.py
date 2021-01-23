letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25:0:-1]
# backwards = letters[::-1] #ezzel a sorral tudjuk elérni azt,
# hogy az a betűt, vagyis az első karaktert is kiírja!
# Ez egy közkedvelt és ismert "idiom" "::-1"

print(backwards)

# Challenge: qpo, ecdba, utolsó 8 karakter

qpoIsWrittenOut = letters[16:13:-1]
print(qpoIsWrittenOut)

edcbaIsWrittenOut = letters[4::-1]
print(edcbaIsWrittenOut)

last8CharIsWrittenOut = letters[:-9:-1] #vagy [15:17:-1]
print(last8CharIsWrittenOut)


#more idioms
#utolsó 4 elem
print(letters[-4:])

#utolsó elem
print(letters[-1:])

#első elem #üres str esetén nem crashel a programunk!!
print(letters[:1])
#vagy
print(letters[0])