'''Francesco Fresta - Matricola: 453710
'''
import time
class ContoCorrente:
	def __init__(self, _numeroconto, _correntista, _eta, _saldo, _datastipula):
		#inizializza le variabili di istanza
		self._numeroconto = _numeroconto
		self._correntista = _correntista
		self._eta = _eta
		self._saldo = _saldo
		self._datastipula = _datastipula
		self._fee=0.0
#variabili di istanza per la lista dei movimenti	
		self._listamovimenti = []
		self._tipo = ""
		self._importo = 0.0
		self._descrizione = ""
		self._contatore=0
		self._i=0
		self._j=0
		self._k=0
#variabili di istanza per bonifico
		self._beneficiario = ""
		self._causale = ""

	def displayinfo (self):
		#implementa la prima voce del menù mostrando a video informazioni sul correntista
		print("------")
		print("Numero conto: ", self._numeroconto)
		print("Intestato a: ", self._correntista)
		print("Età: ", self._eta)
		print("Stipulato il: ", self._datastipula)
		print("------\n")
		print("Saldo disponibile EUR: %.2f " % self._saldo)
		return ""

	def setfee(self):
		#imposta una fee in base agli anni di età
		if (self._eta <= 20):
			self._fee = 1.00
		elif (self._eta > 20 and self._eta < 65):
			self._fee = 2.50
		elif (self._eta >= 65):
			self._fee = 0.00

	def getfee(self):

		return self._fee

	def bonifico(self, _importo, _fee, _beneficiario):
		#simulazione bonifico - per semplicità al posto di chiedere l'IBAN chiedo il numero di conto del beneficiario
		self._beneficiario = _beneficiario
		self._causale = str(input("Causale: "))
		print("---\n")
		self._importo = _importo + _fee 
		if (self._saldo > (self._importo) and (self._beneficiario != self._numeroconto)):
			self._saldo = (self._saldo - self._importo)
			#Mi preoccupo di memorizzare ogni operazione nella lista movimenti 
			#in ordine: prima il tipo poi importo e infine descrizione
			self._listamovimenti.append("B") #inserisci il tipo - b=bonifico
			self._listamovimenti.append(self._importo) #inserisci importo comprensivo di fee
			self._listamovimenti.append("Bonifico da sportello") #inserisci descrizione
			print("Importo totale bonifico %d" % self._importo)	
			print("\nBonifico correttamente effettuato.\n")	
		else:
			print("Fondi insufficienti per effettuare l'operazione\n")

	def getsaldo(self):
		return self._saldo

	def getlistamovimenti(self):
		#ottieni la lista di tutti i movimenti effettuati
		#La lista deve essere vista come tante terne formate ognuna da : tipo operazione, importo,descrizione
		#esempio [P, 200, Prelievo da sportello] indica che è stato fatto un prelievo di 200 euro dallo sportello
		self._contatore=0
		self._i=0 #contatore che parte dallo zeresimo elemento e si occupa dei tipi "p"=prelievo "b"=bonifico
		self._j=1 #contatore che parte dal primo elemento e si occupa degli importi
		self._k=2 #contatore che parte dal secondo elemento e si occupa della descrizione per esteso
		print(str("Tipo").rjust(2), (str("Importo").rjust(12)), (str("Descrizione").rjust(23))) #formattazione a colonne
		while (self._contatore < len(self._listamovimenti)):
#stampa un movimento per riga
			print(str(self._listamovimenti[self._i]).rjust(2),(str(self._listamovimenti[self._j]).rjust(12)),"EUR",(str(self._listamovimenti[self._k]).rjust(31)))
			self._i+=3 #aumenta di tre posizioni, ricevendo per forza il tipo seguente
			self._j+=3 #aumenta di tre posizioni, ricevendo per forza l'importo seguente
			self._k+=3 #aumenta di tre posizioni, ricevendo per forza la descrizione seguete
			self._contatore+=3 #contatore si sposta di tre posizioni - ovvero un'operazione- alla volta
		return ""

	def prelievo(self, _importo, _fee):
	#è obbligatorio prelevare minimo 5 euro ed ovviamente al più tutti i soldi presenti sul conto
		self._importo = _importo + _fee
		if ((self._saldo >= self._importo) and (_importo > 4)):
			print("Prelievo in corso...\n")
			time.sleep(1)
			self._saldo -= self._importo
			print("Ritirare le banconote entro 5 secondi\n")
			time.sleep(5)
			print("Nuovo saldo disponibile: EUR %.2f" % self._saldo)
			#Anche qui mi preoccupo di memorizzare nella lista movimenti il singolo movimento
			self._listamovimenti.append("P") #inserisci il tipo - "p"=prelievo 
			self._listamovimenti.append(self._importo) #inserisci importo prelievo
			self._listamovimenti.append("Prelievo da sportello") #inserisci descrizione
		else:
			print("Fondi insufficienti oppure si sta prelevando meno di 5 euro.\n")

	def reset(self):
		#da usare alla chiusura delle operazioni presso lo sportello
		self._numeroconto = 0
		self._correntista = ""
		self._eta = 0
		self._saldo = 0.0
		self._datastipula = ""
		self._fee=0.0
		self._listamovimenti = []
		self._tipo = ""
		self._importo = 0.0
		self._descrizione = ""
		self._contatore=0
		self._i=0
		self._j=0
		self._k=0
		self._beneficiario = ""
		self._causale = ""