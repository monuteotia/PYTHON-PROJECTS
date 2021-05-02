# creating a text translator using python
from tkinter.ttk import Combobox
from tkinter import *
from tkinter import messagebox
from textblob import TextBlob

root=Tk()
root.geometry('500x400')
root.title('TRANSLATOR')
root.resizable(False,False)
root.configure(bg='turquoise1')
lan_dict = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia': 'or', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}

#########Functions ####################
def tt(event=None):
    try:
        word3 = TextBlob(varname1.get())
        lan=word3.detect_language()
        lan_todict = languages.get() 
        lan_to = lan_dict[lan_todict]
        word3 = word3.translate(from_lang=lan,to=lan_to)
        label3.configure(text=word3)  
        varname2.set(word3)
    except:
        varname.set('try another keyword')
        
def main_exit():
    rr=messagebox.askyesnocancel('Notification','Are you want to exit',parent=root)
    if(rr==True):
        root.destroy()

##########Combo Box Languages ################
languages = StringVar()
font_box = Combobox(root,width=30,textvariable=languages,state='readonly')
font_box['values'] = [e for e in lan_dict.keys()]
font_box.current(37)
font_box.place(x=300,y=0)

#########Entry Box###############
varname1 = StringVar()
entry1 = Entry(root,width=30,textvariable=varname1,font=('times',15,'italic bold'))
entry1.place(x=150,y=40)

varname2 = StringVar()
entry2 = Entry(root,width=30,textvariable=varname2,font=('times',15,'italic bold'))
entry2.place(x=150,y=100)

###########LABELS############
label1 = Label(root,text='Enter Words :',font=('times',15,'italic bold'),bg='turquoise1')
label1.place(x=5,y=40)

label2 = Label(root,text='Translated :',font=('times',15,'italic bold'),bg='turquoise1')
label2.place(x=5,y=100)

label3 = Label(root,text='',font=('times',15,'italic bold'),bg='turquoise1')
label3.place(x=5,y=250)

##############BUTTONS###############
imgbt1 = PhotoImage(file='click.png')
imgbt2 = PhotoImage(file='close.png')

imgbt1 = imgbt1.subsample(9,9)
imgbt2 = imgbt2.subsample(5,5)

btn1 = Button(root,text='CLick',bd=10,bg='yellow',activeforeground='red',width=100,font=('times',15,'italic bold'),
              image=imgbt1,compound=RIGHT,command=tt)
btn1.place(x=70,y=170)

btn2 = Button(root,text='Exit',bd=10,bg='yellow',activeforeground='red',width=100,font=('times',15,'italic bold'),
              image=imgbt2,compound=RIGHT,command=main_exit)
btn2.place(x=280,y=170)

root.bind('<Return>',tt)
########button Binding##########

root.mainloop()