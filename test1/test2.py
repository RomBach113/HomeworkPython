x = int(input('введите первую координату: '))
y = int(input('ввдедите вторую координату:'))

def XY(x,y):
    if x>=0 and y>=0:
        print('первая четверть')
    elif x <= 0 and y>=0:
        print('вторая четверть')
    elif x<=0 and y<=0:
        print('третья четверть')
    elif x>=0 and y<=0:
        print('четвертая четверть')
      
print(XY(x,y))