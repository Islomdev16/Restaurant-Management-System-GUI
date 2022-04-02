from __future__ import print_function
from telesign.messaging import MessagingClient
from tkinter import *
from tkinter import filedialog, messagebox
import random
import time
import requests

# Functions Section
def send():
    def send_msg():
        customer_id = "2EECC704-8AE6-424D-B23F-C973BD5D1EA6"
        api_key = "RetEJ2ZOkkZ1jBX5b5MP5SbZYO5o5uX5DASoXcmNdMkqzZh55MPtta26IBbcGLSKi5YNuPC4SuD4hFJ50XNTOg=="

        phone_number = "998902260416"
        message = textarea.get(1.0, END)
        message_type = "ARN"
        messaging = MessagingClient(customer_id, api_key)
        response = messaging.message(phone_number, message, message_type)

        # url = 'https://portal.telesign.com/portal/account-settings'
        # params = {
        #     'authorization':auth,
        #     "message":message,
        #     "number":number,
        #     "sender-id":"FSTSMS",
        #     "route": "p",
        #     "language":"english"
        # }
        # response = requests.get(url, params=params)
        # dic = response.json()
        # result = dic.get('return')
        if response != True:
            messagebox.showinfo("Send Successfully", "Message sent successfully")
        else:
            messagebox.showerror("Error", "Something went wrong")


    root2 = Toplevel()
    root2.title("📤 Send Bill")
    root2.config(bg="red4")
    root2.geometry("485x620+50+50")

    logoImage = PhotoImage(file="sender.png")
    label = Label(root2, image=logoImage, bg="red4")
    label.pack(pady=5)

    numberLabel = Label(root2, text="Mobile Number", font=("arial", 18, "bold underline"), bg="red4", fg="white")
    numberLabel.pack(pady=5)

    numberfield = Entry(root2, font=("helvetica", 22, "bold"), bd=3, width=24)
    numberfield.pack(pady=5)

    billLabel = Label(root2, text="Bill Details", font=("arial", 18, "bold underline"), bg="red4", fg="white")
    billLabel.pack(pady=5)

    textarea = Text(root2, font=("arial", 12, "bold"), bd=3, width=42, height=14)
    textarea.pack(pady=5)
    textarea.insert(END, "Receipt Ref:\t\t➖" + billnumber + "\t\t➖" + date + "\n\n")

    textarea.insert(END, f'Cost of Food\t\t\t➖{priceofFood} So\'m\n')
    textarea.insert(END, f"Cost of Drinks\t\t\t➖{priceofDrinks} So'm\n")
    textarea.insert(END, f"Cost of Cakes\t\t\t➖{priceofCakes} So'm\n")

    textarea.insert(END, f"Sub Total\t\t\t➖{subtotalofItems} So'm \n")
    textarea.insert(END, f"Service Tax\t\t\t➖{25} So'm\n")
    textarea.insert(END, f"# Total Cost\t\t\t➖{subtotalofItems + 50} So'm\n")

    sendbutton = Button(root2, text="SEND", font=("arial", 19, "bold"), bg="white", fg="red4", bd=7, relief=GROOVE, command=send_msg)
    sendbutton.pack(pady=5)

    root2.mainloop()

def reset():
    textReceipt.delete(1.0, END)

    e_palov.set("0")
    e_shashlik.set("0")
    e_lagman.set("0")
    e_norin.set("0")
    e_mastava.set("0")
    e_manti.set("0")
    e_chuchvara.set("0")
    e_bifshteks.set("0")
    e_kabob.set("0")
    e_somsa.set("0")

    e_nestle.set("0")
    e_fanta.set("0")
    e_dinay.set("0")
    e_cola.set("0")
    e_coffee.set("0")
    e_redbull.set("0")
    e_chortoq.set("0")
    e_pepsi.set("0")
    e_dena.set("0")
    e_bliss.set("0")

    e_napoleon.set("0")
    e_chouxcake.set("0")
    e_absheron.set("0")
    e_cheesecake.set("0")
    e_madonna.set("0")
    e_bostoncreamcake.set("0")
    e_honeynut.set("0")
    e_blackforest.set("0")
    e_anthill.set("0")
    e_praga.set("0")

    textpalov.config(state=DISABLED)
    textshashlik.config(state=DISABLED)
    textlagman.config(state=DISABLED)
    textnorin.config(state=DISABLED)
    textmastava.config(state=DISABLED)
    textmanti.config(state=DISABLED)
    textchuchvara.config(state=DISABLED)
    textbifshteks.config(state=DISABLED)
    textkabob.config(state=DISABLED)
    textsomsa.config(state=DISABLED)

    textnestle.config(state=DISABLED)
    textfanta.config(state=DISABLED)
    textdinay.config(state=DISABLED)
    textcola.config(state=DISABLED)
    textcoffee.config(state=DISABLED)
    textredbull.config(state=DISABLED)
    textchortoq.config(state=DISABLED)
    textpepsi.config(state=DISABLED)
    textdena.config(state=DISABLED)
    textbliss.config(state=DISABLED)

    textnapoleon.config(state=DISABLED)
    textchouxcake.config(state=DISABLED)
    textabsheron.config(state=DISABLED)
    textcheesecake.config(state=DISABLED)
    textmadonna.config(state=DISABLED)
    textbostoncreamcake.config(state=DISABLED)
    texthoneynut.config(state=DISABLED)
    textblackforest.config(state=DISABLED)
    textanthill.config(state=DISABLED)
    textpraga.config(state=DISABLED)

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)
    var28.set(0)
    var29.set(0)
    var30.set(0)

    costoffoodvar.set('')
    costofdrinksvar.set('')
    costofcakesvar.set('')
    subtotalvar.set('')
    servicetaxvar.set('')
    totalcostvar.set('')


def save():
    if textReceipt.get(1.0, END) == '\n':
        messagebox.showerror("Error", "Nothing here to save !")
    else:
        url = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
        if not url != None:
            pass
        else:
            bill_data = textReceipt.get(1.0, END)
            url.write(bill_data)
            url.close()
            messagebox.showinfo("Information", "Your bill is successfully saved")

def receipt():
    global billnumber, date
    if costoffoodvar.get() != '' or costofcakesvar.get() != '' or costofdrinksvar.get() != '':
        textReceipt.delete(1.0, END)
        x = random.randint(100, 10000)
        billnumber = 'BILL' + str(x)
        date = time.strftime('%d/%m/%Y')
        textReceipt.insert(END, 'Receipt REF:\t\t' + billnumber + '\t\t' + date + '\n')
        textReceipt.insert(END, "***" * 21 + "\n")
        textReceipt.insert(END, "Items:\t\t Cost of Items(So'm)\n")
        textReceipt.insert(END, "***" * 21 + "\n")
        if e_palov.get() != '0':
            textReceipt.insert(END, f'Palov\t\t\t{int(e_palov.get())*10}\n\n')
        if e_shashlik.get() != '0':
            textReceipt.insert(END, f'Shashlik\t\t\t{int(e_shashlik.get())*60}\n\n')
        if e_lagman.get() != '0':
            textReceipt.insert(END, f'Lagman\t\t\t{int(e_lagman.get())*100}\n\n')
        if e_norin.get() != '0':
            textReceipt.insert(END, f'Norin\t\t\t{int(e_norin.get())*50}\n\n')
        if e_mastava.get() != '0':
            textReceipt.insert(END, f'Mastava\t\t\t{int(e_mastava.get())*40}\n\n')
        if e_manti.get() != '0':
            textReceipt.insert(END, f'Manti\t\t\t{int(e_manti.get())*30}\n\n')
        if e_chuchvara.get() != '0':
            textReceipt.insert(END, f'Chuchvara\t\t\t{int(e_chuchvara.get())*120}\n\n')
        if e_bifshteks.get() != '0':
            textReceipt.insert(END, f'Bifshteks\t\t\t{int(e_bifshteks.get())*100}\n\n')
        if e_kabob.get() != '0':
            textReceipt.insert(END, f'Kabob\t\t\t{int(e_kabob.get())*120}\n\n')
        if e_somsa.get() != '0':
            textReceipt.insert(END, f'Somsa\t\t\t{int(e_somsa.get())*50}\n\n')

        if e_nestle.get() != '0':
            textReceipt.insert(END, f'Nestle\t\t\t{int(e_nestle.get())*40}\n\n')
        if e_fanta.get() != '0':
            textReceipt.insert(END, f'Fanta\t\t\t{int(e_fanta.get())*80}\n\n')
        if e_dinay.get() != '0':
            textReceipt.insert(END, f'Dinay\t\t\t{int(e_dinay.get())*30}\n\n')
        if e_cola.get() != '0':
            textReceipt.insert(END, f'Cola\t\t\t{int(e_cola.get())*45}\n\n')
        if e_coffee.get() != '0':
            textReceipt.insert(END, f'Coffee\t\t\t{int(e_coffee.get())*60}\n\n')
        if e_redbull.get() != '0':
            textReceipt.insert(END, f'Redbull\t\t\t{int(e_redbull.get())*20}\n\n')
        if e_chortoq.get() != '0':
            textReceipt.insert(END, f'Chortoq\t\t\t{int(e_chortoq.get())*50}\n\n')
        if e_pepsi.get() != '0':
            textReceipt.insert(END, f'Pepsi\t\t\t{int(e_pepsi.get())*80}\n\n')
        if e_dena.get() != '0':
            textReceipt.insert(END, f'Dena\t\t\t{int(e_dena.get())*400}\n\n')
        if e_bliss.get() != '0':
            textReceipt.insert(END, f'Bliss\t\t\t{int(e_bliss.get())*300}\n\    n')

        if e_napoleon.get() != '0':
            textReceipt.insert(END, f'Napoleon\t\t\t{int(e_napoleon.get())*150}\n\n')
        if e_chouxcake.get() != '0':
            textReceipt.insert(END, f'Chouxcake\t\t\t{int(e_chouxcake.get())*124}\n\n')
        if e_absheron.get() != '0':
            textReceipt.insert(END, f'Absheron\t\t\t{int(e_absheron.get())*174}\n\n')
        if e_cheesecake.get() != '0':
            textReceipt.insert(END, f'Cheesecake\t\t\t{int(e_cheesecake.get())*200}\n\n')
        if e_madonna.get() != '0':
            textReceipt.insert(END, f'Madonna\t\t\t{int(e_madonna.get())*129}\n\n')
        if e_bostoncreamcake.get() != '0':
            textReceipt.insert(END, f'BostonCreamcake\t\t\t{int(e_bostoncreamcake.get())*139}\n\n')
        if e_honeynut.get() != '0':
            textReceipt.insert(END, f'Honeynut\t\t\t{int(e_honeynut.get())*96}\n\n')
        if e_blackforest.get() != '0':
            textReceipt.insert(END, f'Blackforest\t\t\t{int(e_blackforest.get())*104}\n\n')
        if e_anthill.get() != '0':
            textReceipt.insert(END, f'Anthill\t\t\t{int(e_anthill.get())*129}\n\n')
        if e_praga.get() != '0':
            textReceipt.insert(END, f'Praga\t\t\t{int(e_praga.get())*113}\n\n')

        textReceipt.insert(END, "***"*21 + "\n")
        textReceipt.insert(END, f"Cost of Food\t\t\t{priceofFood} So'm\n\n")
        textReceipt.insert(END, f"Cost of Drinks\t\t\t{priceofDrinks} So'm\n\n")
        textReceipt.insert(END, f"Cost of Cakes\t\t\t{priceofCakes} So'm\n\n")

        textReceipt.insert(END, f"Sub Total\t\t\t{subtotalofItems} So'm \n\n")
        textReceipt.insert(END, f"Service Tax\t\t\t{25} So'm\n\n")
        textReceipt.insert(END, f"# Total Cost\t\t\t{subtotalofItems+50} So'm\n\n")
        textReceipt.insert(END, "***"*21 + "\n")
    
    else:
        messagebox.showerror("Error", "No Item is selected")


def totalcost():
    global priceofFood, priceofDrinks, priceofCakes, subtotalofItems
    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or var6.get() != 0 or var7.get() != 0 or \
         var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or var11.get() != 0 or var12.get() != 0 or var13.get() != 0 or var14.get() != 0 or \
         var15.get() != 0 or var16.get() != 0 or var17.get() != 0 or var18.get() != 0  or var19.get() != 0  or var20.get() != 0 or var21.get() != 0 or \
         var22.get() != 0 or var23.get() != 0 or var24.get() != 0 or var25.get() != 0 or var26.get() != 0 or var27.get() != 0 or var28.get() != 0 or var29.get() != 0 or var30.get() != 0:

        item1 = int(e_palov.get())
        item2 = int(e_shashlik.get())
        item3 = int(e_lagman.get())
        item4 = int(e_norin.get())
        item5 = int(e_mastava.get())
        item6 = int(e_manti.get())
        item7 = int(e_chuchvara.get())
        item8 = int(e_bifshteks.get())
        item9 = int(e_kabob.get())
        item10 = int(e_somsa.get())

        item11 = int(e_nestle.get())
        item12 = int(e_fanta.get())
        item13 = int(e_dinay.get())
        item14 = int(e_cola.get())
        item15 = int(e_coffee.get())
        item16 = int(e_redbull.get())
        item17 = int(e_chortoq.get())
        item18 = int(e_pepsi.get())
        item19 = int(e_dena.get())
        item20 = int(e_bliss.get())

        item21 = int(e_napoleon.get())
        item22 = int(e_chouxcake.get())
        item23 = int(e_absheron.get())
        item24 = int(e_cheesecake.get())
        item25 = int(e_madonna.get())
        item26 = int(e_bostoncreamcake.get())
        item27 = int(e_honeynut.get())
        item28 = int(e_blackforest.get())
        item29 = int(e_anthill.get())
        item30 = int(e_praga.get())

        priceofFood = (item1*10)+(item2*60)+(item3*100)+(item4*50)+(item5*40)+(item6*30)+(item7*120)+(item8*100)+(item9*120)+(item10*50)

        priceofDrinks = (item11*40)+(item12*80)+(item13*30)+(item14*45)+(item15*60)+(item16*20)+(item17*50)+(item18*80)+(item19*400)+(item20*300)

        priceofCakes = (item21*150)+(item22*124)+(item23*174)+(item24*200)+(item25*129)+(item26*139)+(item27*96)+(item28*104)+(item29*129)+(item30*113)

        costoffoodvar.set(str(priceofFood)+ ".000 So'm")
        costofdrinksvar.set(str(priceofDrinks)+ ".000 So'm")
        costofcakesvar.set(str(priceofCakes)+ ".000 So' m")

        subtotalofItems = priceofFood+priceofDrinks+priceofCakes
        subtotalvar.set(str(subtotalofItems) + ".000 So'm")
        servicetaxvar.set("25.000 So'm")
        totalcost = subtotalofItems+25
        totalcostvar.set(str(totalcost) + ".000 So'm")

    else:
        messagebox.showerror("Error", "No Item is selected !")


def palov():
    if var1.get() == 1:
        textpalov.config(state=NORMAL)
        textpalov.delete(0, END)
        textpalov.focus()
    else:
        textpalov.config(state=DISABLED)
        e_palov.set('0')

def shashlik():
    if var2.get() == 1:
        textshashlik.config(state=NORMAL)
        textshashlik.delete(0, END)
        textshashlik.focus()
    else:
        textshashlik.config(state=DISABLED)
        e_shashlik.set('0')

def lagman():
    if var3.get() == 1:
        textlagman.config(state=NORMAL)
        textlagman.delete(0, END)
        textlagman.focus()
    else:
        textlagman.config(state=DISABLED)
        e_lagman.set('0')

def norin():
    if var4.get() == 1:
        textnorin.config(state=NORMAL)
        textnorin.delete(0, END)
        textnorin.focus()
    else:
        textnorin.config(state=DISABLED)
        e_norin.set('0')

def mastava():
    if var5.get() == 1:
        textmastava.config(state=NORMAL)
        textmastava.delete(0, END)
        textmastava.focus()
    else:
        textmastava.config(state=DISABLED)
        e_mastava.set('0')

def manti():
    if var6.get() == 1:
        textmanti.config(state=NORMAL)
        textmanti.delete(0, END)
        textmanti.focus()
    else:
        textmanti.config(state=DISABLED)
        e_manti.set('0')

def chuchvara():
    if var7.get() == 1:
        textchuchvara.config(state=NORMAL)
        textchuchvara.delete(0, END)
        textchuchvara.focus()
    else:
        textchuchvara.config(state=DISABLED)
        e_chuchvara.set('0')

def bifshteks():
    if var8.get() == 1:
        textbifshteks.config(state=NORMAL)
        textbifshteks.delete(0, END)
        textbifshteks.focus()
    else:
        textbifshteks.config(state=DISABLED)
        e_bifshteks.set('0')

def kabob():
    if var9.get() == 1:
        textkabob.config(state=NORMAL)
        textkabob.delete(0, END)
        textkabob.focus()
    else:
        textkabob.config(state=DISABLED)
        e_kabob.set('0')
   
def somsa():
    if var10.get() == 1:
        textsomsa.config(state=NORMAL)
        textsomsa.delete(0, END)
        textsomsa.focus()
    else:
        textsomsa.config(state=DISABLED)
        e_somsa.set('0')


# Functions of Drink Section
def nestle():
    if var11.get() == 1:
        textnestle.config(state=NORMAL)
        textnestle.delete(0, END)
        textnestle.focus()
    else:
        textnestle.config(state=DISABLED)
        e_nestle.set('0')

def fanta():
    if var12.get() == 1:
        textfanta.config(state=NORMAL)
        textfanta.delete(0, END)
        textfanta.focus()
    else:
        textfanta.config(state=DISABLED)
        e_fanta.set('0')

def dinay():
    if var13.get() == 1:
        textdinay.config(state=NORMAL)
        textdinay.delete(0, END)
        textdinay.focus()
    else:
        textdinay.config(state=DISABLED)
        e_dinay.set('0')

def cola():
    if var14.get() == 1:
        textcola.config(state=NORMAL)
        textcola.delete(0, END)
        textcola.focus()
    else:
        textcola.config(state=DISABLED)
        e_cola.set('0')

def coffee():
    if var15.get() == 1:
        textcoffee.config(state=NORMAL)
        textcoffee.delete(0, END)
        textcoffee.focus()
    else:
        textcoffee.config(state=DISABLED)
        e_coffee.set('0')

def redbull():
    if var16.get() == 1:
        textredbull.config(state=NORMAL)
        textredbull.delete(0, END)
        textredbull.focus()
    else:
        textredbull.config(state=DISABLED)
        e_redbull.set('0')

def chortoq():
    if var17.get() == 1:
        textchortoq.config(state=NORMAL)
        textchortoq.delete(0, END)
        textchortoq.focus()
    else:
        textchortoq.config(state=DISABLED)
        e_chortoq.set('0')

def pepsi():
    if var18.get() == 1:
        textpepsi.config(state=NORMAL)
        textpepsi.delete(0, END)
        textpepsi.focus()
    else:
        textpepsi.config(state=DISABLED)
        e_pepsi.set('0')

def dena():
    if var19.get() == 1:
        textdena.config(state=NORMAL)
        textdena.delete(0, END)
        textdena.focus()
    else:
        textdena.config(state=DISABLED)
        e_dena.set('0')
   
def bliss():
    if var20.get() == 1:
        textbliss.config(state=NORMAL)
        textbliss.delete(0, END)
        textbliss.focus()
    else:
        textbliss.config(state=DISABLED)
        e_bliss.set('0')

# Functions of Cakes Section
def napoleon():
    if var21.get() == 1:
        textnapoleon.config(state=NORMAL)
        textnapoleon.delete(0, END)
        textnapoleon.focus()
    else:
        textnapoleon.config(state=DISABLED)
        e_napoleon.set('0')

def chouxcake():
    if var22.get() == 1:
        textchouxcake.config(state=NORMAL)
        textchouxcake.delete(0, END)
        textchouxcake.focus()
    else:
        textchouxcake.config(state=DISABLED)
        e_chouxcake.set('0')

def absheron():
    if var23.get() == 1:
        textabsheron.config(state=NORMAL)
        textabsheron.delete(0, END)
        textabsheron.focus()
    else:
        textabsheron.config(state=DISABLED)
        e_absheron.set('0')

def cheesecake():
    if var24.get() == 1:
        textcheesecake.config(state=NORMAL)
        textcheesecake.delete(0, END)
        textcheesecake.focus()
    else:
        textcheesecake.config(state=DISABLED)
        e_cheesecake.set('0')

def madonna():
    if var25.get() == 1:
        textmadonna.config(state=NORMAL)
        textmadonna.delete(0, END)
        textmadonna.focus()
    else:
        textmadonna.config(state=DISABLED)
        e_madonna.set('0')

def bostoncreamcake():
    if var26.get() == 1:
        textbostoncreamcake.config(state=NORMAL)
        textbostoncreamcake.delete(0, END)
        textbostoncreamcake.focus()
    else:
        textbostoncreamcake.config(state=DISABLED)
        e_bostoncreamcake.set('0')

def honeynut():
    if var27.get() == 1:
        texthoneynut.config(state=NORMAL)
        texthoneynut.delete(0, END)
        texthoneynut.focus()
    else:
        texthoneynut.config(state=DISABLED)
        e_honeynut.set('0')

def blackforest():
    if var28.get() == 1:
        textblackforest.config(state=NORMAL)
        textblackforest.delete(0, END)
        textblackforest.focus()
    else:
        textblackforest.config(state=DISABLED)
        e_blackforest.set('0')

def anthill():
    if var29.get() == 1:
        textanthill.config(state=NORMAL)
        textanthill.delete(0, END)
        textanthill.focus()
    else:
        textanthill.config(state=DISABLED)
        e_anthill.set('0')
   
def praga():
    if var30.get() == 1:
        textpraga.config(state=NORMAL)
        textpraga.delete(0, END)
        textpraga.focus()
    else:
        textpraga.config(state=DISABLED)
        e_praga.set('0')

root = Tk()
root.geometry("1337x750+0+0")
root.resizable(True, True)
root.title("Restaurant Management System")
root.config(bg="firebrick4")

topFrame = Frame(root, bd=10, relief=RIDGE, bg="firebrick4")
topFrame.pack(side=TOP)

labelTitle = Label(topFrame, text="Restaurant Management System", font=("arial", 30, "bold"), fg="yellow", bd=9, bg="red4", width=59)
labelTitle.grid(row=0, column=0)

# Frames Section
menuFrame = Frame(root, bd=10, relief=RIDGE, bg="firebrick4")
menuFrame.pack(side=LEFT)

costFrame = Frame(menuFrame, bd=4, relief=RIDGE, bg="firebrick4", pady=10)
costFrame.pack(side=BOTTOM)

foodFrame = LabelFrame(menuFrame, text="Food", font=("arial", 20, "bold"), bd=10, relief=RIDGE, fg="red4")
foodFrame.pack(side=LEFT)

drinksFrame = LabelFrame(menuFrame, text="Drinks", font=("arial", 20, "bold"), bd=10, relief=RIDGE, fg="red4")
drinksFrame.pack(side=LEFT)

cakesFrame = LabelFrame(menuFrame, text="Cakes", font=("arial", 20, "bold"), bd=10, relief=RIDGE, fg="red4")
cakesFrame.pack(side=LEFT)

rightFrame = Frame(root, bd=15, relief=RIDGE, bg="red4")
rightFrame.pack(side=RIGHT)

calculatorFrame = Frame(rightFrame, bd=1, relief=RIDGE, bg="red4")
calculatorFrame.pack()

recieptFrame = Frame(rightFrame, bd=4, relief=RIDGE, bg="red4")
recieptFrame.pack()

buttonFrame = Frame(rightFrame, bd=3, relief=RIDGE, bg="red4")
buttonFrame.pack()

# Variable Section
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()
var24 = IntVar()
var25 = IntVar()
var26 = IntVar()
var27 = IntVar()
var28 = IntVar()
var29 = IntVar()
var30 = IntVar()


e_palov = StringVar()
e_shashlik = StringVar()
e_lagman = StringVar()
e_norin = StringVar()
e_mastava = StringVar()
e_manti = StringVar()
e_chuchvara = StringVar()
e_bifshteks = StringVar()
e_kabob = StringVar()
e_somsa = StringVar()

e_nestle = StringVar()
e_fanta = StringVar()
e_dinay = StringVar()
e_cola = StringVar()
e_coffee = StringVar()
e_redbull = StringVar()
e_chortoq = StringVar()
e_pepsi = StringVar()
e_dena = StringVar()
e_bliss = StringVar()

e_napoleon = StringVar()
e_chouxcake = StringVar()
e_absheron = StringVar()
e_cheesecake = StringVar()
e_madonna = StringVar()
e_bostoncreamcake = StringVar()
e_honeynut = StringVar()
e_blackforest = StringVar()
e_anthill = StringVar()
e_praga = StringVar()

costoffoodvar = StringVar()
costofdrinksvar = StringVar()
costofcakesvar = StringVar()
subtotalvar = StringVar()
servicetaxvar = StringVar()
totalcostvar = StringVar()


e_palov.set("0")
e_shashlik.set("0")
e_lagman.set("0")
e_norin.set("0")
e_mastava.set("0")
e_manti.set("0")
e_chuchvara.set("0")
e_bifshteks.set("0")
e_kabob.set("0")
e_somsa.set("0")

e_nestle.set("0")
e_fanta.set("0")
e_dinay.set("0")
e_cola.set("0")
e_coffee.set("0")
e_redbull.set("0")
e_chortoq.set("0")
e_pepsi.set("0")
e_dena.set("0")
e_bliss.set("0")

e_napoleon.set("0")
e_chouxcake.set("0")
e_absheron.set("0")
e_cheesecake.set("0")
e_madonna.set("0")
e_bostoncreamcake.set("0")
e_honeynut.set("0")
e_blackforest.set("0")
e_anthill.set("0")
e_praga.set("0")

# Food Label Section
palov = Checkbutton(foodFrame, text="Palov", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var1, command=palov)
palov.grid(row=0, column=0, sticky=W)

shashlik = Checkbutton(foodFrame, text="Shashlik", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var2, command=shashlik)
shashlik.grid(row=1, column=0, sticky=W)

lagman = Checkbutton(foodFrame, text="Lagman", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var3, command=lagman)
lagman.grid(row=2, column=0, sticky=W)

norin = Checkbutton(foodFrame, text="Norin", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var4, command=norin)
norin.grid(row=3, column=0, sticky=W)

mastava = Checkbutton(foodFrame, text="Mastava", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var5, command=mastava)
mastava.grid(row=4, column=0, sticky=W)

manti = Checkbutton(foodFrame, text="Manti", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var6, command=manti)
manti.grid(row=5, column=0, sticky=W)

chuchvara = Checkbutton(foodFrame, text="Chuchvara", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var7, command=chuchvara)
chuchvara.grid(row=6, column=0, sticky=W)

bifshteks = Checkbutton(foodFrame, text="Bifshteks", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var8, command=bifshteks)
bifshteks.grid(row=7, column=0, sticky=W)

kabob = Checkbutton(foodFrame, text="Kabob", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var9, command=kabob)
kabob.grid(row=8, column=0, sticky=W)

somsa = Checkbutton(foodFrame, text="Somsa", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var10, command=somsa)
somsa.grid(row=9, column=0, sticky=W)


# Entry Food Section
textpalov = Entry(foodFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_palov)
textpalov.grid(row=0, column=1)

textshashlik = Entry(foodFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_shashlik)
textshashlik.grid(row=1, column=1)

textlagman = Entry(foodFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_lagman)
textlagman.grid(row=2, column=1)

textnorin = Entry(foodFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_norin)
textnorin.grid(row=3, column=1)

textmastava = Entry(foodFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_mastava)
textmastava.grid(row=4, column=1)

textmanti = Entry(foodFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_manti)
textmanti.grid(row=5, column=1)

textchuchvara = Entry(foodFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_chuchvara)
textchuchvara.grid(row=6, column=1)

textbifshteks = Entry(foodFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_bifshteks)
textbifshteks.grid(row=7, column=1)

textkabob = Entry(foodFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_kabob)
textkabob.grid(row=8, column=1)

textsomsa = Entry(foodFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_somsa)
textsomsa.grid(row=9, column=1)


# Drinks Label Section
nestle = Checkbutton(drinksFrame, text="Nestle", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var11, command=nestle)
nestle.grid(row=0, column=0, sticky=W)

fanta = Checkbutton(drinksFrame, text="Fanta", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var12, command=fanta)
fanta.grid(row=1, column=0, sticky=W)

dinay = Checkbutton(drinksFrame, text="Dinay", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var13, command=dinay)
dinay.grid(row=2, column=0, sticky=W)

cola = Checkbutton(drinksFrame, text="Coca-Cola", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var14, command=cola)
cola.grid(row=3, column=0, sticky=W)

coffee = Checkbutton(drinksFrame, text="Coffee", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var15, command=coffee)
coffee.grid(row=4, column=0, sticky=W)

redbull = Checkbutton(drinksFrame, text="Red Bull", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var16, command=redbull)
redbull.grid(row=5, column=0, sticky=W)

chortoq = Checkbutton(drinksFrame, text="Chortoq", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var17, command=chortoq)
chortoq.grid(row=6, column=0, sticky=W)

pepsi = Checkbutton(drinksFrame, text="Pepsi", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var18, command=pepsi)
pepsi.grid(row=7, column=0, sticky=W)

dena = Checkbutton(drinksFrame, text="Dena", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var19, command=dena)
dena.grid(row=8, column=0, sticky=W)

bliss = Checkbutton(drinksFrame, text="Bliss", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var20, command=bliss)
bliss.grid(row=9, column=0, sticky=W)

# Entry Drinks Section
textnestle = Entry(drinksFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_nestle)
textnestle.grid(row=0, column=1)

textfanta = Entry(drinksFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_fanta)
textfanta.grid(row=1, column=1)

textdinay = Entry(drinksFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_dinay)
textdinay.grid(row=2, column=1)

textcola = Entry(drinksFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_cola)
textcola.grid(row=3, column=1)

textcoffee = Entry(drinksFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_coffee)
textcoffee.grid(row=4, column=1)

textredbull = Entry(drinksFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_redbull)
textredbull.grid(row=5, column=1)

textchortoq = Entry(drinksFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_chortoq)
textchortoq.grid(row=6, column=1)

textpepsi = Entry(drinksFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_pepsi)
textpepsi.grid(row=7, column=1)

textdena = Entry(drinksFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_dena)
textdena.grid(row=8, column=1)

textbliss = Entry(drinksFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_bliss)
textbliss.grid(row=9, column=1)


# Cakes Label Section
napoleon = Checkbutton(cakesFrame, text="Napoleon", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var21, command=napoleon)
napoleon.grid(row=0, column=0, sticky=W)

chouxcake = Checkbutton(cakesFrame, text="ChouxCake", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var22, command=chouxcake)
chouxcake.grid(row=1, column=0, sticky=W)

absheron = Checkbutton(cakesFrame, text="Absheron", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var23, command=absheron)
absheron.grid(row=2, column=0, sticky=W)

cheesecake = Checkbutton(cakesFrame, text="CheeseCake", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var24, command=cheesecake)
cheesecake.grid(row=3, column=0, sticky=W)

madonna = Checkbutton(cakesFrame, text="Madonna", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var25, command=madonna)
madonna.grid(row=4, column=0, sticky=W)

bostoncreamcake = Checkbutton(cakesFrame, text="Boston Cream", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var26, command=bostoncreamcake)
bostoncreamcake.grid(row=5, column=0, sticky=W)

honeynut = Checkbutton(cakesFrame, text="Honeynut Cake", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var27, command=honeynut)
honeynut.grid(row=6, column=0, sticky=W)

blackforest = Checkbutton(cakesFrame, text="Blackforest", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var28, command=blackforest)
blackforest.grid(row=7, column=0, sticky=W)

anthill = Checkbutton(cakesFrame, text="Anthill", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var29, command=anthill)
anthill.grid(row=8, column=0, sticky=W)

praga = Checkbutton(cakesFrame, text="Praga", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var30, command=praga)
praga.grid(row=9, column=0, sticky=W)

# Entry Cakes Section
textnapoleon = Entry(cakesFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_napoleon)
textnapoleon.grid(row=0, column=1)

textchouxcake = Entry(cakesFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_chouxcake)
textchouxcake.grid(row=1, column=1)

textabsheron = Entry(cakesFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_absheron)
textabsheron.grid(row=2, column=1)

textcheesecake = Entry(cakesFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_cheesecake)
textcheesecake.grid(row=3, column=1)

textmadonna = Entry(cakesFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_madonna)
textmadonna.grid(row=4, column=1)

textbostoncreamcake = Entry(cakesFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_bostoncreamcake)
textbostoncreamcake.grid(row=5, column=1)

texthoneynut = Entry(cakesFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_honeynut)
texthoneynut.grid(row=6, column=1)

textblackforest = Entry(cakesFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_blackforest)
textblackforest.grid(row=7, column=1)

textanthill = Entry(cakesFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_anthill)
textanthill.grid(row=8, column=1)

textpraga = Entry(cakesFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_praga)
textpraga.grid(row=9, column=1)


# CostLabels & EntryFields Section
labelCostofFood = Label(costFrame, text="Cost of Food", font=("arial", 16, "bold"), bg="firebrick4", fg="white")
labelCostofFood.grid(row=0, column=0)
textCostofFood = Entry(costFrame, font=("arial", 16, "bold"), bd=6, width=14, state='readonly', textvariable=costoffoodvar)
textCostofFood.grid(row=0, column=1, padx=59)

labelCostofDrinks = Label(costFrame, text="Cost of Drinks", font=("arial", 16, "bold"), bg="firebrick4", fg="white")
labelCostofDrinks.grid(row=1, column=0)
textCostofDrinks = Entry(costFrame, font=("arial", 16, "bold"), bd=6, width=14, state='readonly', textvariable=costofdrinksvar)
textCostofDrinks.grid(row=1, column=1, padx=59)

labelCostofCakes = Label(costFrame, text="Cost of Cakes", font=("arial", 16, "bold"), bg="firebrick4", fg="white")
labelCostofCakes.grid(row=2, column=0)
textCostofCakes = Entry(costFrame, font=("arial", 16, "bold"), bd=6, width=14, state='readonly', textvariable=costofcakesvar)
textCostofCakes.grid(row=2, column=1, padx=59)

labelSubTotal = Label(costFrame, text="Sub Total", font=("arial", 16, "bold"), bg="firebrick4", fg="white")
labelSubTotal.grid(row=0, column=2)
textSubTotal = Entry(costFrame, font=("arial", 16, "bold"), bd=6, width=14, state="readonly", textvariable=subtotalvar)
textSubTotal.grid(row=0, column=3, padx=59)

labelServiceTax = Label(costFrame, text="Service Tax", font=("arial", 16, "bold"), bg="firebrick4", fg="white")
labelServiceTax.grid(row=1, column=2)
textServiceTax = Entry(costFrame, font=("arial", 16, "bold"), bd=6, width=14, state="readonly", textvariable=servicetaxvar)
textServiceTax.grid(row=1, column=3, padx=59)

labelTotalCost = Label(costFrame, text="Total Cost", font=("arial", 16, "bold"), bg="firebrick4", fg="white")
labelTotalCost.grid(row=2, column=2)
textTotalCost = Entry(costFrame, font=("arial", 16, "bold"), bd=6, width=14, state="readonly", textvariable=totalcostvar)
textTotalCost.grid(row=2, column=3, padx=59)


# Buttons Section
buttonTotal = Button(buttonFrame, text="Total", font=("arial", 14, "bold"), fg="white", bg="red4", bd=5, padx=8, pady=7, command=totalcost)
buttonTotal.grid(row=0, column=0)

buttonReceipt = Button(buttonFrame, text="Receipt", font=("arial", 14, "bold"), fg="white", bg="red4", bd=5, padx=8, pady=7, command=receipt)
buttonReceipt.grid(row=0, column=1)

buttonSave = Button(buttonFrame, text="Save", font=("arial", 14, "bold"), fg="white", bg="red4", bd=5, padx=8, pady=7, command=save)
buttonSave.grid(row=0, column=2)

buttonSend = Button(buttonFrame, text="Send", font=("arial", 14, "bold"), fg="white", bg="red4", bd=5, padx=8, pady=7, command=send)
buttonSend.grid(row=0, column=3)

buttonReset = Button(buttonFrame, text="Reset", font=("arial", 14, "bold"), fg="white", bg="red4", bd=5, padx=8, pady=7, command=reset)
buttonReset.grid(row=0, column=4)


# Textarea for receipt section
textReceipt = Text(recieptFrame, font=("arial", 12, "bold"), bd=3, width=42, height=17)
textReceipt.grid(row=0, column=0)

# Calculator Backend Section
operator = ''
def buttonClick(numbers):
    global operator
    operator = operator + numbers
    calculatorField.delete(0, END)
    calculatorField.insert(END, operator)

def clear():
    global operator
    operator = ''
    calculatorField.delete(0, END)

def answer():
    global operator
    result = str(eval(operator))
    calculatorField.delete(0, END)
    calculatorField.insert(0, result)
    operator = ''

# Calculator Field Section
calculatorField = Entry(calculatorFrame, font=("arial", 16, "bold"), width=32, bd=4)
calculatorField.grid(row=0, column=0, columnspan=4)

button7 = Button(calculatorFrame, text="7", font=("arial", 16, "bold"), fg="yellow", bg="red4", bd=6, width=5, command=lambda:buttonClick("7"))
button7.grid(row=1, column=0)

button8 = Button(calculatorFrame, text="8", font=("arial", 16, "bold"), fg="yellow", bg="red4", bd=6, width=5, command=lambda:buttonClick("8"))
button8.grid(row=1, column=1)

button9 = Button(calculatorFrame, text="9", font=("arial", 16, "bold"), fg="yellow", bg="red4", bd=6, width=5, command=lambda:buttonClick("9"))
button9.grid(row=1, column=2)

buttonPlus = Button(calculatorFrame, text="+", font=("arial", 16, "bold"), fg="yellow", bg="red4", bd=6, width=5, command=lambda:buttonClick("+"))
buttonPlus.grid(row=1, column=3)


button4 = Button(calculatorFrame, text="4", font=("arial", 16, "bold"), fg="yellow", bg="red4", bd=6, width=5, command=lambda:buttonClick("4"))
button4.grid(row=2, column=0)

button5 = Button(calculatorFrame, text="5", font=("arial", 16, "bold"), fg="red4", bg="white", bd=6, width=5, command=lambda:buttonClick("5"))
button5.grid(row=2, column=1)

button6 = Button(calculatorFrame, text="6", font=("arial", 16, "bold"), fg="red4", bg="white", bd=6, width=5, command=lambda:buttonClick("6"))
button6.grid(row=2, column=2)

buttonMinus = Button(calculatorFrame, text="-", font=("arial", 16, "bold"), fg="yellow", bg="red4", bd=6, width=5, command=lambda:buttonClick("-"))
buttonMinus.grid(row=2, column=3)


button1 = Button(calculatorFrame, text="1", font=("arial", 16, "bold"), fg="yellow", bg="red4", bd=6, width=5, command=lambda:buttonClick("1"))
button1.grid(row=3, column=0)

button2 = Button(calculatorFrame, text="2", font=("arial", 16, "bold"), fg="yellow", bg="red4", bd=6, width=5, command=lambda:buttonClick("2"))
button2.grid(row=3, column=1)

button3 = Button(calculatorFrame, text="3", font=("arial", 16, "bold"), fg="yellow", bg="red4", bd=6, width=5, command=lambda:buttonClick("3"))
button3.grid(row=3, column=2)

buttonMult = Button(calculatorFrame, text="*", font=("arial", 16, "bold"), fg="yellow", bg="red4", bd=6, width=5, command=lambda:buttonClick("*"))
buttonMult.grid(row=3, column=3)


buttonAns = Button(calculatorFrame, text="Ans", font=("arial", 16, "bold"), fg="yellow", bg="red4", bd=6, width=5, command=answer)
buttonAns.grid(row=4, column=0)

buttonClear = Button(calculatorFrame, text="Clear", font=("arial", 16, "bold"), fg="yellow", bg="red4", bd=6, width=5, command=clear)
buttonClear.grid(row=4, column=1)

button0 = Button(calculatorFrame, text="0", font=("arial", 16, "bold"), fg="yellow", bg="red4", bd=6, width=5, command=lambda:buttonClick("0"))
button0.grid(row=4, column=2)

buttonDiv = Button(calculatorFrame, text="/", font=("arial", 16, "bold"), fg="yellow", bg="red4", bd=6, width=5, command=lambda:buttonClick("/"))
buttonDiv.grid(row=4, column=3)


root.mainloop()
