import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument('--type', type=str)
parser.add_argument('--principal', type=int)
parser.add_argument('--payment', type=int)
parser.add_argument('--periods', type=int)
parser.add_argument('--interest', type=float)

args = parser.parse_args()
args_dict = {'type': args.type, 'principal': args.principal, 
			 'payment': args.payment, 'periods': args.periods, 'interest': args.interest}

# args check

for i in args_dict.values():
    if type(i) in [int, float] and i < 0:
        print('Incorrect parameters')
        exit(0)

if args.type not in ['annuity', 'diff'] or len(args_dict.values()) < 4:
	print('Incorrect parameters')
	exit(0)
elif args.type == 'diff' and args.payment != None:
	print('Incorrect parameters')
	exit(0)
elif args_dict['interest'] == None:
	print('Incorrect parameters')
	exit(0)

interest_rate = args_dict['interest']/(12*100) #month interest
count = 0
if args_dict['type'] == 'diff':  # differentiated payment
    for i in range(1,args_dict['periods']+1):
        diff_payment = math.ceil((args_dict['principal'] / args_dict['periods'] + interest_rate * (args_dict['principal'] - (args_dict['principal'] * (i-1) / args_dict['periods']))))
        count += diff_payment
        print('Month {}: payment is {}'.format(i, diff_payment ))
    print('')
    print('Overpayment = {}'.format(count - args_dict['principal']))   

else:  # annuity payments
    if args_dict['payment'] == None:  #payment calculation
    	anuity_payment = math.ceil(args_dict['principal']*(((interest_rate*(1+interest_rate)**args_dict['periods']))
    	/((1+interest_rate)**args_dict['periods'] -1)))
    	overpayment = args_dict['periods']*anuity_payment - args_dict['principal']
    	print('Your annuity payment = {}!'.format(anuity_payment))
		# print()
    	print('Overpayment =', int(overpayment))
    elif args_dict['principal'] == None:  #principal calculation
        loan_principal = int(args_dict['payment']/(((interest_rate*(1+interest_rate)**args_dict['periods']))
                                     /((1+interest_rate)**args_dict['periods'] -1)))
        print('Your loan principal = {}!'.format(loan_principal))
        print("Overpayment = {}".format(args_dict['payment']*args_dict['periods']-loan_principal))
    elif args_dict['periods'] == None:
        temp_b = interest_rate+1
        temp_v = args_dict['payment']/(args_dict['payment']-(interest_rate*args_dict['principal']))
        number_of_periods = math.ceil(math.log(temp_v, temp_b))
        print('It will take', '{} months'.format(number_of_periods) if number_of_periods < 12 
            else '{} years'.format(int(number_of_periods // 12)) if not number_of_periods % 12 
                else '{} years and {} months'.format((int(number_of_periods // 12)),(math.ceil(number_of_periods % 12))),
            'to repay this credit!')
        print('Overpayment =', number_of_periods*args_dict['payment'] - args_dict['principal'])



