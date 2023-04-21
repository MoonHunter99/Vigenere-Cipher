#Kunin yung input ni User AKA yung Message na gustong encrypt ni User
user_input_message = str(input("What is your message that you want to encrypt?: "))
#kunin yung Input ni user na keyword na gusto niyang gamitin
user_input_keyword = str(input("What is the Keyword that you would like to use?: "))
#lalgyan mo nung cyhered text
chpr_txt = ""
#Turn the characters of the User input to the respective number values ranging from 0-25
number_value_msg = [ord(w)-65 for w in user_input_message]
number_value_key = [ord(w)-65 for w in user_input_keyword]
#for loop para sa encryption
for i in range(len(user_input_message)):
    number_value = (number_value_msg[i] + number_value_key[i % len(user_input_keyword)]) % 26
    chpr_txt += chr(number_value + 65)
#print mo na output mo
print(chpr_txt)