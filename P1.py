from bs4 import BeautifulSoup
import json


def load_html(path: str) -> str: 
    data = ''
    with open(path, encoding ='utf-8') as file:
        data = file.read()
    return data

def parse_html(html: str) -> BeautifulSoup:
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def extract(soup: BeautifulSoup) -> dict:
    res = dict()
    data = json.loads(soup)
    for provinence in data['component'][0]['caseList']:
        area = provinence['area']
        res[area] = dict()
        res[area]['confirmedRelative'] = provinence['confirmedRelative']                                                    #新增
        res[area]['current'] = str(int(provinence['confirmed']) - int(provinence['crued']) - int(provinence['died']))       #现有 = 累计 - 治愈 - 死亡
        res[area]['confirmed'] = provinence['confirmed']                                                                    #累计
        res[area]['crued'] = provinence['crued']                                                                            #治愈
        res[area]['died'] = provinence['died']                                                                              #死亡


    # Bug Testing Only    
    # for i in res.keys():
    #     print(i,res[i])

    return res

def to_csv(data: dict, title: str) -> None:
    with open(title, 'w', encoding = 'utf-8-sig') as file:
        file.write('地区,新增,现有,累计,治愈,死亡\n')
        for key in data.keys():
            file.write(key)
            
            # Bug Test Only
            # print(key)
            
            for col in ['confirmedRelative','current','confirmed','crued','died']:
                file.write(',' + data[key][col])
            file.write('\n')


def main():
    html = load_html('page.html')
    soup = parse_html(html)
    data = soup.find(id = 'captain-config').contents
    final_data = extract(data[0])
    to_csv(final_data, 'result.csv')
    
if __name__ == "__main__":
    main()
