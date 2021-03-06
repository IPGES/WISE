import MySQLdb
from Tkinter import *

class POM:

	def __init__(self, pom, root):
		self.pom = pom
		self.enabled = IntVar() 
		self.name = ''
		self.db = MySQLdb.connect("localhost", "wise", "wisepassword", "wisedb")
		self.dbcursor = self.db.cursor() 
		self.va = StringVar()
		self.vb = StringVar()
		self.vc = StringVar()
		self.ia = StringVar()
		self.ib = StringVar()
		self.ic = StringVar()
		self.root = root

		self.va.set('---')
		self.vb.set('---')
		self.vc.set('---')
		self.ia.set('---')
		self.ib.set('---')
		self.ic.set('---')


		self.dbcursor.execute('select name, active from pom where id = ' + str(pom))
		rec = self.dbcursor.fetchone()
		self.name = rec[0]
		self.enabled.set(rec[1])

        	col = pom*3

		Frame(root, height=3, width=112, bg='white').grid(row=0, column=col, columnspan=2, sticky='news')
		Label(root, bg='white', text=self.name).grid(row=1, column=col, sticky='ew')
		Checkbutton(root, bg='white', highlightthickness=0, bd=0, variable=self.enabled, command=self.cb).grid(row=1, column=col+1, sticky='ns')
		Frame(root, height=1, width=112, bg='black').grid(row=2, column=col, columnspan=2, sticky='news')
		Label(root, bg='white', text='Va :', anchor='e', padx=0).grid(row=3, column=col, sticky='ew')
		Label(root, bg='white', textvariable=self.va, anchor='w', padx=3).grid(row=3, column=col+1, sticky='ew')
		Frame(root, height=1, width=112, bg='grey').grid(row=4, column=col, columnspan=2, sticky='news')
		Label(root, bg='white', text='Vb :', anchor='e', padx=0).grid(row=5, column=col, sticky='ew')
		Label(root, bg='white', textvariable=self.vb, anchor='w', padx=3).grid(row=5, column=col+1, sticky='ew')
		Frame(root, height=1, width=112, bg='grey').grid(row=6, column=col, columnspan=2, sticky='news')
		Label(root, bg='white', text='Vc :', anchor='e', padx=0).grid(row=7, column=col, sticky='ew')
		Label(root, bg='white', textvariable=self.vc, anchor='w', padx=3).grid(row=7, column=col+1, sticky='ew')
		Frame(root, height=1, width=112, bg='grey').grid(row=8, column=col, columnspan=2, sticky='news')
		Label(root, bg='white', text='Ia :', anchor='e', padx=0).grid(row=9, column=col, sticky='ew')
		Label(root, bg='white', textvariable=self.ia, anchor='w', padx=3).grid(row=9, column=col+1, sticky='ew')
		Frame(root, height=1, width=112, bg='grey').grid(row=10, column=col, columnspan=2, sticky='news')
		Label(root, bg='white', text='Ib :', anchor='e', padx=0).grid(row=11, column=col, sticky='ew')
		Label(root, bg='white', textvariable=self.ib, anchor='w', padx=3).grid(row=11, column=col+1, sticky='ew')
		Frame(root, height=1, width=112, bg='grey').grid(row=12, column=col, columnspan=2, sticky='news')
		Label(root, bg='white', text='Ic :', anchor='e', padx=0).grid(row=13, column=col, sticky='ew')
		Label(root, bg='white', textvariable=self.ic, anchor='w', padx=3).grid(row=13, column=col+1, sticky='ew')
		Frame(root, height=1, width=112, bg='grey').grid(row=14, column=col, columnspan=2, sticky='news')
		Frame(root, width=2, bg='black').grid(row=0, column=col+2, rowspan=20, sticky='ns')

		self.refresh_data()

	def cb(self):
		
		self.dbcursor.execute('update pom set active = ' + str(self.enabled.get()) + ' where id = ' + str(self.pom))
		self.db.commit()

	def refresh_data(self):

		self.va.set('---')
		self.vb.set('---')
		self.vc.set('---')
		self.ia.set('---')
		self.ib.set('---')
		self.ic.set('---')
		
		if self.enabled == 1:
			self.dbcursor.execute('select id, insert_date, insert_date_micro from pom_data where pom_id = ' + str(self.pom) + ' order by insert_date, insert_date_micro')
 			rec = self.dbcursor.fetchone()
			if rec is None:
				return

			pom_data_id = rec[0]
			
			self.dbcursor.execute('select sample_type, phase, rms, min, max from pom_data_samples where pom_data_id = ' + str(pom_data_id))
			for rec in self.dbcursor.fetch():
				if rec[0] == 'voltage':
					if rec[1] == 'a':
						self.va = str(rec[2])
					if rec[1] == 'b':
						self.vb = str(rec[2])
					if rec[1] == 'c':
						self.vc = str(rec[2])
				if rec[0] == 'current':
					if rec[1] == 'a':
						self.ia = str(rec[2])
					if rec[1] == 'b':
						self.ib = str(rec[2])
					if rec[1] == 'c':
						self.ic = str(rec[2])
			
