'''
x = 2
def myFunc():
    x = 3
    print(x)    
myFunc()
print(x)
'''
score = 0
def add_score():
    global score
    score += 1
    print(score)    
add_score()
print(score)

#https://ithelp.ithome.com.tw/articles/10230680