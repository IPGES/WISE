import MySQLdb
from Tkinter import *

class POM:

	def __init__(self, pom, root, graph_pom):
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

		Radiobutton(root, text="Graph", value=pom, variable=graph_pom, indicatoron=0).grid(row=0, column=col, sticky='news')
		Checkbutton(root, text="Enable", variable=self.enabled, command=self.cb, indicatoron=0).grid(row=0, column=col+1, sticky='news') 	
		Frame(root, height=3, width=112, bg='white').grid(row=1, column=col, columnspan=2, sticky='news')
		Label(root, bg='white', text=self.name).grid(row=2, column=col, columnspan=2, sticky='ew')
		Frame(root, height=1, width=112, bg='black').grid(row=3, column=col, columnspan=2, sticky='news')
		Label(root, bg='white', text='Va :', anchor='e', padx=0).grid(row=4, column=col, sticky='ew')
		Label(root, bg='white', textvariable=self.va, anchor='w', padx=3).grid(row=4, column=col+1, sticky='ew')
		Frame(root, height=1, width=112, bg='grey').grid(row=5, column=col, columnspan=2, sticky='news')
		Label(root, bg='white', text='Vb :', anchor='e', padx=0).grid(row=6, column=col, sticky='ew')
		Label(root, bg='white', textvariable=self.vb, anchor='w', padx=3).grid(row=6, column=col+1, sticky='ew')
		Frame(root, height=1, width=112, bg='grey').grid(row=7, column=col, columnspan=2, sticky='news')
		Label(root, bg='white', text='Vc :', anchor='e', padx=0).grid(row=8, column=col, sticky='ew')
		Label(root, bg='white', textvariable=self.vc, anchor='w', padx=3).grid(row=8, column=col+1, sticky='ew')
		Frame(root, height=1, width=112, bg='grey').grid(row=9, column=col, columnspan=2, sticky='news')
		Label(root, bg='white', text='Ia :', anchor='e', padx=0).grid(row=10, column=col, sticky='ew')
		Label(root, bg='white', textvariable=self.ia, anchor='w', padx=3).grid(row=10, column=col+1, sticky='ew')
		Frame(root, height=1, width=112, bg='grey').grid(row=11, column=col, columnspan=2, sticky='news')
		Label(root, bg='white', text='Ib :', anchor='e', padx=0).grid(row=12, column=col, sticky='ew')
		Label(root, bg='white', textvariable=self.ib, anchor='w', padx=3).grid(row=12, column=col+1, sticky='ew')
		Frame(root, height=1, width=112, bg='grey').grid(row=13, column=col, columnspan=2, sticky='news')
		Label(root, bg='white', text='Ic :', anchor='e', padx=0).grid(row=14, column=col, sticky='ew')
		Label(root, bg='white', textvariable=self.ic, anchor='w', padx=3).grid(row=14, column=col+1, sticky='ew')
		Frame(root, height=1, width=112, bg='grey').grid(row=15, column=col, columnspan=2, sticky='news')
		Frame(root, width=2, bg='black').grid(row=0, column=col+2, rowspan=20, sticky='ns')

		self.refresh_data()

	def cb(self):
		
		self.dbcursor.execute('update pom set active = ' + str(self.enabled.get()) + ' where id = ' + str(self.pom))
		self.db.commit()

	def graph_select(self):

		print "blah"

	def refresh_data(self):

		self.va.set('---')
		self.vb.set('---')
		self.vc.set('---')
		self.ia.set('---')
		self.ib.set('---')
		self.ic.set('---')
		
		if self.enabled.get() == 1:
			sql_stmt = "select pom_data.id, insert_date, insert_date_micro from pom_data, pom_data_samples where pom_data.id = pom_data_id and pom_id = " + str(self.pom) + " and sample_type = 'voltage' order by insert_date desc, insert_date_micro desc limit 1"
			self.dbcursor.execute(sql_stmt)
 			rec = self.dbcursor.fetchone()
			if rec != None:
				pom_data_id = rec[0]
			
				sql_stmt = 'select phase, rms, min, max from pom_data_samples where pom_data_id = ' + str(pom_data_id)
				self.dbcursor.execute(sql_stmt)
				for rec in self.dbcursor.fetchall():
					if rec[0] == 'a':
						self.va.set(str(rec[1]))
					if rec[0] == 'b':
						self.vb.set(str(rec[1]))
					if rec[0] == 'c':
						self.vc.set(str(rec[1]))
			
			sql_stmt = "select pom_data.id, insert_date, insert_date_micro from pom_data, pom_data_samples where pom_data.id = pom_data_id and pom_id = " + str(self.pom) + " and sample_type = 'current' order by insert_date desc, insert_date_micro desc limit 1"
			self.dbcursor.execute(sql_stmt)
 			rec = self.dbcursor.fetchone()
			if rec != None:

				pom_data_id = rec[0]
			
				sql_stmt = 'select phase, rms, min, max from pom_data_samples where pom_data_id = ' + str(pom_data_id)
				self.dbcursor.execute(sql_stmt)
				for rec in self.dbcursor.fetchall():
					if rec[0] == 'a':
						self.ia.set(str(rec[1]))
					if rec[0] == 'b':
						self.ib.set(str(rec[1]))
					if rec[0] == 'c':
						self.ic.set(str(rec[1]))
			
			self.db.commit()
