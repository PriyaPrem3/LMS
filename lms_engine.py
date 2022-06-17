import master_data as md
import sys

# md.add10(100)

# print(md.g_master_data)

"""
### User Input Style #1
cust_name="abc"
cust_credit_score=247 
cust_requested_loan_amt=23400
"""

"""
### User Input Style #2
print(sys.argv)
cust_name=sys.argv[1]
cust_credit_score=int(sys.argv[2])
cust_requested_loan_amt=int(sys.argv[3])
"""
### User Input Style #3
cust_name=input("Enter Cust Name: ")
cust_credit_score=int(input("Enter Cust Credit Score: "))
cust_requested_loan_amt=int(input("Enter Loan Amount: "))

# Local Vars
l_input_status = "Success"

## Custom Exceptions
class invalid_cs_excp(Exception):pass
class invalid_loan_amt_excp(Exception):pass

max_cs = 0
max_cs_list =[]
min_cs = 0
min_cs_list =[]
max_loan_amt = 0
max_loan_list = []
min_loan_amt = 0
min_loan_list = []
for a in md.g_master_data:
    min_cs_list.append(a["cs_start"])
    max_cs_list.append(a["cs_end"])
    min_loan_list.append(a["loan_amt_start"])
    max_loan_list.append(a["loan_amt_end"])
min_cs = min(min_cs_list)
max_cs = max(max_cs_list)
max_loan_amt =max(max_loan_list)
min_loan_amt = min(min_loan_list)  


# Invalid Credit Score Exception
##
try:
    if cust_credit_score < min_cs or cust_credit_score > max_cs:
        raise invalid_cs_excp
except invalid_cs_excp:
    print("Credit Score is not valid")
    l_input_status = "Error"

# Invalid Loan Amount Exception    
##
try:
    if cust_requested_loan_amt< min_loan_amt or cust_requested_loan_amt > max_loan_amt:
        raise invalid_loan_amt_excp
except invalid_loan_amt_excp:
    print("Requested Loan Amount is not valid")
    l_input_status = "Error"


if l_input_status == "Success":  
    ## Core Business Logic
    for c1 in md.g_master_data:
        # print(c1)

        if cust_credit_score>=c1["cs_start"] and cust_credit_score<=c1["cs_end"] \
        and cust_requested_loan_amt>=c1["loan_amt_start"] and cust_requested_loan_amt<=c1["loan_amt_end"]:
            print("Approved")
            print(c1["interest"])
            print(c1["duration"])
    



# Loan engine
# {"cs_start":100, "cs_end":199, "loan_amt_start":10000, "loan_amt_end":19999, "interest":6,"duration":65}