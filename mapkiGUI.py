#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
	---===|||Inne uwagi|||===---
	-dla powiekszen wiekszych niz 17 dla duzych obszarow (np. Zielona Gora) program
	 moze dzialac dlugo i powodowac znaczacy spadek wydajnosci komputera :)
	-program nie wygeneruje mapki wiekszej niz 50 000px x 50 000px
	-do wykonania potrzebny interpreter python2.7 (nie sprawdzone pod pythonem 3 i nie zdziwie sie jak nie zadziała!) i biblioteka PIL do pobrania z:
		https://www.python.org/downloads/
		http://www.pythonware.com/products/pil/
'''


import Tkinter as tk 
import ttk
import tkMessageBox 
import ttk
import urllib2
import Image
import os
import re
import time


class Application(tk.Frame):              
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)   
        self.grid()                       
        self.createWidgets()

    def createWidgets(self):
    	top=self.winfo_toplevel()                
        top.rowconfigure(0, weight=1)            
        top.columnconfigure(0, weight=1)
    	self.columnconfigure(0, weight=1)
    	self.rowconfigure(0, weight=1)           
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)
        self.rowconfigure(7, weight=2)

    	self.LUAddressLabel = tk.Label(self, text='Adres lewego górnego kafelka:') #Left upper tile
    	self.LUAddressLabel.grid(row=0,column=0,sticky=tk.E+tk.W,pady=5)
	  
        self.LUAddressEntry = tk.Entry(self,width=60,)
        self.LUAddressEntry.grid(row=1,column=0,pady=5)

    	self.RDAddressLabel = tk.Label(self, text='Adres prawego dolnego kafelka:')#right down tile
    	self.RDAddressLabel.grid(row=2,column=0,pady=5)
      
        self.RDAddressEntry = tk.Entry(self,width=60)
        self.RDAddressEntry.grid(row=3,column=0,pady=5)

        self.FileNameLabel = tk.Label(self, text='Nazwa pliku docelowego',)#right down tile
        self.FileNameLabel.grid(row=4,column=0,pady=5)

        self.FileNameEntry = tk.Entry(self,width=60)
        self.FileNameEntry.grid(row=5,column=0,pady=5)

        self.GenButton = tk.Button(self, text='Generuj obraz', command=self.gen)   
        self.GenButton.grid(row=6,column=0,pady=5)


        self.pBVar = tk.IntVar()
        self.pB= ttk.Progressbar(self, orient='horizontal',length=400,mode='determinate',variable=self.pBVar)
        self.pB.grid(row=7,column=0,pady=5)

        
        
    def gen(self):
    	self.FN = self.FileNameEntry.get()
    	with open(self.FN+'.log','w') as log:
	    	self.LUA = self.LUAddressEntry.get()
	    	self.RDA = self.RDAddressEntry.get()
	    	
	    	if self.LUA == '' or self.RDA == '' or self.FN == '':
	    		tkMessageBox.showerror('BRAK DANYCH!', 'Chyba zapomniałeś o czymś!' )
	    		return
	    	self.LUAs = self.LUA.split('/')
	    	self.RDAs = self.RDA.split('/')
	    	self.LUAs[5] = self.LUAs[5].split('.')[0]
	    	self.RDAs[5] = self.RDAs[5].split('.')[0]
	    	#print ('zoom: '+self.LUAs[3])
	    	#print ('x: '+self.LUAs[4])
	    	#print ('y: '+self.LUAs[5])
	    	#print ('zoom: '+self.RDAs[3])
	    	#print ('x: '+self.RDAs[4])
	    	#print ('y: '+self.RDAs[5])

	    	log.write ('LU zoom: '+self.LUAs[3]+'\n')
	    	log.write ('LU x: '+self.LUAs[4]+'\n')
	    	log.write ('LU y: '+self.LUAs[5]+'\n')
	    	log.write ('RD zoom: '+self.RDAs[3]+'\n')
	    	log.write ('RD x: '+self.RDAs[4]+'\n')
	    	log.write ('RD y: '+self.RDAs[5]+'\n')
	    	log.write ('filename: '+self.FN+'\n\n\n')


			
		if self.LUAs[3] != self.RDAs[3]:
			tkMessageBox.showerror('ZŁE DANE!', 'Chyba coś namieszałeś!\nLinki mają inne przybliżenie!' )
			return


		
		#pobieranie
		self.startX=int(self.LUAs[4])
		self.startY=int(self.LUAs[5])
		self.endX=int(self.RDAs[4])+1
		self.endY=int(self.RDAs[5])+1
		self.zoom=int(self.LUAs[3])
		self.howManyX=self.endX-self.startX
		self.howManyY=self.endY-self.startY

		if self.howManyY*256>50000 or self.howManyX*256>50000:
			tkMessageBox.showerror('Za duzy obrszar!', 'Nie możliwy jest zapis obrazka o krawędzi wiekszej niz 50 000px!')

		self.pB['maximum']=(self.howManyY*self.howManyX)-1
		
		self.newImg=Image.new('RGB',(self.howManyX*256,self.howManyY*256),)

		self.url="tile.openstreetmap.org/"+str(self.zoom)+'/'
		for self.a in range(self.startX,self.endX):
			for self.b in range(self.startY,self.endY):
				self.update()
				self.pBVar.set(((self.a-self.startX)*self.howManyY)+self.b-self.startY)
				self.curl='http://a.'+self.url+str(self.a)+'/'+str(self.b)+'.png'
				print ('pobieram: '+self.curl+'\n')
				print('value:'+str((self.a-self.startX)*self.howManyY+self.b-self.startY)+'x'+str(self.pBVar.get())+'/'+str(self.howManyX*self.howManyY))
				
				try:
					response = urllib2.urlopen(self.curl)
				except urllib2.URLError:
					log.write('Błąd przy adresie: '+self.curl+' \n')
					self.curl='http://b.'+self.url+str(self.a)+'/'+str(self.b)+'.png'
					try:
						response = urllib2.urlopen(self.curl)
					except urllib2.URLError:
						log.write('Błąd przy adresie: '+self.curl+' \n')
						self.curl='http://c.'+self.url+str(self.a)+'/'+str(self.b)+'.png'
						try:
							response = urllib2.urlopen(self.curl)
						except urllib2.URLError:
							log.write('Błąd przy adresie: '+self.curl+' \n')
							self.curl='http://d.'+self.url+str(self.a)+'/'+str(self.b)+'.png'
							try:
								response = urllib2.urlopen(self.curl)
							except urllib2.URLError:
								log.write('!!!Błąd krytyczny przy adresie: '+self.curl+' \n')
								continue
				self.fName=str(self.a)+'x'+str(self.b)+'.png'
				self.f=open(self.fName,'wb')
				self.f.write(response.read())
				self.f.close()
				self.i=self.a-self.startX
				self.j=self.b-self.startY
				try:
					self.img = Image.open(self.fName)
				except IOError:
					log.write('Nie ma obrazka'+self.fName+'\n')
				else:
					self.newImg.paste(self.img,(self.i*256,self.j*256))#paste downloaded image to newimage
					os.remove(self.fName)
		self.p=re.compile ('.*[.].*')		
		if re.search(self.p,self.FN)==None:
			self.newImg.save(self.FN+'.png')
		else:
			self.newImg.save(self.FN)
		tkMessageBox.showinfo('KONIEC!', 'Mapkę ściągnięto pomyślnie!' )

app = Application()                       
app.master.title('OSM Downloader by other019')    
app.mainloop()       
