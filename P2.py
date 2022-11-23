long_text = '''
Variopartner SICAV
529900LPCSV88817QH61
1. TARENO GLOBAL WATER SOLUTIONS FUND
LU2001709034
LU2057889995
LU2001709547
2. TARENO FIXED INCOME FUND
LU1299722972
3. TARENO GLOBAL EQUITY FUND
LU1299721909
LU1299722113
LU1299722030
4. MIV GLOBAL MEDTECH FUND
LU0329630999
LU0329630130
ANOTHER COMPANY
529900LPC349823094809834
1. TARENO GLOBAL WATER SOLUTIONS FUND
LU1299721909
LU1299722113
2. TARENO GLOBAL WATER SOLUTIONS FUND
LU1299721909
LU1299722113
3. TARENO GLOBAL WATER SOLUTIONS FUND
LU1299721909
LU1299722113
100. TARENO GLOBAL WATER SOLUTIONS FUND
LU1299721909
LU1299722113
'''
import re

def parse(long_text: str) -> dict:
    long_text = long_text.strip()
    parsed = re.split("[0-9]+\. ", long_text)
    res = dict()
    res['name'], res['lei'] = parsed[0].split('\n')[0:2]
    res['sub_fund'] = []
    for line in parsed[1:]:
        line = line.strip().split('\n')
        res['sub_fund'].append({'title': line[0], 'isin': line[1:]})

    return (res)

#如果有多个公司在一个file里面 比如
'''
Variopartner SICAV
529900LPCSV88817QH61
1. TARENO GLOBAL WATER SOLUTIONS FUND
LU2001709034
ANOTHER COMPANY
529900LPC349823094809834
1. TARENO GLOBAL WATER SOLUTIONS FUND
LU1299721909
LU1299722113
'''
#这个function会分离每个公司
def parse_block(long_text: str) -> list:
    block = []
    long_text = long_text.strip()
    lines = long_text.split('\n')
    idx = []

    # find lines that start with 1.
    for i in range(len(lines)):
        if lines[i].startswith('1.'):
            idx.append(i-2)
    idx.append(len(lines))
    
    # find company block
    for i in range(1,len(idx)):
        block.append(lines[idx[i-1]: idx[i]])
    
    # connect each company together
    res = []
    for i in block:
        res.append('\n'.join(i))
    return res


if __name__ == '__main__':
    block = parse_block(long_text)
    final = []

    # parse every company indvidually
    for company in block:
        final.append(parse(company))
        
    #print result
    for js in final:
        print(js)
        print('\n')
