# result_sum	The result of adding first_number and second_number. This variable is already declared in the example code above.
# result_difference	The result of subtracting second_number from first_number.
# result_product	The result of multiplying first_number and second_number.
# result_quotient	The result of dividing first_number by second_number.




import sys

# This code reads in arguments and converts those inputs to decimal numbers
first_number = float(sys.argv[1])
second_number = float(sys.argv[2])

result_sum = first_number + second_number
result_difference = first_number - second_number
result_product = first_number * second_number
result_quotient	= first_number / second_number

#print(f"{first_number} plus {second_number} equals {result_sum}")

