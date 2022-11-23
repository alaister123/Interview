# Interview
Interview Question

Start: 11:00
End: 12:37

## P1.py -> Interview Question 1
## 我的思路
在HTML里面找到JSON代码（也可以通过F12抓包）
用BeautifulSoup 提取JSON代码
然后进行数据处理

def load_html(path: str) -> str:
  把html文件放入内存
  
def parse_html(html: str) -> BeautifulSoup:
   找到json位置并提取

def extract(soup: BeautifulSoup) -> dict:
  提取需要的信息并保存到dict
  保存到dict可以方面以后拓展

def to_csv(data: dict, title: str) -> None:
  保存到本地.csv文件

## P2.py -> Interview Question 2
## 我的思路


### 可能不止一个company比如
### Variopartner SICAV            <----------------- First
### 529900LPCSV88817QH61
### 1. TARENO GLOBAL WATER SOLUTIONS FUND
### LU2001709034
### ANOTHER COMPANY               <----------------- First
### 529900LPC349823094809834
### 1. TARENO GLOBAL WATER SOLUTIONS FUND
### LU1299721909
### LU1299722113

所以先把整个str 分成 单个company
然后单个parse

def parse(long_text: str) -> dict:
  parse每一个company
  用 "[数字]. " 进行分离
  前2行就是 name，lei
  后面每个list element 就是title 和is
 
 def parse_block(long_text: str) -> list:
  把每个company分离出来
  用 "1. "进行分离 因为每个name 和lei 下面肯定有 "1. XXXXXXXXX"
  分离后保存为list，每个element对应一个company
  
  
  
