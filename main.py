import inquirer
import q2   
import counter
import a
import add_to_list


# time = False
# sw = stopwatch.stopwatch()
# stopwatch(start())


#global test_counter
#test_counter = 0
a.get_date()
before = a.before_test()
durring = a.durring_test()
after = a.after_test()
#a.brew_info()
#counter.add_to_counter(test_counter)

#have the responces to the different parts to a bigger list

add_to_list.get_from_b(before)
add_to_list.get_from_d(durring)
item_list = add_to_list.get_from_a(after)
#print(item_list)

test = add_to_list.eq(before, after)

# work on - 
    # vessel size 
    # brew size

#find the equations that are used and implament it

 