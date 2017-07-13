from Tkinter import *
import tkMessageBox
import Pmw
import string
class Shell:
	def __init__(self, title=''):
		self.root = Tk()
		Pmw.initialise(self.root)
		self.root.title(title)
		
	def win(self, master):
		Label(master, text='From:').grid(row=0, sticky=W)
		Label(master, text='To:').grid(row=1, sticky=W)
		Label(master, text='Password:').grid(row=2,sticky=W)
		Label(master, text='Message:').grid(row=3,sticky=W)
		
		self.fromaddress = Entry(master, width = 30)
		self.toaddress = Entry(master, width = 30)
		self.password= Entry(master, width = 15, show='*')
		self.password.pack(fill=BOTH, expand=1, padx = 10)
		
		self.userInfo = Pmw.ScrolledText(master,borderframe=1,labelpos=N,usehullsize=1,hull_width=270,hull_height=100,text_padx=10,text_pady=10,text_wrap=NONE)
		self.userInfo.configure(text_font = ('verdana', 8))
		self.userInfo.pack(fill=BOTH, expand=1)
		Button(master, text="Send", command= self.send).grid(row=4,column=1, sticky=W)
		self.fromaddress.grid(row=0, column=1, sticky=W)
		
		self.toaddress.grid(row=1, column=1, sticky=W)
		
		self.userInfo.grid(row=3, column=1, sticky=W)
		self.password.grid(row=2,column=1, sticky=W)
		
		
	def send(self):
		import smtplib 
		if self.fromaddress.get().strip() == "":
			tkMessageBox.showerror ("Error","Enter sender's email address")
		self.fromaddrs=self.fromaddress.get().strip()
		if self.toaddress.get().strip() == "":
			tkMessageBox.showerror ("Error","Enter receiver's email address")
		self.toaddrs=self.toaddress.get().strip()
		if self.password.get().strip() == "":
			tkMessageBox.showerror ("Error","Enter password")
		self.password1=self.password.get().strip()
		if self.userInfo.get().strip() == "":
			tkMessageBox.showerror ("Error","Enter some message")
		msg=self.userInfo.get().strip()
		server = smtplib.SMTP("smtp.gmail.com", 587)
		server.ehlo('x')
		server.starttls()
		server.ehlo('x')
		server.login( self.fromaddrs,self.password1)
		try:
			server.sendmail(self.fromaddrs,self.toaddrs,  msg)
			tkMessageBox.showinfo ("Mail","Mail sent successfully!")
		except:
			tkMessageBox.showerror ("Mail","Unable to send mail")
		
if __name__ == '__main__':
	shell=Shell(title='Report')
	shell.root.geometry("%dx%d" % (400,350))
	shell.win(shell.root)
	shell.root.mainloop()
