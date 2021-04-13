'''
a = 3
data = "btn_buz_led"
D2 ={'a':"btn_led_on", 'b':"btn_buz_on", 'c':"btn_led_off", 
        'd':"btn_buz_off", 'e':"btn_bebebe", 'f':"btn_buz_led"}
if a > 0:
    while True:    
        if len(data) == 0:
            print("None")
            break
        if data == D2['a']:
            print("Turn on the light")
        elif data == D2['b']:
            print("Turn on the buzzer")
        elif data == D2['c']:
            print("Turn off the light")
        elif data == D2['d']:
            print("Turn off the buzzer")
        elif data == D2['e']:
            print("Click the BeBeBe button")
        elif data == D2['f']:
            print("Click the BeBeBe button")
        else:
            print('Unknown Command: {}'.format(data))            


letter = input()
D = {'s':"黑桃", 'h':"紅心", 'd':"方塊", 'c':"梅花"}
suit = D[letter]
print("suit = ", suit)
'''

labels = ['user1', 'user2', 'user3', 'user4', 'user5']
label = []
lbl=[]
print("labels1:", labels)
print("lbl1:", lbl[:len(lbl)+1])
#method2
label_dict = { 'a':"user1", 'b':"user2", 'c':"user3", 'd':"user4", 'e':"user5"}
for label in labels:
    if label == label_dict['a']:
        lbl.append(0)
    elif label == label_dict['b']:
         lbl.append(1)
    elif label == label_dict['c']:
        lbl.append(2)
    elif label == label_dict['d']:
        lbl.append(3)
    else:
        lbl.append(4)
labels = lbl
print("labels:", labels)
print("lbl:", lbl[:len(lbl)+1])
'''
#method1
for label in labels:
    if label.endswith('user1'):
       lbl.append(0)
    elif label.endswith('user2'):
        lbl.append(1)
    elif label.endswith('user3'):
        lbl.append(2)
    elif label.endswith('user4'):
        lbl.append(3)
    else:
        lbl.append(4)
labels = lbl
print("labels:", labels)
print("lbl:", lbl[:len(lbl)+1])'''