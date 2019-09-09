from dkb_robo import DKBRobo
from pprint import pprint
with DKBRobo('MLacher_89', 'Fred7') as dkb:
    print(dkb.last_login)
    pprint(dkb.account_dic)
    # get transaction
    LINK = dkb.account_dic[0]['transactions']
    TYPE = dkb.account_dic[0]['type']
    DATE_FROM = '14.03.2017'
    DATE_TO = '21.08.2017'
    TRANSACTION_LIST = dkb.get_transactions(LINK, TYPE, DATE_FROM, DATE_TO)
  
    print(TRANSACTION_LIST[6]['amount'])