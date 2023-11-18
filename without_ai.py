from get_email import *
from spreadsheet_write import *
lst = ['An amount of INR 2.00 has been DEBITED to your account XXX356 on 12/11/2023. Total Avail.bal INR 23,958.44. - Canara Bank']
lst = convert(lst)
amount = lst[4]
print(amount)

