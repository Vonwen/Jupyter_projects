
def cs_service_bot():
    print("Hello! Welcome to the DNS Cable Company's Service Portal. Are you a new or existing customer?\n[1] New Customer\n[2] Existing Customer")
    response = input("Please enter the number corresponding to your choice: ")
    if response == "1":
        new_customer()
    elif response == "2":
        existing_customer()
    else:
        print("Sorry, we didn't understand your selection.")
        cs_service_bot()



def existing_customer():
    print("What kind of support do you need?\n[1] Television Support\n[2] Internet Support\n[3] Speak to a support representative. ")
    response = input("Please enter the number corresponding to your choice: ")
    if response == "1":
        television_support()
    elif response == "2":
        internet_support()
    elif response == "3":
        live_rep("support")
    else:
        print("Sorry, we didn't understand your selection.")
        existing_customer()
    

def new_customer():
    print("We're excited to have you join the DNS family, how can we help you?\n[1] Sign up for service.\n[2] Schedule a home visit.\n[3] Speak to a sales representative.")
    response = input("Please enter the number corresponding to your choice: ")
    if response == "1":
        sign_up()
    elif response == "2":
        home_visit()
    elif response == "3":
        live_rep("sales")
    else:
        print("Sorry, we didn't understand your selection.")
        new_customer()           


def television_support():
    print("What is the nature of your problem?\n[1] I can't access certain channels.\n[2] My picture is blurry.[3] I keep losing service.\n[4] Other issues.")
    response = input("Please enter the number corresponding to your choice: ")
    if response == "1":
        print("Please check the channel lists at DefinitelyNotSinister.com. If the channel you cannot access is there, please contact a live representative.")
        did_that_help()
    elif response == "2":
        print("Try adjusting the antenna above your television set.")
        did_that_help()
    elif response == "3":
        print("Is it raining outside? If so, wait until it is not raining and then try again.")
        did_that_help()
    elif response == "4":
        live_rep("support")
    else:
        print("Sorry, we didn't understand your selection.")
        television_support()


def internet_support():
    print("What is the nature of your problem?\n[1] I can't connect to the internet.\n[2] My connection is very slow.\n[3] I can't access certain sites.\n[4] Other issues.")
    response = input("Please enter the number corresponding to your choice: ")
    if response == "1":
        print("Unplug your router, then plug it back in, then give it a good whack, like the Fonz.")
        did_that_help()
    elif response == "2":
        print("Make sure that all cell phones and other peoples computers are not connected to the internet, so that you can have all the bandwidth.")
        did_that_help()
    elif response == "3":
        print("Move to a different region or install a VPN. Some areas block certain sites.")
        did_that_help()
    elif response == "4":
        live_rep("support")
    else:
        print("Sorry, we didn't understand your selection.")
        internet_support()


def did_that_help():
    print("Did this solution solve your problem ?\n[1] Yes\n[2] No")
    response = input("Please enter the number corresponding to your choice: ")
    if response == "1":
        print("Thank you very much, have a great day!")
    elif response == "2":
        more_help = input("Would you rather talk to a live representative or schedule a home visit ?\n[1] Talk to a representative\n[2] Schedule a home visit")
        if more_help == "1":
            live_rep("support")
        elif more_help == "2":
            home_visit("support")
        else:
            print("Sorry, we didn't understand your selection.")
            did_that_help()
    else:
        print("Sorry, we didn't understand your selection.")
        did_that_help()    
            


def sign_up():
    print("Great choice, friend! We're excited to have you join the DNS family! Please select the package you are interested in signing up for.\n[1] Bundle Deal (Internet + Cable)\n[2] Internet\n[3] Cable")
    response = input("Please enter the number corresponding to your choice: ")
    if response == "1":
        print("You've selected the Bundle Package! Please schedule a home visit and our technician will come and set up your new service.")
        home_visit("new install")
    elif response == "2":
        print("You've selected the Internet Only Package! Please schedule a home visit and our technician will come and set up your new service.")
        home_visit("new install")
    elif response == "3":
        print("You've selected the Cable Only Package! Please schedule a home visit and our technician will come and set up your new service.")
        home_visit("new install")
    else:
        print("Sorry, we didn't understand your selection.")
        sign_up()


def home_visit(purpose="none"):
    if purpose == "none":
        response = input("What will be the purpose of the home visit?\n[1] New service installation.\n[2] Exisitng service repair.\n[3] Location scouting for unserviced region.")
        if response == "1":
            home_visit("new install")
        elif response == "2":
            home_visit("support")
        elif response == "3":
            home_visit("scout")
        else:
            print("Sorry, we didn't understand your selection.")
            home_visit()
    if purpose == "new install":
        visit_date = input("Please enter a date below when you are available for a technician to come to your home and install your service.")
        print("Wonderful! A technical will come visit you on " + visit_date + ". Please be available between the hours of 1:00 am and 11:00 pm.")
        return visit_date
    if purpose == "support":
        visit_date = input("Please enter a date below when you are available for a technician to come to your home and fix your problem.")
        print("Wonderful! A technical will come visit you on " + visit_date + ". Please be available between the hours of 1:00 am and 11:00 pm.")
        return visit_date
    if purpose == "scout":
        visit_date = input("Please enter a date below when you are available for a technician to come scout your region for expansion of our service.")
        print("Wonderful! A technical will come visit you on " + visit_date + ". Please be available between the hours of 1:00 am and 11:00 pm.")
        return visit_date


def live_rep(purpose):
    if purpose == "sales":
        print("Please hold while we connect you with a live sales representative. The wait time will be between two minutes and six hours. We thank you for your patience.")
    if purpose == "support":
        print("Please hold while we connect you with a live support representative. The wait time will be between two minutes and six hours. We thank you for your patience.")


cs_service_bot()
