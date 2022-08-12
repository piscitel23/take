# # from InquirerPy import prompt
# from InquirerPy.validator import NumberValidator


# # # from InquirerPy import prompt
# from InquirerPy.base.control import Choice
# # # from InquirerPy.separator import Separator

# # # questions = [
# # #     {
# # #         "type": "list",
# # #         "message": "Select regions:",
# # #         "choices": [
# # #             Choice("ap-southeast-2", name="Sydney"),
# # #             Choice("ap-southeast-1", name="Singapore"),
# # #             Separator(),
# # #             "us-east-1",
# # #             "us-east-2",
# # #         ],
# # #         "multiselect": True,
# # #         "transformer": lambda result: f"{len(result)} region{'s' if len(result) > 1 else ''} selected",
# # #     },
# # # ]

# # # result = prompt(questions=questions)

# # # # def get_message(result):
# # # #     return f"Hi {result['confirm_name']}, enter your age:"

# # # # questions = [
# # # #     {
# # # #         "type": "input",
# # # #         "message": "Name:",
# # # #         "name": "name",
# # # #     },
# # # #     {
# # # #         "type": "input",
# # # #         "message": "Confirm Name:",
# # # #         "name": 'confirm_name',
# # # #         "default": lambda result: result["name"],   # inline lambda to make the code shorter
# # # #     },
# # # #     {
# # # #         "type": "input",
# # # #         "message": get_message,   # use a named function for more complex logic
# # # #         "name": 'age',
# # # #         "validate": NumberValidator(),
# # # #     },
# # # # ]

# # # # result = prompt(questions)
# # from InquirerPy import prompt
# # from InquirerPy.base.control import Choice

# # choices = [
# #     Choice("ap-southeast-2", name="Sydney", enabled=True),
# #     Choice("ap-southeast-1", name="Singapore", enabled=False),
# #     "us-east-1",
# #     "us-east-2",
# # ]

# # questions = [
# #     {
# #         "type": "checkbox",
# #         "message": "Select regions:",
# #         "choices": choices,
# #         "cycle": False,
# #         "transformer": lambda result: f"{len(result)} region{'s' if len(result) > 1 else ''} selected",
# #     }
# # ]

# # result = prompt(questions=questions)
# from InquirerPy import prompt

# q = prompt(
#     questions=[
#         {
#             "type": "list",
#             "message": "Select one:",
#             "choices": ["CFN","CFN drip"],
#             "filter": lambda result
#             "mandatory": False,
#         },
#         {
#             "type": "list",
#             "message": "Select one:",
#             "choices": ['Classic', 'Rich','Over Ice'],
#             "mandatory": True,
#             "mandatory_message": "Cannot skip"
#         },
#     ],
#     vi_mode=True,
# )
# result = inquirerPy.select(message = "Select one", choices = ["Fruit", "Meat", "Drinks", "Vegetable"]).execute()
# print(result)
# print(q)