# Import necessary libraries
import math
import matplotlib.pyplot as plt


def get_int_input(prompt):
	# loop until a valid integer is entered
	valid_input = False
	value = 0
	while valid_input is False:
		try:
			value = int(input(prompt))
			valid_input = True
		except ValueError:
			print("Invalid input. Please enter an integer value.")
	return value


def get_float_input(prompt):
	# loop until a valid float is entered
	valid_input = False
	value = 0.0
	while valid_input is False:
		try:
			value = float(input(prompt))
			valid_input = True
		except ValueError:
			print("Invalid input. Please enter a numeric value.")
	return value


def get_positive_float_input(prompt):
	# loop until a valid positive float is entered
	valid_input = False
	value = 0.0
	while valid_input is False:
		try:
			value = float(input(prompt))
			if value > 0:
				valid_input = True
			elif value == 0:
				print("Value cannot be zero. Please enter a positive number.")
			else:
				print("Value cannot be negative. Please enter a positive number.")
		except ValueError:
			print("Invalid input. Please enter a numeric value.")
	return value


def get_non_negative_float_input(prompt):
	# loop until a valid non-negative float is entered
	valid_input = False
	value = 0.0
	while valid_input is False:
		try:
			value = float(input(prompt))
			if value >= 0:
				valid_input = True
			else:
				print("Value cannot be negative. Please enter a non-negative number.")
		except ValueError:
			print("Invalid input. Please enter a numeric value.")
	return value


def get_positive_rate_input(prompt):
	# loop until a valid non-negative rate is entered
	valid_input = False
	value = 0.0
	while valid_input is False:
		try:
			value = float(input(prompt))
			if value >= 0:
				valid_input = True
			else:
				print("Rate cannot be negative. Please enter a non-negative rate.")
		except ValueError:
			print("Invalid input. Please enter a numeric value.")
	return value


def display_menu():
	# display the main operations menu
	print("\nChoose the operation you wish to perform:")
	print("1. Interest rate conversions")
	print("2. Annuity calculations")
	print("3. Interest and capital components")
	print("4. Annuity calculations (increasing every period)")
	print("5. Simple interest")
	print("6. Effective interest")
	print("7. Effective periodic interest")
	print("8. Continuous interest")
	print("9. View graphs")
	print("10. Exit program")


def interest_rate_conversion():
	# display the conversion sub-menu
	print("\nInterest rate conversions selected.")
	print("1. Simple interest")
	print("2. Effective")
	print("3. Effective periodic")
	print("4. Nominal")
	print("5. Continuous")

	# get the source and target conversion types
	convert_from = get_int_input("Enter the option you would like to convert from: ")
	convert_to = get_int_input("Enter the option you would like to convert to: ")
	print(f"Converting from option {convert_from} to option {convert_to}.")

	if convert_from == 1 and convert_to == 2:
		# simple interest to effective annual rate
		simple_interest = get_positive_rate_input("Enter the simple interest rate (%): ")
		given_periods = get_positive_float_input("Enter the given compounding periods per year: ")
		effective_rate = (1 + (simple_interest / 100) * given_periods) - 1
		print(f"The effective interest rate is: {effective_rate * 100:.5f}%")

	elif convert_from == 1 and convert_to == 3:
		# simple interest to effective periodic rate
		simple_interest = get_positive_rate_input("Enter the simple interest rate (%): ")
		given_periods = get_positive_float_input("Enter the given compounding periods per year: ")
		required_periods = get_positive_float_input("Enter the required compounding periods per year: ")
		effective_rate = (1 + (simple_interest / 100) * given_periods) - 1
		effective_periodic_rate = (1 + effective_rate) ** (1 / required_periods) - 1
		print(f"The effective periodic interest rate is: {effective_periodic_rate * 100:.5f}%")

	elif convert_from == 1 and convert_to == 4:
		# simple interest to nominal rate
		simple_interest = get_positive_rate_input("Enter the simple interest rate (%): ")
		given_periods = get_positive_float_input("Enter the given compounding periods per year: ")
		required_periods = get_positive_float_input("Enter the required compounding periods per year: ")
		effective_rate = (1 + (simple_interest / 100) * given_periods) - 1
		nominal_rate = ((1 + effective_rate) ** (1 / required_periods) - 1) * required_periods
		print(f"The nominal interest rate is: {nominal_rate * 100:.5f}%")

	elif convert_from == 1 and convert_to == 5:
		# simple interest to continuous (force of interest)
		simple_interest = get_positive_rate_input("Enter the simple interest rate (%): ")
		given_periods = get_positive_float_input("Enter the given compounding periods per year: ")
		effective_rate = (1 + (simple_interest / 100) * given_periods) - 1
		continuous_rate = math.log(1 + effective_rate)
		print(f"The continuous interest rate is: {continuous_rate * 100:.5f}%")

	elif convert_from == 2 and convert_to == 1:
		# effective annual rate to simple interest
		effective_rate = get_positive_rate_input("Enter the effective interest rate (%): ")
		required_periods = get_positive_float_input("Enter the required compounding periods per year: ")
		simple_interest = (effective_rate / 100) / required_periods
		print(f"The simple interest rate is: {simple_interest * 100:.5f}%")

	elif convert_from == 2 and convert_to == 3:
		# effective annual rate to effective periodic rate
		effective_rate = get_positive_rate_input("Enter the effective interest rate (%): ")
		required_periods = get_positive_float_input("Enter the required compounding periods per year: ")
		effective_periodic_rate = (1 + (effective_rate / 100)) ** (1 / required_periods) - 1
		print(f"The effective periodic interest rate is: {effective_periodic_rate * 100:.5f}%")

	elif convert_from == 2 and convert_to == 4:
		# effective annual rate to nominal rate
		effective_rate = get_positive_rate_input("Enter the effective interest rate (%): ")
		required_periods = get_positive_float_input("Enter the required compounding periods per year: ")
		nominal_rate = ((1 + (effective_rate / 100)) ** (1 / required_periods) - 1) * required_periods
		print(f"The nominal interest rate is: {nominal_rate * 100:.5f}%")

	elif convert_from == 2 and convert_to == 5:
		# effective annual rate to continuous (force of interest)
		effective_rate = get_positive_rate_input("Enter the effective interest rate (%): ")
		continuous_rate = math.log(1 + (effective_rate / 100))
		print(f"The continuous interest rate is: {continuous_rate * 100:.5f}%")

	elif convert_from == 3 and convert_to == 1:
		# effective periodic rate to simple interest
		effective_periodic_rate = get_positive_rate_input("Enter the effective periodic interest rate (%): ")
		given_periods = get_positive_float_input("Enter the given compounding periods per year: ")
		required_periods = get_positive_float_input("Enter the required compounding periods per year: ")
		effective_rate = (1 + (effective_periodic_rate / 100)) ** given_periods - 1
		simple_interest = effective_rate / required_periods
		print(f"The simple interest rate is: {simple_interest * 100:.5f}%")

	elif convert_from == 3 and convert_to == 2:
		# effective periodic rate to effective annual rate
		effective_periodic_rate = get_positive_rate_input("Enter the effective periodic interest rate (%): ")
		given_periods = get_positive_float_input("Enter the given compounding periods per year: ")
		effective_rate = (1 + (effective_periodic_rate / 100)) ** given_periods - 1
		print(f"The effective interest rate is: {effective_rate * 100:.5f}%")

	elif convert_from == 3 and convert_to == 4:
		# effective periodic rate to nominal rate
		effective_periodic_rate = get_positive_rate_input("Enter the effective periodic interest rate (%): ")
		required_periods = get_positive_float_input("Enter the required compounding periods per year: ")
		nominal_rate = (effective_periodic_rate / 100) * required_periods
		print(f"The nominal interest rate is: {nominal_rate * 100:.5f}%")

	elif convert_from == 3 and convert_to == 5:
		# effective periodic rate to continuous (force of interest)
		effective_periodic_rate = get_positive_rate_input("Enter the effective periodic interest rate (%): ")
		given_periods = get_positive_float_input("Enter the given compounding periods per year: ")
		effective_rate = (1 + (effective_periodic_rate / 100)) ** given_periods - 1
		continuous_rate = math.log(1 + effective_rate)
		print(f"The continuous interest rate is: {continuous_rate * 100:.5f}%")

	elif convert_from == 4 and convert_to == 1:
		# nominal rate to simple interest
		nominal_rate = get_positive_rate_input("Enter the nominal interest rate (%): ")
		given_periods = get_positive_float_input("Enter the given compounding periods per year: ")
		required_periods = get_positive_float_input("Enter the required compounding periods per year: ")
		effective_rate = (1 + (nominal_rate / 100) / given_periods) ** given_periods - 1
		simple_interest = effective_rate / required_periods
		print(f"The simple interest rate is: {simple_interest * 100:.5f}%")

	elif convert_from == 4 and convert_to == 2:
		# nominal rate to effective annual rate
		nominal_rate = get_positive_rate_input("Enter the nominal interest rate (%): ")
		given_periods = get_positive_float_input("Enter the given compounding periods per year: ")
		effective_rate = (1 + (nominal_rate / 100) / given_periods) ** given_periods - 1
		print(f"The effective interest rate is: {effective_rate * 100:.5f}%")

	elif convert_from == 4 and convert_to == 3:
		# nominal rate to effective periodic rate
		nominal_rate = get_positive_rate_input("Enter the nominal interest rate (%): ")
		given_periods = get_positive_float_input("Enter the given compounding periods per year: ")
		required_periods = get_positive_float_input("Enter the required compounding periods per year: ")
		effective_rate = (1 + (nominal_rate / 100) / given_periods) ** given_periods - 1
		effective_periodic_rate = (1 + effective_rate) ** (1 / required_periods) - 1
		print(f"The effective periodic interest rate is: {effective_periodic_rate * 100:.5f}%")

	elif convert_from == 4 and convert_to == 5:
		# nominal rate to continuous (force of interest)
		nominal_rate = get_positive_rate_input("Enter the nominal interest rate (%): ")
		given_periods = get_positive_float_input("Enter the given compounding periods per year: ")
		effective_rate = (1 + (nominal_rate / 100) / given_periods) ** given_periods - 1
		continuous_rate = math.log(1 + effective_rate)
		print(f"The continuous interest rate is: {continuous_rate * 100:.5f}%")

	elif convert_from == 5 and convert_to == 1:
		# continuous (force of interest) to simple interest
		continuous_rate = get_positive_rate_input("Enter the continuous interest rate (%): ")
		required_periods = get_positive_float_input("Enter the required compounding periods per year: ")
		effective_rate = math.exp(continuous_rate / 100) - 1
		simple_interest = effective_rate / required_periods
		print(f"The simple interest rate is: {simple_interest * 100:.5f}%")

	elif convert_from == 5 and convert_to == 2:
		# continuous (force of interest) to effective annual rate
		continuous_rate = get_positive_rate_input("Enter the continuous interest rate (%): ")
		effective_rate = math.exp(continuous_rate / 100) - 1
		print(f"The effective interest rate is: {effective_rate * 100:.5f}%")

	elif convert_from == 5 and convert_to == 3:
		# continuous (force of interest) to effective periodic rate
		continuous_rate = get_positive_rate_input("Enter the continuous interest rate (%): ")
		required_periods = get_positive_float_input("Enter the required compounding periods per year: ")
		effective_rate = math.exp(continuous_rate / 100) - 1
		effective_periodic_rate = (1 + effective_rate) ** (1 / required_periods) - 1
		print(f"The effective periodic interest rate is: {effective_periodic_rate * 100:.5f}%")

	elif convert_from == 5 and convert_to == 4:
		# continuous (force of interest) to nominal rate
		continuous_rate = get_positive_rate_input("Enter the continuous interest rate (%): ")
		required_periods = get_positive_float_input("Enter the required compounding periods per year: ")
		effective_rate = math.exp(continuous_rate / 100) - 1
		nominal_rate = ((1 + effective_rate) ** (1 / required_periods) - 1) * required_periods
		print(f"The nominal interest rate is: {nominal_rate * 100:.5f}%")

	elif convert_from == convert_to:
		# same option selected on both sides: no conversion required
		print("The same option was selected for both sides. No conversion is required.")

	else:
		# any option number outside the valid range 1 to 5
		print("Invalid conversion selected.")


def annuity_future_value():
	# future value of a level annuity in arrears
	print("\nFuture value of a level annuity (arrears).")
	initial_amount = get_positive_float_input("Enter the periodic payment amount (X): ")
	rate = get_positive_rate_input("Enter the effective interest rate per period (%): ") / 100
	time = get_positive_float_input("Enter the time in years: ")
	periods = get_positive_float_input("Enter the number of compounding periods per year: ")
	number_of_payments = periods * time
	
	if rate == 0:
		future_value = initial_amount * number_of_payments
	else:
		future_value = initial_amount * (((1 + rate) ** number_of_payments - 1) / rate)
	print(f"The future value is: R{future_value:.2f}")


def annuity_payment_from_future_value():
	# solve for the periodic payment given a target future value
	print("\nPeriodic payment given a target future value.")
	future_value = get_positive_float_input("Enter the target future value: ")
	rate = get_positive_rate_input("Enter the effective interest rate per period (%): ") / 100
	time = get_positive_float_input("Enter the time in years: ")
	periods = get_positive_float_input("Enter the number of compounding periods per year: ")
	number_of_payments = periods * time
	
	if rate == 0:
		payment = future_value / number_of_payments
	else:
		payment = future_value / (((1 + rate) ** number_of_payments - 1) / rate)
	print(f"The periodic payment is: R{payment:.2f}")


def annuity_time_from_future_value():
	# solve for the time in years given a target future value
	print("\nTime in years given a target future value.")
	payment = get_positive_float_input("Enter the periodic payment amount (X): ")
	rate = get_positive_rate_input("Enter the effective interest rate per period (%): ") / 100
	future_value = get_positive_float_input("Enter the target future value: ")
	periods = get_positive_float_input("Enter the number of compounding periods per year: ")
	
	if rate == 0:
		number_of_payments = future_value / payment
	else:
		argument = (future_value * rate / payment) + 1
		if argument <= 0:
			print("Error: The calculated value would require negative time. Please check your inputs.")
			return
		number_of_payments = math.log(argument) / math.log(1 + rate)
	time = number_of_payments / periods
	print(f"The time in years is: {time:.2f}")
	print(f"The time in months is: {time * 12:.2f}")


def annuity_present_value():
	# present value of a level annuity in arrears
	print("\nPresent value of a level annuity (arrears).")
	payment = get_positive_float_input("Enter the periodic payment amount (X): ")
	rate = get_positive_rate_input("Enter the effective interest rate per period (%): ") / 100
	time = get_positive_float_input("Enter the time in years: ")
	periods = get_positive_float_input("Enter the number of compounding periods per year: ")
	number_of_payments = periods * time
	
	if rate == 0:
		present_value = payment * number_of_payments
	else:
		present_value = payment * ((1 - (1 + rate) ** -number_of_payments) / rate)
	print(f"The present value is: R{present_value:.2f}")


def annuity_payment_from_present_value():
	# solve for the periodic payment given a present value
	print("\nPeriodic payment given a present value.")
	present_value = get_positive_float_input("Enter the present value: ")
	rate = get_positive_rate_input("Enter the effective interest rate per period (%): ") / 100
	time = get_positive_float_input("Enter the time in years: ")
	periods = get_positive_float_input("Enter the number of compounding periods per year: ")
	number_of_payments = periods * time
	
	if rate == 0:
		payment = present_value / number_of_payments
	else:
		payment = present_value * rate / (1 - (1 + rate) ** -number_of_payments)
	print(f"The periodic payment is: R{payment:.2f}")


def annuity_time_from_present_value():
	# solve for the time in years given a present value
	print("\nTime in years given a present value.")
	present_value = get_positive_float_input("Enter the present value: ")
	rate = get_positive_rate_input("Enter the effective interest rate per period (%): ") / 100
	payment = get_positive_float_input("Enter the periodic payment amount (X): ")
	periods = get_positive_float_input("Enter the number of compounding periods per year: ")
	
	if rate == 0:
		number_of_payments = present_value / payment
	else:
		argument = 1 - (present_value * rate / payment)
		if argument <= 0:
			print("Error: The loan would never be paid off with these payments. Please increase payment amount.")
			return
		number_of_payments = -math.log(argument) / math.log(1 + rate)
	time = number_of_payments / periods
	print(f"The time in years is: {time:.2f}")
	print(f"The time in months is: {time * 12:.2f}")


def annuity_balance_outstanding():
	# balance outstanding on a loan after a given number of payments
	print("\nBalance outstanding after a given number of payments.")
	loan_amount = get_positive_float_input("Enter the original loan amount: ")
	rate = get_positive_rate_input("Enter the effective interest rate per period (%): ") / 100
	payment = get_positive_float_input("Enter the periodic payment amount: ")
	payment_number = get_non_negative_float_input("Enter the number of payments already made: ")
	
	if rate == 0:
		balance_outstanding = loan_amount - payment * payment_number
	else:
		balance_outstanding = loan_amount * (1 + rate) ** payment_number - payment * (((1 + rate) ** payment_number - 1) / rate)
	
	if balance_outstanding < 0:
		balance_outstanding = 0
	print(f"The balance outstanding is: R{balance_outstanding:.2f}")


def accumulated_value_with_withdrawals():
	# accumulated value of an investment with regular level withdrawals
	print("\nAccumulated value with regular withdrawals.")
	print("AV = C(1 + i)^np - X((1 + i)^np - 1) / i")
	investment_amount = get_positive_float_input("Enter the initial investment amount (C): ")
	rate = get_positive_rate_input("Enter the effective interest rate per period (%): ") / 100
	periods = get_positive_float_input("Enter the number of compounding periods per year (p): ")
	time = get_positive_float_input("Enter the number of years (n): ")
	withdrawal = get_positive_float_input("Enter the amount withdrawn per period (X): ")
	number_of_periods = periods * time
	
	if rate == 0:
		accumulated_value = investment_amount - withdrawal * number_of_periods
	else:
		accumulated_value = investment_amount * (1 + rate) ** number_of_periods - withdrawal * (((1 + rate) ** number_of_periods - 1) / rate)
	
	if accumulated_value < 0:
		accumulated_value = 0
	print(f"The accumulated value with withdrawals is: R{accumulated_value:.2f}")


def accumulated_value_with_investments():
	# accumulated value of an investment with regular level additional investments
	print("\nAccumulated value with regular additional investments.")
	print("AV = C(1 + i)^np + X((1 + i)^np - 1) / i")
	investment_amount = get_positive_float_input("Enter the initial investment amount (C): ")
	rate = get_positive_rate_input("Enter the effective interest rate per period (%): ") / 100
	periods = get_positive_float_input("Enter the number of compounding periods per year (p): ")
	time = get_positive_float_input("Enter the number of years (n): ")
	additional_investment = get_positive_float_input("Enter the amount invested per period (X): ")
	number_of_periods = periods * time
	
	if rate == 0:
		accumulated_value = investment_amount + additional_investment * number_of_periods
	else:
		accumulated_value = investment_amount * (1 + rate) ** number_of_periods + additional_investment * (((1 + rate) ** number_of_periods - 1) / rate)
	print(f"The accumulated value with investments is: R{accumulated_value:.2f}")


def present_value_from_accumulated_value():
	# present value of a known accumulated value
	print("\nPresent value of a known accumulated value.")
	print("PV = AV(1 + i)^-np")
	accumulated_value = get_positive_float_input("Enter the accumulated value (AV): ")
	rate = get_positive_rate_input("Enter the effective interest rate per period (%): ") / 100
	periods = get_positive_float_input("Enter the number of compounding periods per year (p): ")
	time = get_positive_float_input("Enter the number of years (n): ")
	number_of_periods = periods * time
	present_value = accumulated_value * (1 + rate) ** -number_of_periods
	print(f"The present value is: R{present_value:.2f}")


def annuity_due_future_value():
	# future value of a level annuity-due (payments in advance)
	print("\nFuture value of a level annuity-due (payments in advance).")
	payment = get_positive_float_input("Enter the periodic payment amount (X): ")
	rate = get_positive_rate_input("Enter the effective interest rate per period (%): ") / 100
	time = get_positive_float_input("Enter the time in years: ")
	periods = get_positive_float_input("Enter the number of compounding periods per year: ")
	number_of_payments = periods * time
	
	if rate == 0:
		future_value = payment * number_of_payments
	else:
		future_value = payment * (1 + rate) * (((1 + rate) ** number_of_payments - 1) / rate)
	print(f"The future value in advance is: R{future_value:.2f}")


def annuity_due_present_value():
	# present value of a level annuity-due (payments in advance)
	print("\nPresent value of a level annuity-due (payments in advance).")
	payment = get_positive_float_input("Enter the periodic payment amount (X): ")
	rate = get_positive_rate_input("Enter the effective interest rate per period (%): ") / 100
	time = get_positive_float_input("Enter the time in years: ")
	periods = get_positive_float_input("Enter the number of compounding periods per year: ")
	number_of_payments = periods * time
	
	if rate == 0:
		present_value = payment * number_of_payments
	else:
		present_value = payment * (1 + rate) * ((1 - (1 + rate) ** -number_of_payments) / rate)
	print(f"The present value in advance is: R{present_value:.2f}")


def loan_arrears_amount():
	# loan amount supported by level payments made in arrears
	print("\nLoan amount supported by level payments in arrears.")
	payment = get_positive_float_input("Enter the periodic payment amount: ")
	rate = get_positive_rate_input("Enter the effective interest rate per period (%): ") / 100
	time = get_positive_float_input("Enter the time in years: ")
	periods = get_positive_float_input("Enter the number of compounding periods per year: ")
	number_of_payments = periods * time
	
	if rate == 0:
		loan_amount = payment * number_of_payments
	else:
		loan_amount = payment * ((1 - (1 + rate) ** -number_of_payments) / rate)
	print(f"The loan amount is: R{loan_amount:.2f}")


def loan_arrears_payment():
	# level payment in arrears required to repay a loan
	print("\nLevel payment in arrears required to repay a loan.")
	loan_amount = get_positive_float_input("Enter the loan amount: ")
	rate = get_positive_rate_input("Enter the effective interest rate per period (%): ") / 100
	time = get_positive_float_input("Enter the time in years: ")
	periods = get_positive_float_input("Enter the number of compounding periods per year: ")
	number_of_payments = periods * time
	
	if rate == 0:
		payment = loan_amount / number_of_payments
	else:
		payment = loan_amount * rate / (1 - (1 + rate) ** -number_of_payments)
	print(f"The payment amount is: R{payment:.2f}")


def loan_arrears_number_of_payments():
	# number of level payments in arrears required to repay a loan
	print("\nNumber of payments in arrears required to repay a loan.")
	loan_amount = get_positive_float_input("Enter the loan amount: ")
	payment = get_positive_float_input("Enter the periodic payment amount: ")
	rate = get_positive_rate_input("Enter the effective interest rate per period (%): ") / 100
	periods = get_positive_float_input("Enter the number of compounding periods per year: ")
	
	if rate == 0:
		number_of_payments = loan_amount / payment
	else:
		argument = 1 - (loan_amount * rate / payment)
		if argument <= 0:
			print("Error: The loan would never be paid off with these payments. Please increase payment amount.")
			return
		number_of_payments = -math.log(argument) / math.log(1 + rate)
	time = number_of_payments / periods
	print(f"The number of payments is: {number_of_payments:.2f}")
	print(f"The time in years is: {time:.2f}")


def loan_advance_amount():
	# loan amount supported by level instalments paid in advance
	print("\nLoan amount supported by level instalments in advance.")
	instalment = get_positive_float_input("Enter the periodic instalment amount: ")
	rate = get_positive_rate_input("Enter the effective interest rate per period (%): ") / 100
	time = get_positive_float_input("Enter the time in years: ")
	periods = get_positive_float_input("Enter the number of compounding periods per year: ")
	number_of_payments = periods * time
	
	if rate == 0:
		loan_amount = instalment * number_of_payments
	else:
		loan_amount = instalment * (1 + rate) * ((1 - (1 + rate) ** -number_of_payments) / rate)
	print(f"The loan amount is: R{loan_amount:.2f}")


def loan_advance_instalment():
	# level instalment in advance required to repay a loan
	print("\nLevel instalment in advance required to repay a loan.")
	loan_amount = get_positive_float_input("Enter the loan amount: ")
	rate = get_positive_rate_input("Enter the effective interest rate per period (%): ") / 100
	time = get_positive_float_input("Enter the time in years: ")
	periods = get_positive_float_input("Enter the number of compounding periods per year: ")
	number_of_payments = periods * time
	
	if rate == 0:
		instalment = loan_amount / number_of_payments
	else:
		instalment = loan_amount * rate / ((1 + rate) * (1 - (1 + rate) ** -number_of_payments))
	print(f"The instalment amount is: R{instalment:.2f}")


def loan_advance_balance_outstanding():
	# balance outstanding on a loan repaid by instalments in advance
	print("\nBalance outstanding for a loan repaid by instalments in advance.")
	loan_amount = get_positive_float_input("Enter the original loan amount: ")
	instalment = get_positive_float_input("Enter the periodic instalment amount: ")
	rate = get_positive_rate_input("Enter the effective interest rate per period (%): ") / 100
	payment_number = get_non_negative_float_input("Enter the number of instalments already paid: ")
	
	if rate == 0:
		balance_outstanding = loan_amount - instalment * payment_number
	else:
		balance_outstanding = loan_amount * (1 + rate) ** payment_number - instalment * (1 + rate) * (((1 + rate) ** payment_number - 1) / rate)
	
	if balance_outstanding < 0:
		balance_outstanding = 0
	print(f"The balance outstanding is: R{balance_outstanding:.2f}")


def loan_advance_interest_component():
	# interest component of a given instalment, loan repaid in advance
	print("\nInterest component of a given instalment (advance).")
	loan_amount = get_positive_float_input("Enter the loan amount: ")
	instalment = get_positive_float_input("Enter the instalment amount: ")
	rate = get_positive_rate_input("Enter the effective interest rate per period (%): ") / 100
	payment_number = get_int_input("Enter the instalment number: ") - 1
	
	if rate == 0:
		interest_component = 0
	else:
		interest_component = (loan_amount * rate - instalment * (1 + rate)) * (1 + rate) ** payment_number + instalment * (1 + rate)
	
	if interest_component < 0:
		interest_component = 0
	print(f"The interest component is: R{interest_component:.2f}")


def loan_advance_capital_component():
	# capital component of a given instalment from instalment and interest
	print("\nCapital component of a given instalment.")
	instalment = get_positive_float_input("Enter the instalment amount: ")
	interest_component = get_non_negative_float_input("Enter the interest component: ")
	capital_component = instalment - interest_component
	
	if capital_component < 0:
		capital_component = 0
	print(f"The capital component is: R{capital_component:.2f}")


def loan_advance_number_of_payments():
	# number of instalments in advance required to repay a loan
	print("\nNumber of instalments in advance required to repay a loan.")
	loan_amount = get_positive_float_input("Enter the loan amount: ")
	instalment = get_positive_float_input("Enter the periodic instalment amount: ")
	rate = get_positive_rate_input("Enter the effective interest rate per period (%): ") / 100
	
	if rate == 0:
		number_of_payments = loan_amount / instalment
	else:
		argument = 1 - (loan_amount * rate / (instalment * (1 + rate)))
		if argument <= 0:
			print("Error: The loan would never be paid off with these instalments. Please increase instalment amount.")
			return
		number_of_payments = -math.log(argument) / math.log(1 + rate)
	print(f"The number of instalments is: {number_of_payments:.2f}")


def loan_last_payment():
	# value of the final payment given the balance outstanding before it
	print("\nValue of the final payment.")
	print("Use the balance outstanding immediately before the final payment.")
	balance_outstanding = get_positive_float_input("Enter the balance outstanding before the final payment: ")
	rate = get_positive_rate_input("Enter the effective interest rate per period (%): ") / 100
	last_payment = balance_outstanding * (1 + rate)
	print(f"The last payment is: R{last_payment:.2f}")


def annuity_calculations():
	# display the annuity calculations sub-menu
	print("\nAnnuity calculations selected.")
	print("Use the interest rate per payment period for all calculations.")
	print("Use option 1 on the main menu to convert rates if required.")
	print("1. Future value (arrears)")
	print("2. Present value (arrears)")
	print("3. Balance outstanding")
	print("4. Accumulated value with withdrawals")
	print("5. Accumulated value with investments")
	print("6. Present value of an accumulated value")
	print("7. Future value (annuity-due)")
	print("8. Present value (annuity-due)")
	print("9. Loan calculations (arrears)")
	print("10. Loan calculations (advance)")
	choice = get_int_input("Enter your choice (1 - 10): ")

	if choice == 1:
		annuity_future_value()
	elif choice == 2:
		annuity_present_value()
	elif choice == 3:
		annuity_balance_outstanding()
	elif choice == 4:
		accumulated_value_with_withdrawals()
	elif choice == 5:
		accumulated_value_with_investments()
	elif choice == 6:
		present_value_from_accumulated_value()
	elif choice == 7:
		annuity_due_future_value()
	elif choice == 8:
		annuity_due_present_value()
	elif choice == 9:
		loan_calculations_arrears()
	elif choice == 10:
		loan_calculations_advance()
	else:
		print("Invalid choice. Please select a number between 1 and 10.")


def loan_calculations_arrears():
	# display the loan calculations (arrears) sub-menu
	print("\nLoan calculations (arrears) selected.")
	print("1. Loan amount")
	print("2. Payment amount")
	print("3. Number of payments")
	print("4. Last payment")
	choice = get_int_input("Enter your choice (1 - 4): ")

	if choice == 1:
		loan_arrears_amount()
	elif choice == 2:
		loan_arrears_payment()
	elif choice == 3:
		loan_arrears_number_of_payments()
	elif choice == 4:
		loan_last_payment()
	else:
		print("Invalid choice. Please select a number between 1 and 4.")


def loan_calculations_advance():
	# display the loan calculations (advance) sub-menu
	print("\nLoan calculations (advance) selected.")
	print("1. Loan amount")
	print("2. Instalment amount")
	print("3. Balance outstanding")
	print("4. Interest component")
	print("5. Capital component")
	print("6. Number of instalments")
	print("7. Last payment")
	choice = get_int_input("Enter your choice (1 - 7): ")

	if choice == 1:
		loan_advance_amount()
	elif choice == 2:
		loan_advance_instalment()
	elif choice == 3:
		loan_advance_balance_outstanding()
	elif choice == 4:
		loan_advance_interest_component()
	elif choice == 5:
		loan_advance_capital_component()
	elif choice == 6:
		loan_advance_number_of_payments()
	elif choice == 7:
		loan_last_payment()
	else:
		print("Invalid choice. Please select a number between 1 and 7.")


def interest_component_from_formula():
	# interest component of a given payment, loan repaid in arrears
	print("\nInterest component of a given payment (formula).")
	loan_amount = get_positive_float_input("Enter the original loan amount: ")
	rate = get_positive_rate_input("Enter the effective interest rate per period (%): ") / 100
	payment_number = get_int_input("Enter the payment number: ")
	payment = get_positive_float_input("Enter the payment amount: ")
	
	if rate == 0:
		interest_component = 0
	else:
		interest_component = (loan_amount * rate - payment) * (1 + rate) ** (payment_number - 1) + payment
	
	if interest_component < 0:
		interest_component = 0
	print(f"The interest component is: R{interest_component:.2f}")


def interest_component_from_balance():
	# interest component of the next payment using the balance outstanding
	print("\nInterest component of the next payment (from balance outstanding).")
	print("Use option 3 under annuity calculations to find the balance outstanding.")
	balance_outstanding = get_positive_float_input("Enter the balance outstanding: ")
	rate = get_positive_rate_input("Enter the effective interest rate per period (%): ") / 100
	interest_component = balance_outstanding * rate
	print(f"The interest component is: R{interest_component:.2f}")


def capital_component_from_formula():
	# capital component of a given payment, loan repaid in arrears
	print("\nCapital component of a given payment (formula).")
	loan_amount = get_positive_float_input("Enter the original loan amount: ")
	rate = get_positive_rate_input("Enter the effective interest rate per period (%): ") / 100
	payment_number = get_int_input("Enter the payment number: ")
	payment = get_positive_float_input("Enter the payment amount: ")
	
	if rate == 0:
		capital_component = payment
	else:
		capital_component = (payment - loan_amount * rate) * (1 + rate) ** (payment_number - 1)
	
	if capital_component < 0:
		capital_component = 0
	print(f"The capital component is: R{capital_component:.2f}")


def capital_component_from_interest():
	# capital component derived from the payment and interest component
	print("\nCapital component from payment and interest component.")
	payment = get_positive_float_input("Enter the payment amount: ")
	interest_component = get_non_negative_float_input("Enter the interest component: ")
	capital_component = payment - interest_component
	
	if capital_component < 0:
		capital_component = 0
	print(f"The capital component is: R{capital_component:.2f}")


def total_interest_from_payments():
	# total interest paid, derived from total payments made
	print("\nTotal interest from total payments made.")
	loan_amount = get_positive_float_input("Enter the original loan amount: ")
	payment = get_positive_float_input("Enter the payment amount: ")
	number_of_payments = get_positive_float_input("Enter the total number of payments: ")
	total_paid = payment * number_of_payments
	total_interest = total_paid - loan_amount
	
	if total_interest < 0:
		total_interest = 0
	print(f"The total interest is: R{total_interest:.2f}")


def total_interest_from_formula():
	# total interest paid, derived directly from the loan terms
	print("\nTotal interest from loan terms (formula).")
	loan_amount = get_positive_float_input("Enter the original loan amount: ")
	rate = get_positive_rate_input("Enter the effective interest rate per period (%): ") / 100
	payment = get_positive_float_input("Enter the payment amount: ")
	time = get_positive_float_input("Enter the term in years: ")
	periods = get_positive_float_input("Enter the number of compounding periods per year: ")
	number_of_payments = time * periods
	total_paid = payment * number_of_payments
	total_interest = total_paid - loan_amount
	
	if total_interest < 0:
		total_interest = 0
	print(f"The total interest is: R{total_interest:.2f}")


def capital_paid_in_year():
	# capital repaid during a given year, from outstanding balances
	print("\nCapital repaid during a given year.")
	year_number = get_int_input("Enter the year number (n): ")
	previous_balance = get_positive_float_input(f"Enter the balance outstanding at the start of year {year_number}: ")
	current_balance = get_non_negative_float_input(f"Enter the balance outstanding at the end of year {year_number}: ")
	capital_paid = previous_balance - current_balance
	
	if capital_paid < 0:
		capital_paid = 0
	print(f"The capital paid during year {year_number} is: R{capital_paid:.2f}")


def interest_paid_in_year():
	# interest paid during a given year, from payments and capital repaid
	print("\nInterest paid during a given year.")
	year_number = get_int_input("Enter the year number (n): ")
	previous_balance = get_positive_float_input(f"Enter the balance outstanding at the start of year {year_number}: ")
	current_balance = get_non_negative_float_input(f"Enter the balance outstanding at the end of year {year_number}: ")
	payment = get_positive_float_input("Enter the payment amount per period: ")
	periods = get_positive_float_input("Enter the number of compounding periods per year: ")
	capital_paid = previous_balance - current_balance
	
	if capital_paid < 0:
		capital_paid = 0
	
	total_paid_in_year = payment * periods
	interest_paid = total_paid_in_year - capital_paid
	
	if interest_paid < 0:
		interest_paid = 0
	print(f"The interest paid during year {year_number} is: R{interest_paid:.2f}")


def interest_and_capital_components():
	# display the interest and capital components sub-menu
	print("\nInterest and capital components selected.")
	print("1. Interest component (formula)")
	print("2. Interest component (from balance outstanding)")
	print("3. Capital component (formula)")
	print("4. Capital component (from interest component)")
	print("5. Total interest (from total payments)")
	print("6. Total interest (formula)")
	print("7. Capital paid during year n")
	print("8. Interest paid during year n")
	choice = get_int_input("Enter your choice (1 - 8): ")

	if choice == 1:
		interest_component_from_formula()
	elif choice == 2:
		interest_component_from_balance()
	elif choice == 3:
		capital_component_from_formula()
	elif choice == 4:
		capital_component_from_interest()
	elif choice == 5:
		total_interest_from_payments()
	elif choice == 6:
		total_interest_from_formula()
	elif choice == 7:
		capital_paid_in_year()
	elif choice == 8:
		interest_paid_in_year()
	else:
		print("Invalid choice. Please select a number between 1 and 8.")


def increasing_annuity_future_value():
	# future value of an annuity with geometrically increasing payments
	print("\nFuture value of an annuity with geometrically increasing payments.")
	print("FV = X[((1 + i)^np - (1 + j)^np) / (i - j)]")
	initial_amount = get_positive_float_input("Enter the first payment amount (X): ")
	rate = get_positive_rate_input("Enter the effective interest rate per period (%): ") / 100
	increase_rate = get_positive_rate_input("Enter the rate of increase per period (%): ") / 100
	time = get_positive_float_input("Enter the time in years: ")
	periods = get_positive_float_input("Enter the number of compounding periods per year: ")
	number_of_payments = periods * time
	
	if rate == increase_rate:
		future_value = initial_amount * number_of_payments * (1 + rate) ** (number_of_payments - 1)
	else:
		future_value = initial_amount * (((1 + rate) ** number_of_payments - (1 + increase_rate) ** number_of_payments) / (rate - increase_rate))
	print(f"The future value is: R{future_value:.2f}")


def increasing_annuity_present_value():
	# present value of an increasing annuity, derived from its future value
	print("\nPresent value from an accumulated value of an increasing annuity.")
	print("PV = AV(1 + i)^-np")
	accumulated_value = get_positive_float_input("Enter the accumulated value (AV): ")
	rate = get_positive_rate_input("Enter the effective interest rate per period (%): ") / 100
	time = get_positive_float_input("Enter the time in years: ")
	periods = get_positive_float_input("Enter the number of compounding periods per year: ")
	number_of_payments = periods * time
	present_value = accumulated_value * (1 + rate) ** -number_of_payments
	print(f"The present value is: R{present_value:.2f}")


def increasing_annuity_calculations():
	# display the increasing annuity calculations sub-menu
	print("\nIncreasing annuity calculations selected.")
	print("These calculations apply to payments that increase geometrically each period.")
	print("1. Future value")
	print("2. Present value (from accumulated value)")
	choice = get_int_input("Enter your choice (1 - 2): ")

	if choice == 1:
		increasing_annuity_future_value()
	elif choice == 2:
		increasing_annuity_present_value()
	else:
		print("Invalid choice. Please select 1 or 2.")


def simple_interest_calculations():
	# simple interest end amount calculation
	print("\nSimple interest selected.")
	initial_amount = get_positive_float_input("Enter the initial amount (PV): ")
	rate = get_positive_rate_input("Enter the simple interest rate (%): ") / 100
	time = get_non_negative_float_input("Enter the time in years: ")
	end_amount = initial_amount * (1 + rate * time)
	print(f"The end amount with simple interest is: R{end_amount:.2f}")


def effective_calculations():
	# display the effective annual interest sub-menu
	print("\nEffective interest calculations selected.")
	print("1. End amount (FV)")
	print("2. Interest rate")
	print("3. Number of years")
	print("4. Initial amount (PV)")
	print("5. Interest earned")
	choice = get_int_input("Enter your choice (1 - 5): ")

	if choice == 1:
		initial_amount = get_positive_float_input("Enter the initial amount (PV): ")
		rate = get_positive_rate_input("Enter the effective annual interest rate (%): ") / 100
		time = get_non_negative_float_input("Enter the time in years: ")
		end_amount = initial_amount * (1 + rate) ** time
		print(f"The end amount is: R{end_amount:.2f}")

	elif choice == 2:
		initial_amount = get_positive_float_input("Enter the initial amount (PV): ")
		end_amount = get_positive_float_input("Enter the end amount (FV): ")
		time = get_positive_float_input("Enter the time in years: ")
		rate = (end_amount / initial_amount) ** (1 / time) - 1
		print(f"The effective annual interest rate is: {rate * 100:.2f}%")

	elif choice == 3:
		initial_amount = get_positive_float_input("Enter the initial amount (PV): ")
		end_amount = get_positive_float_input("Enter the end amount (FV): ")
		rate = get_positive_rate_input("Enter the effective annual interest rate (%): ") / 100
		
		if rate == 0:
			print("Error: Cannot solve for time when interest rate is zero.")
			return
		
		time = math.log(end_amount / initial_amount) / math.log(1 + rate)
		print(f"The term is: {time:.2f} years")

	elif choice == 4:
		end_amount = get_positive_float_input("Enter the end amount (FV): ")
		rate = get_positive_rate_input("Enter the effective annual interest rate (%): ") / 100
		time = get_non_negative_float_input("Enter the time in years: ")
		initial_amount = end_amount / (1 + rate) ** time
		print(f"The initial amount is: R{initial_amount:.2f}")

	elif choice == 5:
		initial_amount = get_positive_float_input("Enter the initial amount (PV): ")
		rate = get_positive_rate_input("Enter the effective annual interest rate (%): ") / 100
		time = get_non_negative_float_input("Enter the time in years: ")
		interest_earned = initial_amount * (1 + rate) ** time - initial_amount
		print(f"The interest earned is: R{interest_earned:.2f}")

	else:
		print("Invalid choice. Please select a number between 1 and 5.")


def effective_periodic_calculations():
	# display the effective periodic interest sub-menu
	print("\nEffective periodic interest calculations selected.")
	print("1. End amount (FV)")
	print("2. Interest rate per period")
	print("3. Number of periods")
	print("4. Initial amount (PV)")
	print("5. Interest earned")
	choice = get_int_input("Enter your choice (1 - 5): ")

	if choice == 1:
		initial_amount = get_positive_float_input("Enter the initial amount (PV): ")
		rate = get_positive_rate_input("Enter the effective periodic interest rate (%): ") / 100
		number_of_periods = get_non_negative_float_input("Enter the number of periods: ")
		end_amount = initial_amount * (1 + rate) ** number_of_periods
		print(f"The end amount is: R{end_amount:.2f}")

	elif choice == 2:
		initial_amount = get_positive_float_input("Enter the initial amount (PV): ")
		end_amount = get_positive_float_input("Enter the end amount (FV): ")
		number_of_periods = get_positive_float_input("Enter the number of periods: ")
		rate = (end_amount / initial_amount) ** (1 / number_of_periods) - 1
		print(f"The effective periodic interest rate is: {rate * 100:.2f}%")

	elif choice == 3:
		initial_amount = get_positive_float_input("Enter the initial amount (PV): ")
		end_amount = get_positive_float_input("Enter the end amount (FV): ")
		rate = get_positive_rate_input("Enter the effective periodic interest rate (%): ") / 100
		
		if rate == 0:
			print("Error: Cannot solve for number of periods when interest rate is zero.")
			return
		
		number_of_periods = math.log(end_amount / initial_amount) / math.log(1 + rate)
		print(f"The number of periods is: {number_of_periods:.2f}")

	elif choice == 4:
		end_amount = get_positive_float_input("Enter the end amount (FV): ")
		rate = get_positive_rate_input("Enter the effective periodic interest rate (%): ") / 100
		number_of_periods = get_non_negative_float_input("Enter the number of periods: ")
		initial_amount = end_amount / (1 + rate) ** number_of_periods
		print(f"The initial amount is: R{initial_amount:.2f}")

	elif choice == 5:
		initial_amount = get_positive_float_input("Enter the initial amount (PV): ")
		rate = get_positive_rate_input("Enter the effective periodic interest rate (%): ") / 100
		number_of_periods = get_non_negative_float_input("Enter the number of periods: ")
		interest_earned = initial_amount * (1 + rate) ** number_of_periods - initial_amount
		print(f"The interest earned is: R{interest_earned:.2f}")

	else:
		print("Invalid choice. Please select a number between 1 and 5.")


def continuous_interest_calculations():
	# display the continuous interest (force of interest) sub-menu
	print("\nContinuous interest calculations selected.")
	print("1. End amount (FV)")
	print("2. Initial amount (PV)")
	print("3. Force of interest")
	print("4. Time in years")
	choice = get_int_input("Enter your choice (1 - 4): ")

	if choice == 1:
		initial_amount = get_positive_float_input("Enter the initial amount (PV): ")
		rate = get_positive_rate_input("Enter the force of interest (%): ") / 100
		time = get_non_negative_float_input("Enter the time in years: ")
		end_amount = initial_amount * math.exp(rate * time)
		print(f"The end amount is: R{end_amount:.2f}")

	elif choice == 2:
		end_amount = get_positive_float_input("Enter the end amount (FV): ")
		rate = get_positive_rate_input("Enter the force of interest (%): ") / 100
		time = get_non_negative_float_input("Enter the time in years: ")
		initial_amount = end_amount * math.exp(-rate * time)
		print(f"The initial amount is: R{initial_amount:.2f}")

	elif choice == 3:
		initial_amount = get_positive_float_input("Enter the initial amount (PV): ")
		end_amount = get_positive_float_input("Enter the end amount (FV): ")
		time = get_positive_float_input("Enter the time in years: ")
		rate = math.log(end_amount / initial_amount) / time
		print(f"The force of interest is: {rate * 100:.2f}%")

	elif choice == 4:
		initial_amount = get_positive_float_input("Enter the initial amount (PV): ")
		end_amount = get_positive_float_input("Enter the end amount (FV): ")
		rate = get_positive_rate_input("Enter the force of interest (%): ") / 100
		
		if rate == 0:
			print("Error: Cannot solve for time when force of interest is zero.")
			return
		
		time = math.log(end_amount / initial_amount) / rate
		print(f"The time is: {time:.2f} years")

	else:
		print("Invalid choice. Please select a number between 1 and 4.")


def view_graphs():
	# display a chosen graph using calculated data based on user input
	print("\nGraph menu:")
	print("1. Future value over time (compare arrears vs advance)")
	print("2. Present value over time (compare arrears vs advance)")
	print("3. Loan amortization schedule (interest vs capital)")
	choice = get_int_input("Enter your choice (1 - 3): ")

	if choice == 1:
		# compare future value of annuity in arrears vs advance
		payment = get_positive_float_input("Enter the periodic payment amount (X): ")
		rate = get_positive_rate_input("Enter the effective interest rate per period (%): ") / 100
		periods_per_year = get_positive_float_input("Enter the number of compounding periods per year: ")
		max_years = get_positive_float_input("Enter the maximum time in years to display: ")
		
		years = []
		fv_arrears = []
		fv_advance = []
		
		for year in range(0, int(max_years) + 1):
			years.append(year)
			n = year * periods_per_year
			
			if n > 0:
				if rate == 0:
					fv_arrears_value = payment * n
					fv_advance_value = payment * n
				else:
					fv_arrears_value = payment * (((1 + rate) ** n - 1) / rate)
					fv_advance_value = payment * (1 + rate) * (((1 + rate) ** n - 1) / rate)
				
				fv_arrears.append(fv_arrears_value)
				fv_advance.append(fv_advance_value)
			else:
				fv_arrears.append(0)
				fv_advance.append(0)
		
		plt.figure(figsize=(10, 6))
		plt.plot(years, fv_arrears, linestyle="-", marker="o", color="blue", label="Annuity in Arrears")
		plt.plot(years, fv_advance, linestyle="-", marker="s", color="red", label="Annuity in Advance")
		plt.title(f"Future Value Comparison (Payment = R{payment:.2f}, Rate = {rate*100:.2f}%)")
		plt.xlabel("Time (years)")
		plt.ylabel("Future Value (R)")
		plt.legend()
		plt.grid(True)
		plt.show()

	elif choice == 2:
		# compare present value of annuity in arrears vs advance
		payment = get_positive_float_input("Enter the periodic payment amount (X): ")
		rate = get_positive_rate_input("Enter the effective interest rate per period (%): ") / 100
		periods_per_year = get_positive_float_input("Enter the number of compounding periods per year: ")
		max_years = get_positive_float_input("Enter the maximum time in years to display: ")
		
		years = []
		pv_arrears = []
		pv_advance = []
		
		for year in range(0, int(max_years) + 1):
			years.append(year)
			n = year * periods_per_year
			
			if n > 0:
				if rate == 0:
					pv_arrears_value = payment * n
					pv_advance_value = payment * n
				else:
					pv_arrears_value = payment * ((1 - (1 + rate) ** -n) / rate)
					pv_advance_value = payment * (1 + rate) * ((1 - (1 + rate) ** -n) / rate)
				
				pv_arrears.append(pv_arrears_value)
				pv_advance.append(pv_advance_value)
			else:
				pv_arrears.append(0)
				pv_advance.append(0)
		
		plt.figure(figsize=(10, 6))
		plt.plot(years, pv_arrears, linestyle="-", marker="o", color="blue", label="Annuity in Arrears")
		plt.plot(years, pv_advance, linestyle="-", marker="s", color="red", label="Annuity in Advance")
		plt.title(f"Present Value Comparison (Payment = R{payment:.2f}, Rate = {rate*100:.2f}%)")
		plt.xlabel("Time (years)")
		plt.ylabel("Present Value (R)")
		plt.legend()
		plt.grid(True)
		plt.show()

	elif choice == 3:
		# loan amortization: interest vs capital components over time
		loan_amount = get_positive_float_input("Enter the original loan amount: ")
		rate = get_positive_rate_input("Enter the effective interest rate per period (%): ") / 100
		periods_per_year = get_positive_float_input("Enter the number of compounding periods per year: ")
		term_years = get_positive_float_input("Enter the loan term in years: ")
		
		n = periods_per_year * term_years
		
		if rate == 0:
			payment = loan_amount / n
		else:
			payment = loan_amount * rate / (1 - (1 + rate) ** -n)
		
		payment_numbers = []
		interest_components = []
		capital_components = []
		balance = loan_amount
		
		for i in range(1, int(n) + 1):
			payment_numbers.append(i)
			
			if rate == 0:
				interest = 0
				capital = payment
			else:
				interest = balance * rate
				capital = payment - interest
			
			interest_components.append(interest)
			capital_components.append(capital)
			balance -= capital
			
			if balance < 0:
				balance = 0
		
		plt.figure(figsize=(12, 6))
		x_axis = list(range(1, int(n) + 1))
		plt.bar(x_axis, interest_components, alpha=0.7, label="Interest Component", color="orange")
		plt.bar(x_axis, capital_components, bottom=interest_components, alpha=0.7, label="Capital Component", color="green")
		plt.title(f"Loan Amortization: Interest vs Capital (Loan = R{loan_amount:.2f}, Rate = {rate*100:.2f}%)")
		plt.xlabel("Payment Number")
		plt.ylabel("Amount (R)")
		plt.legend()
		plt.grid(True, alpha=0.3)
		plt.show()

	else:
		print("Invalid choice. Please select 1, 2, or 3.")


def main():
	# boolean flag controls whether the main program keeps running
	program_running = True
	while program_running is True:
		display_menu()
		choice = get_int_input("Enter your choice (1 - 10): ")

		if choice == 1:
			interest_rate_conversion()
		elif choice == 2:
			annuity_calculations()
		elif choice == 3:
			interest_and_capital_components()
		elif choice == 4:
			increasing_annuity_calculations()
		elif choice == 5:
			simple_interest_calculations()
		elif choice == 6:
			effective_calculations()
		elif choice == 7:
			effective_periodic_calculations()
		elif choice == 8:
			continuous_interest_calculations()
		elif choice == 9:
			view_graphs()
		elif choice == 10:
			# set the flag to False to end the main program loop
			program_running = False
		else:
			print("Invalid choice. Please select a number between 1 and 10.")

	print("Program terminated.")


if __name__ == "__main__":
	main()