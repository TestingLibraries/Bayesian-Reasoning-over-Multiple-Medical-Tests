## When we order tests for a patient, sensitivity and specificity only tells us the TPR and TNR specifically.
## However, we do not get the P(Has disease|tested positive) or P(Does not have disease|Tested negative)
## These 2 values are known as the PPV (Positive Predictive value) and the NPV(Negative predictive value) respectively.
## This project serves to allow you to get the PPV and NPV for your patient, not just over one test,
## But over multiple tests of varying specificities and sensitivities.

## This function calculates the PPV for your patient
def PPV_Finder(sensitivity,specificity,prevalence) :

    PPV = (prevalence*sensitivity)/((prevalence)*(sensitivity)+(1-prevalence)*(1-specificity))
    PPV = PPV*100
    return(PPV)

## This function calculates the NPV for your patient
def NPV_Finder(sensitivity,specificity,prevalence) :
    NPV = (1-prevalence)*(specificity)/((1-prevalence)*(specificity)+(prevalence)*(1-sensitivity))
    NPV = NPV*100
    return(NPV)

## This function checks and cleans the numerical userinput
def Check_CleanUser_input(input) :  
    try :
        input = float(input)
    except :
        print("Please enter a number from 0-100")
        print("The program will now shut down...")
        quit()
    if input < 0 or input >100 :
        print("Please enter a number between 0-100")
        print("The program will now shut down...")
        quit()
    return(input)

## This function checks if the user properly typed p or n.
def Check_Positive_or_Negative(input) :
    if input not in ("p", "n") :
        print("Please enter p or n to indicate whether your input is positive or negative!")
        print("program is shutting down...")
        quit()  
    return(input)

## This function converts the userinput from a whole number between 0-100
## to a fraction between 0-1.0. This is important for the proper computation of the PPV and NPV values.
def ConvertToFraction(input) :
    input = input/100
    return(input)

## This function checks if the user properly typed y or n.
def Check_yes_or_no(input) :
    if input not in ("y", "n") :
        print("Please enter y or n to indicate yes or no!")
        print("program is shutting down...")
        quit()  
    return(input)

## The code proper begins here -------------------------------------------------------------------------

sensitivity = input("Welcome!, please enter the sensitivity of your test, a number from 0-100 ")
specificity = input("please enter the specificity of your test, in the same format ")
prevalence = input("please enter the prevalence of your disease, in the same format ")
PositiveOrNegative = input("Was your test positive or negative? (p/n) ")

## lets proceed to clean and check our user's input

sensitivity = Check_CleanUser_input(sensitivity)
specificity = Check_CleanUser_input(specificity)
prevalence = Check_CleanUser_input(prevalence)
PositiveOrNegative = Check_Positive_or_Negative(PositiveOrNegative)

## now lets proceed to convert it to fractions so that we can accurately run our tests.

sensitivity = ConvertToFraction(sensitivity)
specificity = ConvertToFraction(specificity)
prevalence = ConvertToFraction(prevalence)

## now lets proceed to run our tests, and present our PPV and NPV values to the user

if PositiveOrNegative == "p" :
    PPV = PPV_Finder(sensitivity,specificity,prevalence)
    print(f"your PPV is {PPV}%")
else :
    NPV = NPV_Finder(sensitivity,specificity,prevalence)
    print(f"your NPV is {NPV}%")

## Now, lets ask the user, if he would like to continue testing, because, from now onwards, the code is a loop of continous bayesian testing
## Looping section ------------------------------------------------------------------------------------------------------------------

## i will set the "want to continue" flag to y (yes) first.
## This way, we can initiate the loop without errors or code verbosity.
Want_to_continue = "y"

while Want_to_continue == "y" :
    Want_to_continue = input("do you have more tests you would like to conduct? (y/n)? ")
    Check_yes_or_no(Want_to_continue)
    if Want_to_continue == "n" :
        print("Alright then, shutting down...")
        quit()
    
    # Lets get in our sensitivity, specificity and prior belief (that the patient has the disease) again
    sensitivity = input("please enter the sensitivity of your new test, a number from 0-100 ")
    specificity = input("please enter the specificity of your new test, in the same format ")  
    ## lets rename our PPV and 1-NPV to Prior_Belief 
    ## This is because we are no longer using prevalence as we are using our prior belief (that the patient has the disease).
    ## our prior belief is now simply how much we believe the patient has the disease.
    if PositiveOrNegative == "p" :
        Prior_Belief = PPV
    else :
        Prior_Belief = 100-NPV
    PositiveOrNegative = input("Was your test positive or negative? (p/n) ")

    ## Lets proceed to clean and check our user inputs
    sensitivity = Check_CleanUser_input(sensitivity)
    specificity = Check_CleanUser_input(specificity)
    PositiveOrNegative = Check_Positive_or_Negative(PositiveOrNegative)

    ## Lets proceed to convert it into fractions so that we can properly run our tests.
    sensitivity = ConvertToFraction(sensitivity)
    specificity = ConvertToFraction(specificity)
    Prior_Belief = ConvertToFraction(Prior_Belief)

    ## lets run our tests, and proceed to present it to our user.
    if PositiveOrNegative == "p" :
        PPV = PPV_Finder(sensitivity,specificity,Prior_Belief)
        print(f"your updated probability that the patient has the disease is {PPV}%")
    else :
        NPV = NPV_Finder(sensitivity,specificity,Prior_Belief)
        print(f"your updated probability that the patient has the disease, after a negative test, is {100-NPV}%")
quit()   

