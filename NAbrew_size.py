# def get_size(brew):
#     if brew == 'Classic':
#         brew_size_q = [
#             inquirer.List(
#                 'brew_size', 
#                 message='what is the brew size', 
#                 choices =[
#                     ('55','Carafe'),
#                     ('46','Carafe'),
#                     ('37','Carafe'),
#                     ('28','Carafe'),
#                     ('18','Travel'),
#                     ('14','Travel'),
#                     ('12','Cup'),
#                     ('10','Cup'),
#                     ('8','Cup')],)
#                 ]
#         s  = inquirer.prompt(brew_size_q)
      

#     elif brew == "Rich":
#         brew_size_q = [
#             inquirer.List(
#                 'brew_size', 
#                 message='what is the brew size', 
#                 choices =[
#                     ('47','Carafe'),
#                     ('41','Carafe'),
#                     ('33','Carafe'),
#                     ('26','Carafe'),
#                     ('16','Travel'),
#                     ('12','Travel'),
#                     ('10','Cup'),
#                     ('8','Cup'),
#                     ('7','Cup')],)
#                     ]
#         s  = inquirer.prompt(brew_size_q)
#     elif brew== "Over Ice":
#         brew_size_q = [
#             inquirer.List(
#                 'brew_size', 
#                 message='what is the brew size', 
#                 choices =[
#                     ('55','Carafe'),
#                     ('46','Carafe'),
#                     ('37','Carafe'),
#                     ('28','Carafe'),
#                     ('18','Travel'),
#                     ('14','Travel'),
#                     ('12','Cup'),
#                     ('10','Cup'),
#                     ('8','Cup')],)
#                 ]
#         s  = inquirer.prompt(brew_size_q)
#     print("Vessel: " + s['brew_size'])
#     return s