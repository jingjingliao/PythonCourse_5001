# The main function is to test that whether you have pneumonia or
# infection of airways or viral infection


def main():
    symptoms_question1 = input("Are you coughing? ")
    if symptoms_question1.lower() == "yes":
        symptoms_question2 = input("""Are you short of breath or wheezing
or coughing up phlegm? """)
        if symptoms_question2.lower() == "yes":
            print("Possibilities include pneumonia or infection of airways")
        else:
            symptoms_question3 = input("Do you have a headache? ")
            if symptoms_question3.lower() == "yes":
                print("Possibilities include viral infection")
            else:
                aching()
    else:
        headache()


# The headache function is to test that whether you have menigitis


def headache():
    symptoms_question4 = input("Do you have a headache? ")
    if symptoms_question4.lower() == "yes":
        symptoms_question5 = input("""Are you expreiencing any of the following:
pain when bending your head forward, nausea or vomiting,
bright light burting your eyes, drosiness or confustion?""")
        if symptoms_question5.lower() == "yes":
            print("Possibilities include menigitis.")
        else:
            vomit_or_diarrhea()
    else:
        aching()


# The aching function is to test that whether you have viral infection
# or whether your provided information is insufficient


def aching():
    symptoms_question6 = input("Do you have aching bones or aching joints? ")
    if symptoms_question6.lower() == "yes":
        print("Possibilities include viral infection")
    else:
        symptoms_question7 = input("Do you have a rash? ")
        if symptoms_question7.lower() == "yes":
            print("Insufficient information to list possibilities")
        else:
            sore_throat()


# The vomit_or_diarrhea function is to test that whether
# you have digestive tract infection


def vomit_or_diarrhea():
    symptoms_question8 = input("Are you vomiting or had diarrhea? ")
    if symptoms_question8.lower() == "yes":
        print("Possibilities include digestive tract infection")
    else:
        aching()


# The sore_throat function is to test that whether
# you have a throat infection or kidney infection


def sore_throat():
    symptoms_question10 = input("Do you have a sore throat? ")
    if symptoms_question10.lower() == "yes":
        print("Possibilities include a throat infection")
    else:
        symptoms_question11 = input("""Do you have a back pain just above
the waist with chills and fever? """)
        if symptoms_question11.lower() == "yes":
            print("Possibilities include kidney infection")
        else:
            urinating()


# The sore_throat function is to test that whether
# you have a throat infection or kidney infection


def urinating():
    symptoms_question12 = input("""Do you have pain urinating or are you
urinating more often? """)
    if symptoms_question12.lower() == "yes":
        print("Possibilities include a urinary tract infection")
    else:
        sun_hurt()


# The sun_hurt function is to test that whether you have sunstroke
# or heat exhaustion or or whether your provided information is insufficient


def sun_hurt():
    symptoms_question13 = input("""Have you spent the day in the
sun or in hot conditions? """)
    if symptoms_question13.lower() == "yes":
        print("Possibilities sunstroke or heat exhaustion")
    else:
        print("Insufficient information to list possibilities")


main()
