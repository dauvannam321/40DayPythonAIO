# Basic python if-else

can = {0:'Canh', 1:'Tân', 2:'Nhâm', 3:'Quý', 4:'Giáp', 5:'Ất', 6:'Bính', 7:'Đinh', 8:'Mậu', 9:'Kỷ'}
chi = {0: 'Thân', 1:'Dậu', 2:'Tuất', 3:'Hợi',
       4:'Tý', 5:'Sửu', 6:'Dần', 7:'Mão',
       8:'Thìn', 9:'Tỵ', 10:'Ngọ', 11:'Mùi'}

def calculate_can_chi_calendar(year):
    result = can[year%10] + ' ' + chi[year%12]
    print(result)

calculate_can_chi_calendar(2024)
calculate_can_chi_calendar(2023)
calculate_can_chi_calendar(1997)
