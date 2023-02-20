from collections import Counter
import csv
from operator import itemgetter
import matplotlib.pyplot as plt
import tkinter as tk
import plotly.graph_objects as go
import pandas as pd
from PIL import ImageTk, Image

def btn10():
    global selectedVal
    selectedVal = 10
    clearButtons()
    btn10.configure(bg='gray')
    saveGraph()
def btn30():
    global selectedVal
    selectedVal = 30
    clearButtons()
    btn30.configure(bg='gray')
    saveGraph()
def btn50():
    global selectedVal
    selectedVal = 50
    clearButtons()
    btn50.configure(bg='gray')
    saveGraph()
def clearButtons():
    btn10.configure(bg='#f0f0f0')
    btn30.configure(bg='#f0f0f0')
    btn50.configure(bg='#f0f0f0')
def saveGraph():
    global selectedVal
    ignoreWords = ["the", "that", "an", "a", "for", "in", "be", "by", "or", "and", "with"]
    freq = None
    counter = {}
    with open ("TweetsElonMusk.csv", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for col in reader:
            for tweet in col:
                words = [x.lower() for x in tweet.split()] 
                for word in [s for s in words if not (s in ignoreWords)]:
                    if word not in counter:
                        counter[word] = 0
                    counter[word]+=1
    
    res = dict(sorted(counter.items(), key = itemgetter(1), reverse = True)[:selectedVal])
    names = list(res.keys())
    values = list(res.values())
    
    plt.barh(names, values)
    plt.title('store inventory')
    plt.ylabel('product')
    plt.xlabel('quantity')
    plt.gca().invert_yaxis()
    plt.savefig("fig.png")
    plt.clf()
    
    updateWindow()
    
def updateWindow():
    print("HERE")
    img = ImageTk.PhotoImage(Image.open("fig.png"))
    print(img)
    leftGraph.configure(image=img)




window = tk.Tk()
window.title("Tweets")
window.geometry("1400x500")
"""
    Buttons
"""
btn10 = tk.Button(window,width=10,height=2,text="10",command=btn10, bg="gray")
btn10.place(x=0, y=0)
btn30 = tk.Button(window,width=10,height=2,text="30",command=btn30, bg="#f0f0f0")
btn30.place(x=100, y=0)
btn50 = tk.Button(window,width=10,height=2,text="50",command=btn50, bg="#f0f0f0")
btn50.place(x=200, y=0)
"""
    Left Graph
"""
img = ImageTk.PhotoImage(Image.open("fig.png"))
leftGraph = tk.Label(window, image=img)
leftGraph.place(x=0, y=40)
"""
    Right Word Cloud
"""
rightCloud = tk.Label(window)
rightCloud.place(x=700, y=40)

window.mainloop()