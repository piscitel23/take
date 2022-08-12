# import os
# import re
# import sys
# from pprint import pprint
# from wsgiref import validate


# sys.path.append(os.path.realpath("."))
# import inquirer  # noqa

# #making sure that when a number is required,numbers are entered
# def num_validation(answers, current):
#     if not re.match(r"\+?\d", current):
#         raise inquirer.errors.ValidationError("", reason="try entering a number")
#     return True

# #making sure that when letters are required, letters are entered
# def letter_validation(answers, current):
#     # if (current)
#     if (current.isalpha()==False):
#         inquirer.ValidationError(message ="please try again")
#     return True


# def question():  

# #list of questions that the user answers to fill in the data
#     questions = [
#     #test number
#     #date
#         inquirer.Text("name", message="What's your name",validate = letter_validation),
   
#         inquirer.Text("unit", message="What unit are you using"),
#         inquirer.List('brew_type', message='what type of brew are you doing?', 
#             choices =['Classic', 'Rich','Over Ice']),#,validtae = brew_size),
#         inquirer.List('unit',message='what unit are you useing', choices =['CFN','CFN drip',]),
#     #find out if you can use the responce to brew type to get the answer to brew size

#         inquirer.Text("e_res", message="empty resivoir weight", validate=num_validation,),
#         inquirer.Text("f_res", message="filled resivoir weight", validate=num_validation,),
#         inquirer.List("grounds", message="what type of grounds are you using",
#             choices = ["grounds","pods"] ),
#         inquirer.List("vessel", message="which vessel are you using", 
#             choices = ["Carafe","Travel","Cup"]),
#     # inquirer.Text("", message="", validate=num_validation,),
#     ]

#     answers = inquirer.prompt(questions)

#     pprint(answers)
