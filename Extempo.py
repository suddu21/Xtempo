import random
random.seed()
participants = ["Sadanand Venkataraman","Arun Joseph","Hitanshee Pal","Sudhanshu Shekhar Jha","Ankit bhaskar","Soham Vaidya","Pavithra N","Sukanksha","Dinu K"]
topics= ["AI and the future of mankind","Rapid Urbanization","Impact of COVID – 19","What will you eradicate from India, if given a chance?","Hard work Vs. Smart work","Indian Education system","Life of Soldiers","Procrastination and its effects on everyday life","Goal – setting and planning","Health and Fitness"]
pleft=len(participants)
tleft=len(topics)
while (pleft>0):
	p=random.randrange(0,pleft)
	t=random.randrange(0,tleft)
	print("Current participant is ",participants[p]," and topic is ",topics[t])
	print()
	participants.pop(p)
	pleft-=1
	tleft-=1
import threading
def first():
	print("First timer complete")
timer=threading.Timer(3.0, first)
timer.start()
