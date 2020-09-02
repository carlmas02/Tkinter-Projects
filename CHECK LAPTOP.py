from tkinter import *
import requests
import bs4

root = Tk()
root.title("Status of laptop")
root.geometry("400x150")


#program for scrapping
res = requests.get("https://www.flipkart.com/honor-magicbook-15-ryzen-5-quad-core-8-gb"
	"-256-gb-ssd-windows-10-home-boh-waq9hnr-thin-light-laptop/p/itm5cc079"
	"c6abd4d?pid=COMFT42FHH9AGAN6&lid=LSTCOMFT42FHH9AGAN6LYNZPH&marketplace="
	"FLIPKART&srno=b_1_1&otracker=product_breadCrumbs_Laptops&fm=SEARCH&iid=en_"
	"GMcAonPA2as8DPjDuqFxVgH%2BFpb2otuTTadJafJqNfVsz5mOqlzSulvygUZvIyRSynXMgzA%2BSQsVs"
	"9kkw7502Q%3D%3D&ppt=browse&ppn=browse&ssid=tzdnn7l8j40000001598623274897")
soup = bs4.BeautifulSoup(res.text,"lxml")
available = soup.find(attrs = "_2AkmmA _3-iCOr wvj5kH")
available = str(available)

global status
status = available[39:48]
#print(type(status))

def get_status():
        if status == "NOTIFY ME":
                result = "Sorry the product is out of stock."
        else :
                result = "The product is available."
        Label(root,text = result).pack()                 
        



text = Label(root,text = "Click here to check availability of Honor Magicbook laptop",
             font = "comicsans 11",bg = "black",
             fg = "green").pack()

button = Button(root,text = "CLICK HERE",bg= "navajo white",command = get_status ).pack( pady = "10" )





root.mainloop()
