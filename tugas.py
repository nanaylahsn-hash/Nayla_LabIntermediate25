# 1. minta buat kata secret_word
# 2. user memasukan 1 karakter
# 3. pastikan user hanya menginput huruf 
# 4. memastikan karakter tersebut ada di secret_word regardless capitalization

# a - z dan A - Z


secret_word = "mangga"
# step 1
input_user = input("Please input the letter : ")

length_input = len(input_user)
# step 2
if length_input == 1:
    # step 3
    # input pasti satu karakter
    is_alphabet_lower = input_user >= "a" and input_user <= "z"
    is_alphabet_upper = input_user >= "A" and input_user <= "Z"
    is_alphabet = is_alphabet_lower or is_alphabet_upper
    if is_alphabet == True:
        # step 4 , ignore capitalizaiton, force to lower case
        secret_word = secret_word.lower()
        input_user = input_user.lower()
        # step 5, check if the letter is in secret_word
        if input_user in secret_word:
            print(" -> Your answer is correct! . . .")
        else : 
            print(" -> Unfortunately your answer is wrong!")
    else :
        print(" -> Input is not a valid alphabet!")
else :
    print(" -> Please input only one letter!")

