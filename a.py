import inquirer
from datetime import date
import stopwatch 

#making sure that when a number is required,numbers are entered
def num_validation(answers, current):
    if float(current):
        return True
    else:
        return False


#making sure that when letters are required, letters are entered
def letter_validation(answers, current):
    # if (current)
    if (current.isalpha()==False):
        inquirer.ValidationError(message ="please try again")
    return True



#
def valadate_size(answer, current):
    get_size()

#
def brew_info():
    basic = [


    #get the type of grounds that are being used for the test
        inquirer.List("grounds", message="what type of grounds are you using",
            choices = ["grounds","pods"] ),

    
    ]

#
def before_test():
    before = [
            #name
        inquirer.Text("name", message="What's your name",validate = letter_validation),

            #unit
        inquirer.List("unit", message="What unit are you using",choices = ["CFN","CFN drip",""]),
    
            #brew type
        inquirer.List('brew_type', message='what type of brew are you doing?', 
            choices =['Classic', 'Rich','Over Ice'],),

            #UI test
        inquirer.Text("SW Version (UI)", message = "what sw version (UI) are you using"),
            #PW test
        inquirer.Text("SW Version (PW)", message = "what sw version (PW) are you using"),
    
            #empty resivior weight
        inquirer.Text("e_res", message="empty resivoir weight", validate=num_validation,),

            #full resivior weight
        inquirer.Text("f_res", message="filled resivoir weight", validate=num_validation,),

            #filler res basket and filter
        inquirer.Text("empty brew basket", message = 'enter empty brew basket and filter weight',validate = num_validation),

            #get the type of grounds that are being used for the test
        inquirer.List("grounds", message="what type of grounds are you using",
            choices = ["grounds","pods"] ),

            #pre test water temp
        inquirer.Text("pre water temp", message="what is the pre test water temp", validate=num_validation,),
    ]    
    answers = inquirer.prompt(before)
    #print(answers)
    return answers 
    

#
def durring_test():
    global timer 
    timer = False
    start = stopwatch.start_clock(timer)
    stop = stopwatch.stop_clock(start)
    #print()
    return stop
    

#
def after_test():
    after = [
        inquirer.Text("voltage", message = "what was the voltage", validate=num_validation),
        inquirer.Text("post vessel weight", message="what is the vessel weight after test", validate=num_validation,),
        inquirer.Text("post basket weight", message="what is the post basket weight", validate=num_validation,),
        inquirer.Text("post res weight", message="what is the post test resivior weight", validate=num_validation,),
        inquirer.Text("post temp", message="Enter the temp after test", validate=num_validation,),
        inquirer.Text("TDS",message = "TDS", validate = num_validation),
        inquirer.Text("TDS2",message = "TDS 2", validate = num_validation),
        inquirer.Text("TDS3",message = "TDS 3", validate = num_validation)
        #inquirer.Text("", message="", validate=num_validation,),
                
    ]
    answers = inquirer.prompt(after)
    #print(answers)
    return answers





#
def get_date():
        current_date = date.today()
        d = str(current_date)
        print("Date:",d) 
