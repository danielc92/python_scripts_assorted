import pandas as pd

#input variables
input_list = [5,1,3,4,5,2,20,23,25,30,45,20,10]
bin_count = 3
rounder = 4

#output variables
bin_list = []
output_list = []
output_list_str = []


#calculate min, max, range, bin size
max = round(max(input_list), rounder)
min = round(min(input_list),rounder)
the_range = max - min
bin_size = round(the_range / bin_count,rounder)

#append min to bin list before adding remaining items in while loop
bin_list.append(min)

start_position = 1
#generates list of bins
while start_position <= bin_count:
    bin_list.append(bin_list[start_position-1 ] + (bin_size))
    start_position = start_position + 1

#nested loop to bin items from input_list using bin_list
for n in range(len(input_list)):
    number = input_list[n]
    start_range = 0
    end_range = 0

    #first check if number is max or min and add to output list
    if number == min:
        output_list.append(bin_list[0])
    elif number == max:
        output_list.append(bin_list[len(bin_list)-2])
    #process remaining numbers other than min and max
    else:
        for n2 in range(len(bin_list)-1):
            if number > bin_list[n2] and number <= bin_list[n2 + 1]:
                output_list.append(bin_list[n2])
                break

for n in range(len(output_list)):
    lower_bound = round(output_list[n],rounder)
    upper_bound = round(output_list[n] + bin_size,rounder)
    spacer = " ~ "
    output_list_str.append(str(lower_bound) + spacer + str(upper_bound))

data = pd.concat([pd.Series(input_list), pd.Series(output_list_str)], axis = 1)
data.columns = ["input_values", "output_bins"]
print(data)