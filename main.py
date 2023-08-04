from tkinter import *
import datetime
from tkinter import Tk,StringVar, ttk
import tkinter.messagebox as tmsg

root=Tk()
root.title("Food System")

now = datetime.datetime.now()

time=now.strftime("%Y-%m-%d %X")

Label(root,text=f"Date & Time:{time}",font="arial 13").grid(row=2,column=6)

Label(root,text="def Restaurant(food)",font="comicsanms 25 italic",fg="Red",padx=200,pady=10,
).grid(row=0,column=0,columnspan=3,sticky="w")
Label(root,text="Jayanagar,Bangalore",font="tahoma 12 ",fg="Black",padx=200,pady=10).grid(row=1,column=0,columnspan=3)
Label(root,text="Menu",font="arial 10 bold").grid(row=2,column=0,columnspan=3)


###########################################################################################
#defining all the required functions
#adding payment option
pmethod=Label(root,font="arial 11 bold",text="Payment Method",bd=10,width=16,
anchor="w")
pmethod.grid(row=10,column=4)
#adding dropdown menu
paymentoptions=[
    "UPI",
    "Debit Card",
    "Credit Card",
    "Net Banking",
    "Cash On Delivery"
]



paymentmethod=ttk.Combobox(root,value=paymentoptions,width=15)
paymentmethod.current(1)#displaying default value
paymentmethod.grid(row=11,column=4)

#display address and mobile number


def closewindow():
    ex=tmsg.askyesno("Notification","Do you want to exit?")
    if ex>0:
        root.destroy()
        return
   
def reset():
    var_11.set("0")
    var_12.set("0")
    var_13.set("0")
    var_14.set("0")
    var_15.set("0")
    var_21.set("0")
    var_22.set("0")
    var_23.set("0")
    var_24.set("0")
    var_25.set("0")
    var_26.set("0")
    var_27.set("0")
    var_31.set("0")
    var_32.set("0")
    var_33.set("0")
    var_34.set("0")
    var_35.set("0")
    var_36.set("0")
    var_37.set("0")
    var_38.set("0")
    var_39.set("0")
    var_310.set("0")
    var_311.set("0")
    var_312.set("0")
    var_51.set("0")
    var_52.set("0")
    var_53.set("0")
    var_54.set("0")
    var_55.set("0")
    var_56.set("0")
    var_61.set("0")
    var_62.set("0")
    var_63.set("0")
    var_64.set("0")
    var_65.set("0")
    var_66.set("0")
    var_67.set("0")
    var_68.set("0")
    var_69.set("0")
    var_610.set("0")
    var_611.set("0")
    mobile.set("")
    address.set("")
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)
    var31.set(0)
    var32.set(0)
    var33.set(0)
    var34.set(0)
    var35.set(0)
    var36.set(0)
    var37.set(0)
    var38.set(0)
    var39.set(0)
    var310.set(0)
    var311.set(0)
    var51.set(0)
    var52.set(0)
    var53.set(0)
    var54.set(0)
    var55.set(0)
    var56.set(0)
    var61.set(0)
    var62.set(0)
    var63.set(0)
    var64.set(0)
    var65.set(0)
    var66.set(0)
    var67.set(0)
    var68.set(0)
    var69.set(0)
    var610.set(0)
    var611.set(0)
    total.set(0)


#displaying all the info 
def disp():
    if (address.get()=="") :
        tmsg.showinfo("Error","Please enter address where food is delivered ")
    elif mobile.get()=="":
        tmsg.showinfo("Error","Please enter mobile number")
    
    else:
        final=tmsg.showinfo("Info",f"""Your food will be delivered to {address.get()} within 30minutes.Our rider will contact to {mobile.get()} if required\n
        Thank you for ordering!""")
        



#calculating the total bill
def totalbill():
    food1=float(var_11.get())
    food2=float(var_12.get())
    food3=float(var_13.get())
    food4=float(var_14.get())
    food5=float(var_15.get())
    food6=float(var_21.get())
    food7=float(var_22.get())
    food8=float(var_23.get())
    food9=float(var_24.get())
    food10=float(var_25.get())
    food11=float(var_26.get())
    food13=float(var_31.get())
    food14=float(var_32.get())
    food15=float(var_33.get())
    food16=float(var_34.get())
    food17=float(var_35.get())
    food19=float(var_37.get())
    food20=float(var_38.get())
    food21=float(var_39.get())
    food22=float(var_310.get())
    food23=float(var_311.get())
    food24=float(var_51.get())
    food25=float(var_52.get())
    food26=float(var_53.get())
    food27=float(var_54.get())
    food28=float(var_55.get())
    food29=float(var_56.get())
    food30=float(var_61.get())
    food31=float(var_62.get())
    food32=float(var_63.get())
    food33=float(var_64.get())
    food34=float(var_65.get())
    food35=float(var_66.get())
    food36=float(var_67.get())
    food37=float(var_68.get())


    total.set((food1*100)+(food2*120)+(food3*100)+(food4*120)+(food5*140)+(food6*120)+(food7*120)+(food8*140)+(food9*140)+
    (food10*160)+(food11*160)+(food13*390)+(food14*390)+(food15*430)+(food16*430)+(food17*430)+(food19*470)+(food20*470)+(food21*470)+(food22*510)+(food23*510)+
    (food24*210)+(food25*210)+(food26*230)+(food27*230)+(food28*180)+(food29*210)+(food30*120)+(food31*120)+(food32*120)+(food33*120)+(food34*160)+(food35*160)+(food36*200)+(food37*200)+20)
#########################################################################################

#all variables involved
var11=IntVar()#starters
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var21=IntVar()#burgers
var22=IntVar()
var23=IntVar()
var24=IntVar()
var25=IntVar()
var26=IntVar()
var27=IntVar()
var31=IntVar()#pizza
var32=IntVar()
var33=IntVar()
var34=IntVar()
var35=IntVar()
var36=IntVar()
var37=IntVar()
var38=IntVar()
var39=IntVar()
var310=IntVar()
var311=IntVar()

var51=IntVar()#Pasta
var52=IntVar()
var53=IntVar()
var54=IntVar()
var55=IntVar()
var56=IntVar()
var61=IntVar()#dessert
var62=IntVar()
var63=IntVar()
var64=IntVar()
var65=IntVar()
var66=IntVar()
var67=IntVar()
var68=IntVar()
var69=IntVar()
var610=IntVar()
var611=IntVar()

#set int var to 0
var11.set(0)
var12.set(0)
var13.set(0)
var14.set(0)
var15.set(0)
var21.set(0)
var22.set(0)
var23.set(0)
var24.set(0)
var25.set(0)
var26.set(0)
var27.set(0)
var31.set(0)
var32.set(0)
var33.set(0)
var34.set(0)
var35.set(0)
var36.set(0)
var37.set(0)
var38.set(0)
var39.set(0)
var310.set(0)
var311.set(0)
var51.set(0)
var52.set(0)
var53.set(0)
var54.set(0)
var55.set(0)
var56.set(0)
var61.set(0)
var62.set(0)
var63.set(0)
var64.set(0)
var65.set(0)
var66.set(0)
var67.set(0)
var68.set(0)
var69.set(0)
var610.set(0)
var611.set(0)


#creating string variable
var_11=StringVar()#starters
var_12=StringVar()
var_13=StringVar()
var_14=StringVar()
var_15=StringVar()
var_21=StringVar()#burgers
var_22=StringVar()
var_23=StringVar()
var_24=StringVar()
var_25=StringVar()
var_26=StringVar()
var_27=StringVar()
var_31=StringVar()#Pizzas
var_32=StringVar()
var_33=StringVar()
var_34=StringVar()
var_35=StringVar()
var_36=StringVar()
var_37=StringVar()
var_38=StringVar()
var_39=StringVar()
var_310=StringVar()
var_311=StringVar()
var_312=StringVar()

var_51=StringVar()#pasta
var_52=StringVar()
var_53=StringVar()
var_54=StringVar()
var_55=StringVar()
var_56=StringVar()
var_61=StringVar()#Dessert
var_62=StringVar()
var_63=StringVar()
var_64=StringVar()
var_65=StringVar()
var_66=StringVar()
var_67=StringVar()
var_68=StringVar()
var_69=StringVar()
var_610=StringVar()
var_611=StringVar()

#additional things
address=StringVar()
total=StringVar()
mobile=StringVar()
change=StringVar()

##########################################################################################
#set the string var to "0"
var_11.set("0")
var_12.set("0")
var_13.set("0")
var_14.set("0")
var_15.set("0")
var_21.set("0")
var_22.set("0")
var_23.set("0")
var_24.set("0")
var_25.set("0")
var_26.set("0")
var_27.set("0")
var_31.set("0")
var_32.set("0")
var_33.set("0")
var_34.set("0")
var_35.set("0")
var_36.set("0")
var_37.set("0")
var_38.set("0")
var_39.set("0")
var_310.set("0")
var_311.set("0")
var_312.set("0")
var_51.set("0")
var_52.set("0")
var_53.set("0")
var_54.set("0")
var_55.set("0")
var_56.set("0")
var_61.set("0")
var_62.set("0")
var_63.set("0")
var_64.set("0")
var_65.set("0")
var_66.set("0")
var_67.set("0")
var_68.set("0")
var_69.set("0")
var_610.set("0")
var_611.set("0")
mobile.set("")
total.set("0")
change.set("0")



##########################################################################################
#config the variable
#foodntea['state']="DISABLED"
# foodncoffee.configure(state=DISABLED)
# foodnccoffee.configure(state=DISABLED)
# foodnmilk.configure(state=DISABLED)
# foodnbmilk.configure(state=DISABLED)
# foodncb.configure(state=DISABLED)
# foodnshira.configure(state=DISABLED)
# foodnpoha.configure(state=DISABLED)
# foodniv.configure(state=DISABLED)
# foodnmdosa.configure(state=DISABLED)
# foodnpdosa.configure(state=DISABLED)
# foodnvm.configure(state=DISABLED)
# foodnmcd.configure(state=DISABLED)
# foodnpcd.configure(state=DISABLED)
# foodnv65.configure(state=DISABLED)
# foodncchilly.configure(state=DISABLED)
# foodncmd.configure(state=DISABLED)
# foodnccrispy.configure(state=DISABLED)
# foodncl.configure(state=DISABLED)
# foodncs.configure(state=DISABLED)
# foodnms.configure(state=DISABLED)
# foodnfk.configure(state=DISABLED)
# foodnchapati.configure(state=DISABLED)
# foodntroti.configure(state=DISABLED)
# foodnnaan.configure(state=DISABLED)
# foodnkulcha.configure(state=DISABLED)
# foodnbkulcha.configure(state=DISABLED)
# foodnjeera.configure(state=DISABLED)
# foodncurd.configure(state=DISABLED)
# foodnrajma.configure(state=DISABLED)
# foodnvegpulav.configure(state=DISABLED)
# foodnvegbir.configure(state=DISABLED)
# foodncbir.configure(state=DISABLED)
# foodnmbir.configure(state=DISABLED)
# foodnfish.configure(state=DISABLED)







##########################################################################################
#checking state of checkbutton
#starters
def food_fries():
    if (var11.get()==1):
        foodnfri.config(state=NORMAL)
        var_11.set("")
    else:
        foodnfri.configure(state=DISABLED)
        var_11.set(0)

def food_piripiri():
    if (var12.get()==1):
        foodnpir.configure(state=NORMAL)
        var_12.set("")
    else:
        foodnpir.configure(state=DISABLED)
        var_12.set(0)

def food_shots():
    if (var13.get()==1):
        foodnshot.configure(state=NORMAL)
        var_13.set("")
    else:
        foodnshot.configure(state=DISABLED)
        var_13.set(0)

def food_garlic():
    if (var14.get()==1):
        foodngar.configure(state=NORMAL)
        var_14.set("")
    else:
        foodngar.configure(state=DISABLED)
        var_14.set(0)

def food_stuffed():
    if (var15.get()==1):
        foodnstf.configure(state=NORMAL)
        var_15.set("")
    else:
        foodnstf.configure(state=DISABLED)
        var_15.set(0)

#Burgers
def food_cheese():
    if var21.get()==1:
        foodncb.configure(state=NORMAL)
        var_21.set("")
    else:
        foodncb.configure(state=DISABLED)
        var_21.set(0)

def food_paneer():
    if var22.get()==1:
        foodntik.configure(state=NORMAL)
        var_22.set("")
    else:
        foodntik.configure(state=DISABLED)
        var_22.set(0)

def food_mac():
    if var23.get()==1:
        foodnmac.configure(state=NORMAL)
        var_23.set("")
    else:
        foodnmac.configure(state=DISABLED)
        var_23.set(0)

def food_italian():
    if var24.get()==1:
        foodniv.configure(state=NORMAL)
        var_24.set("")
    else:
        foodniv.configure(state=DISABLED)
        var_24.set(0)

def food_mexican():
    if var25.get()==1:
        foodnmex.configure(state=NORMAL)
        var_25.set("")
    else:
        foodnmex.configure(state=DISABLED)
        var_25.set(0)      

def food_veg():
    if var26.get()==1:
        foodnveg.configure(state=NORMAL)
        var_26.set("")
    else:
        foodnveg.configure(state=DISABLED)
        var_26.set(0)


#Pizzas
def food_marg():
    if var31.get()==1:
        foodnvm.configure(state=NORMAL)
        var_31.set("")
    else:
        foodnvm.configure(state=DISABLED)
        var_31.set(0)

def food_caps():
    if var32.get()==1:
        foodnmcd.configure(state=NORMAL)
        var_32.set("")
    else:
        foodnmcd.configure(state=DISABLED)
        var_32.set(0)


def food_farm():
    if var33.get()==1:
        foodnpcd.configure(state=NORMAL)
        var_33.set("")
    else:
        foodnpcd.configure(state=DISABLED)
        var_33.set(0)


def food_pan():
    if var34.get()==1:
        foodnfarm.configure(state=NORMAL)
        var_34.set("")
    else:
        foodnfarm.configure(state=DISABLED)
        var_34.set(0)

def food_jalap():
    if var35.get()==1:
        foodncc.configure(state=NORMAL)
        var_35.set("")
    else:
        foodncc.configure(state=DISABLED)
        var_35.set(0)

def food_paradise():
    if var37.get()==1:
        foodnccrispy.configure(state=NORMAL)
        var_37.set("")
    else:
        foodnccrispy.configure(state=DISABLED)
        var_37.set(0)

def food_indi():
    if var38.get()==1:
        foodncl.configure(state=NORMAL)
        var_38.set("")
    else:
        foodncl.configure(state=DISABLED)
        var_38.set(0)

def food_supreme():
    if var39.get()==1:
        foodnvs.configure(state=NORMAL)
        var_39.set("")
    else:
        foodnvs.configure(state=DISABLED)
        var_39.set(0)

def food_triple():
    if var310.get()==1:
        foodntrip.configure(state=NORMAL)
        var_310.set("")
    else:
        foodntrip.configure(state=DISABLED)
        var_310.set(0)

def food_veggie():
    if var311.get()==1:
        foodnfk.configure(state=NORMAL)
        var_311.set("")
    else:
        foodnfk.configure(state=DISABLED)
        var_311.set(0)


#Pasta
def food_aglio():
    if var51.get()==1:
        foodnag.configure(state=NORMAL)
        var_51.set("")
    else:
        foodnag.configure(state=DISABLED)
        var_51.set(0)

def food_penne():
    if var52.get()==1:
        foodnpen.configure(state=NORMAL)
        var_52.set("")
    else:
        foodnpen.configure(state=DISABLED)
        var_52.set(0)

def food_alpesto():
    if var53.get()==1:
        foodnal.configure(state=NORMAL)
        var_53.set("")
    else:
        foodnal.configure(state=DISABLED)
        var_53.set(0)

def food_arrabbiata():
    if var54.get()==1:
        foodnarb.configure(state=NORMAL)
        var_54.set("")
    else:
        foodnarb.configure(state=DISABLED)
        var_54.set(0)

def food_fried():
    if var55.get()==1:
        foodnrice.configure(state=NORMAL)
        var_55.set("")
    else:
        foodnrice.configure(state=DISABLED)
        var_55.set(0)

def food_schez():
    if var56.get()==1:
        foodnschez.configure(state=NORMAL)
        var_56.set("")
    else:
        foodnschez.configure(state=DISABLED)
        var_56.set(0)


#dessert
def food_mango():
    if var61.get()==1:
        foodnman.configure(state=NORMAL)
        var_61.set("")
    else:
        foodnman.configure(state=DISABLED)
        var_61.set(0)

def food_cran():
    if var62.get()==1:
        foodncran.configure(state=NORMAL)
        var_62.set("")
    else:
        foodncran.configure(state=DISABLED)
        var_62.set(0)
        
def food_green():
    if var63.get()==1:
        foodngreen.configure(state=NORMAL)
        var_63.set("")
    else:
        foodngreen.configure(state=DISABLED)
        var_63.set(0)


def food_passion():
    if var64.get()==1:
        foodnfruit.configure(state=NORMAL)
        var_64.set("")
    else:
        foodnfruit.configure(state=DISABLED)
        var_64.set(0)

def food_fruit():
    if var65.get()==1:
        foodndbc.configure(state=NORMAL)
        var_65.set("")
    else:
        foodndbc.configure(state=DISABLED)
        var_65.set(0)

def food_gulab():
    if var66.get()==1:
        foodngulab.configure(state=NORMAL)
        var_66.set("")
    else:
        foodngulab.configure(state=DISABLED)
        var_66.set(0)






##########################################################################################
Label(root,text="Starters",font="arial 12 bold").grid(row=3,column=0)
Label(root,text="Burgers",font="arial 12 bold").grid(row=3,column=2)
Label(root,text="12' Pizzas",font="arial 12 bold").grid(row=10,column=0)
Label(root,text="Pastas & Rice",font="arial 12 bold").grid(row=10,column=2)
Label(root,text="Desserts & Mocktails",font="arial 12 bold").grid(row=3,column=4)

#adding starters

foodfri=Checkbutton(root,text="Fries\t\t\t₹100",variable=var11,font=" helvetica 10",command=food_fries)
foodfri.grid(row=4,column=0,sticky="w")
foodnfri=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_11)
foodnfri.grid(row=4,column=1,sticky="w")

foodpir=Checkbutton(root,text="Piri Piri Fries\t\t₹120",variable=var12,font=" helvetica 10",command=food_piripiri)
foodpir.grid(row=5,column=0,sticky="W")
foodnpir=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_12)
foodnpir.grid(row=5,column=1,sticky="w")

foodshot=Checkbutton(root,text="Potato shots\t\t₹100",variable=var13,font=" helvetica 10",command=food_shots)
foodshot.grid(row=6,column=0,sticky="W")
foodnshot=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_13)
foodnshot.grid(row=6,column=1,sticky="w")

foodgar=Checkbutton(root,text="Garlic Bread\t\t₹120",variable=var14,font=" helvetica 10",command=food_garlic)
foodgar.grid(row=7,column=0,sticky="W")
foodngar=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_14)
foodngar.grid(row=7,column=1,sticky="w")

foodstf=Checkbutton(root,text="Stuffed Garlic Bread\t₹140",variable=var15,font=" helvetica 10",command=food_stuffed)
foodstf.grid(row=8,column=0,sticky="W")
foodnstf=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_15)
foodnstf.grid(row=8,column=1,sticky="w")

#adding Burgers

foodcb=Checkbutton(root,text="Cheese with Onion\t\t₹120",variable=var21,font=" helvetica 10",command=food_cheese)
foodcb.grid(row=4,column=2,sticky="W")
foodncb=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_21)
foodncb.grid(row=4,column=3,sticky="W")

foodtik=Checkbutton(root,text="Paneer Tikka\t\t₹120",variable=var22,font=" helvetica 10",command=food_paneer)
foodtik.grid(row=5,column=2,sticky="W")
foodntik=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_22)
foodntik.grid(row=5,column=3,sticky="w")

foodmac=Checkbutton(root,text="Double Mac\t\t₹140",variable=var23,font=" helvetica 10",command=food_mac)
foodmac.grid(row=6,column=2,sticky="W")
foodnmac=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_23)
foodnmac.grid(row=6,column=3,sticky="w")

foodiv=Checkbutton(root,text="Italian special\t\t₹140",variable=var24,font=" helvetica 10",command=food_italian)
foodiv.grid(row=7,column=2,sticky="W")
foodniv=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_24)
foodniv.grid(row=7,column=3,sticky="w")

foodmex=Checkbutton(root,text="Mexican Delight\t\t₹160",variable=var25,font=" helvetica 10",command=food_mexican)
foodmex.grid(row=8,column=2,sticky="W")
foodnmex=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_25)
foodnmex.grid(row=8,column=3,sticky="w")

foodveg=Checkbutton(root,text="Veggie special\t\t₹160",variable=var26,font=" helvetica 10",command=food_veg)
foodveg.grid(row=9,column=2,sticky="W")
foodnveg=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_26)
foodnveg.grid(row=9,column=3,sticky="w")

#pizzas
foodvm=Checkbutton(root,text="Margherita\t\t₹390",variable=var31,font=" helvetica 10",command=food_marg).grid(row=11,column=0,sticky="W")
foodnvm=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_31)
foodnvm.grid(row=11,column=1,sticky="w")

foodmcd=Checkbutton(root,text="Onion & Capsicum\t\t₹390",variable=var32,font=" helvetica 10",command=food_caps).grid(row=12,column=0,sticky="W")
foodnmcd=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_32)
foodnmcd.grid(row=12,column=1,sticky="w")

foodpcd=Checkbutton(root,text="Paneer Tikka\t\t₹430",variable=var33,font=" helvetica 10",command=food_pan).grid(row=13,column=0,sticky="W")
foodnpcd=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_33)
foodnpcd.grid(row=13,column=1,sticky="w")

foodfarm=Checkbutton(root,text="Farmhouse\t\t₹430",variable=var34,font=" helvetica 10",command=food_farm).grid(row=14,column=0,sticky="W")
foodnfarm=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_34)
foodnfarm.grid(row=14,column=1,sticky="w")

foodcchilly=Checkbutton(root,text="Spicy Jalapenos\t\t₹430",variable=var35,font=" helvetica 10",command=food_jalap).grid(row=15,column=0,sticky="W")
foodncc=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_35)
foodncc.grid(row=15,column=1,sticky="w")

foodccrispy=Checkbutton(root,text="Veggie Paradise\t\t₹470",variable=var37,font=" helvetica 10",command=food_paradise).grid(row=17,column=0,sticky="W")
foodnccrispy=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_37)
foodnccrispy.grid(row=17,column=1,sticky="w")

foodcl=Checkbutton(root,text="Indi Tandoori\t\t₹470",variable=var38,font=" helvetica 10",command=food_indi).grid(row=18,column=0,sticky="w")
foodncl=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_38)
foodncl.grid(row=18,column=1,sticky="w")

foodvs=Checkbutton(root,text="Veggie Supreme\t\t₹470",variable=var39,font=" helvetica 10",command=food_supreme).grid(row=19,column=0,sticky="W")
foodnvs=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_39)
foodnvs.grid(row=19,column=1,sticky="w")

foodtrip=Checkbutton(root,text="Triple Cheese\t\t₹510",variable=var310,font=" helvetica 10",command=food_triple).grid(row=20,column=0,sticky="W")
foodntrip=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_310)
foodntrip.grid(row=20,column=1,sticky="w")

foodfk=Checkbutton(root,text="All Time Mexican\t\t₹510",variable=var311,font=" helvetica 10",command=food_veggie).grid(row=16,column=0,sticky="W")
foodnfk=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_311)
foodnfk.grid(row=16,column=1,sticky="w")


#Pasta
foodag=Checkbutton(root,text="Agilio Olio Pasta\t\t₹210",variable=var51, font="helvetica 10",command=food_aglio).grid(row=11,column=2,sticky="w")
foodnag=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_51)
foodnag.grid(row=11,column=3)

foodpen=Checkbutton(root,text="Penne Alfredo Pasta\t₹210",variable=var52 , font="helvetica 10",command=food_penne).grid(row=12,column=2,sticky="w")
foodnpen=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_52)
foodnpen.grid(row=12,column=3)

foodal=Checkbutton(root,text="al Pesto Pasta\t\t₹230",variable=var53, font="helvetica 10",command=food_alpesto).grid(row=13,column=2,sticky="w")
foodnal=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_53)
foodnal.grid(row=13,column=3)

foodarb=Checkbutton(root,text="Arrabbiata Pasta\t\t₹230",variable=var54, font="helvetica 10",command=food_arrabbiata).grid(row=14,column=2,sticky="w")
foodnarb=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_54)
foodnarb.grid(row=14,column=3)

foodrice=Checkbutton(root,text="Fried Rice\t\t₹180",variable=var55, font="helvetica 10",command=food_fried).grid(row=15,column=2,sticky="w")
foodnrice=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_55)
foodnrice.grid(row=15,column=3)

foodschez=Checkbutton(root,text="Schezwan Fried Rice\t₹210",variable=var56, font="helvetica 10",command=food_schez).grid(row=16,column=2,sticky="w")
foodnschez=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_56)
foodnschez.grid(row=16,column=3)

#Desserts

foodman=Checkbutton(root,text="Mango toll\t\t\t₹120",variable=var61, font="helvetica 10",command=food_mango).grid(row=4,column=4,sticky="w")
foodnman=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_61)
foodnman.grid(row=4,column=5)

foodcran=Checkbutton(root,text="Cranberry Delight\t\t\t₹120",variable=var62, font="helvetica 10",command=food_cran).grid(row=5,column=4,sticky="w")
foodncran=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_62)
foodncran.grid(row=5,column=5)

foodgreen=Checkbutton(root,text="Green apple Mojito\t\t\t₹120",variable=var63 , font="helvetica 10",command=food_green).grid(row=6,column=4,sticky="w")
foodngreen=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_63)
foodngreen.grid(row=6,column=5)

foodfruit=Checkbutton(root,text="Passion Fruit\t\t\t₹120",variable=var64 , font="helvetica 10",command=food_passion).grid(row=7,column=4,sticky="w")
foodnfruit=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_64)
foodnfruit.grid(row=7,column=5)

fooddbc=Checkbutton(root,text="Death By Chocolate\t\t₹160",variable=var65 , font="helvetica 10",command=food_fruit).grid(row=8,column=4,sticky="w")
foodndbc=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_65)
foodndbc.grid(row=8,column=5)

foodgulab=Checkbutton(root,text="Gulab Jamoon with Ice cream\t₹160",variable=var66, font="helvetica 10",command=food_gulab).grid(row=9,column=4,sticky="w")
foodngulab=Entry(root,state=DISABLED,width=6,justify="right",textvariable=var_66)
foodngulab.grid(row=9,column=5)


#Bill-Calculations

Button(root,text="    Total    ",font="Arial 10 bold",borderwidth=3,relief=RAISED,command=totalbill).grid(row=13,column=4)

Entry(root,textvariable=total,width=15,).grid(row=13,column=5,sticky="w")

Label(root,text="  Delivery Charges= ₹20 ",font="Arial 10 bold").grid(row=14,column=4)

Button(root,text="    Reset    ",font="Arial 10 bold",borderwidth=3,relief=RAISED,command=reset,bg="blue",fg="white").grid(row=17,column=4)

Button(root,text="    Exit    ",font="Arial 10 bold",borderwidth=3,relief=RAISED,command=closewindow,bg="red",fg="white").grid(row=19,column=4)


#adding address
Label(root,text="Address",font="arial 11 bold").grid(row=10,column=6,sticky="w")
Entry(root,textvariable=address,width=50,justify="left").grid(row=11,column=6,sticky="w")
#adding mobile number
Label(root,text="Mobile Number",font="arial 11 bold").grid(row=13,column=6,sticky="w")
Entry(root,textvariable=mobile,width=30,justify="left").grid(row=14,column=6,sticky="w")


#Placing Order
Button(root,text="Place Order",font="arial 10 bold",borderwidth=3,relief=RAISED,command=disp,bg="green",fg="white").grid(row=17,column=5)


#display 
root.mainloop()

