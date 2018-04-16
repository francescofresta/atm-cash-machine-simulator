'''
Francesco Fresta - Matricola: 453710

Ho implementato un simulatore di sportello ATM mono-utente. Due sono le funzioni più importanti, menu che permette di effettuare una 
scelta in modo interattivo, ed appunto la funzione 'scelta' che richiama i vari metodi i quali eseguono materialmente l'opzione 
selezionata. La libreria time mi permette di rendere un minimo interattivo il programma e cronometrare la sessione. 
La classe ContoCorrente da me scritta è richiamata dall'esterno per rendere il codice più leggibile e pulito.
All'avvio del programma viene richiesto il codice del conto. Ho implementato un sistema mono-utente dunque si potrà accedere 
digitando 232 numero di conto di Mario Rossi. 
Se si digitasse una stringa o comunque qualsiasi valore non atteso, il gestore dell'eccezione insisterebbe 
per far inserire il valore corretto.
Una volta dentro viene mostrato un menù che permette di: 1)Visualizzare le informazioni personali, 2)Visualizzare la lista dei 
movimenti totali per quella sessione, 3)Effettuare un prelievo di denaro, 4) Effettuare un bonifico ad un conto terzo, 5) Uscire
Questi cinque punti sono implementati nella funzione 'scelta' contenente dei metodi che ci consentono di compiere le operazioni.
Ovviamente non è possibile, ad esempio, prelevare meno di 5 euro oppure più del totale; inoltre come nella realtà non è possibile
prelevare centesimi ma solo cifre intere. 
Allo stesso modo è indispensabile fornire un numero di conto (es. 757) per compiere un bonifico.
Insomma ho cercato di implementare un sistema il più vicino possibile alla realtà tenendo conto, spero, di tutte le caratteristiche
possedute da tale dispositivo.
'''
import time #mi permette di usare sleep() per rendere interattiva l'esecuzione del programma

#RICHIAMO DELLA MIA CLASSE DA SORGENTE ESTERNO
from classe_contocorrente import ContoCorrente
from threading import Thread

##CREAZIONE OGGETTO ##
mariorossi = ContoCorrente(232, "Mario Rossi", 45, 12500, "20 aprile 2015")

cifraprelievo = 0
tassa = 0.0 #ho previsto il pagamento di una fee in base all'età
numero_carta_credito = 0
clienti = {} #un dizionario per memorizzare tutti i clienti
i=0
cliente = 0

#FUNZIONE MENU PER SCELTE INTERATTIVE
def menu(scelta):
	while (scelta <= 0 or (scelta > 5)):
		print("1) Informazioni personali \n")
		print("2) Lista ultimi movimenti  \n")
		print("3) Prelievo \n")
		print("4) Effettua un bonifico \n")
		print("5) Esci \n")
		while True:
			try:
				scelta = int(input("Cosa vuoi fare oggi? "))
				break
			except ValueError:
				print("Inserisci un numero intero compreso tra 1 e 5.")
	voce(scelta)#menu richiama la funzione voce
# ------------

#Prelievo e bonifico essendo blocchi corposi ho preferito inserirli in funzioni a parte
def sceltatre():
	while True:
		try:
			cifraprelievo = int(input("Quanto desideri prelevare? EUR: "))
			break
		except ValueError:
			print("È possibile prelevare solo cifre intere. Riprova.")
	time.sleep(2)
	mariorossi.setfee() #questo metodo calcola la tassa sull'operazione
	tassa=mariorossi.getfee()
	mariorossi.prelievo(cifraprelievo, tassa)

def sceltaquattro():
#Per il bonifico è necessario il numero di conto del beneficiario, es. 757, l'importo e la causale
	while True:
		try:
			beneficiario=int(input("Numero conto beneficiario: "))
			break
		except ValueError:
			print("Inserire un numero intero. Riprovare.")
	if ((beneficiario in clienti) and (beneficiario != 232)):
		while True:
			try:
				cifrabonifico=float(input("Importo del bonifico EUR: "))
				break
			except ValueError:
				print("Inserire un numero. Riprovare.")
		mariorossi.setfee()
		tassa=mariorossi.getfee()
		mariorossi.bonifico(cifrabonifico,tassa, beneficiario)
		print("Il saldo è EUR: %.2f" % mariorossi.getsaldo())
	else:
		print("Non è possibile effettuare l'operazione")

#FUNZIONE DELLE AZIONI DA INTRAPRENDERE IN BASE ALLA VOCE
def voce(scelta):
	if (scelta == 1):
		#INFORMAZIONI RELATIVE AL CONTO E AL CORRENTISTA
		print("Loading...")
		time.sleep(2)
		print("Di seguito sono riportare le sue informazioni personali.\n")
		print(mariorossi.displayinfo()) #il metodo mostra nome e cognome, eta, saldo del correntista
		
	elif (scelta == 2):
		#LISTA DEI MOVIMENTI
		print("Di seguito la lista degli ultimi movimenti.\n")
		time.sleep(1)
		mariorossi.getlistamovimenti()
	
	elif (scelta == 3):
		#PRELIEVO DEL DENARO CON ADDEBITO FEE IN BASE ALL'ETA
		print("Si è scelto di prelevare del denaro.\n")
		sceltatre()
		
	elif (scelta == 4):
		#EFFETTUARE BONIFICO CON ADDEBITO FEE IN BASE ALL'ETA
		sceltaquattro()
	
	elif (scelta == 5):
		#CONCLUDI ED ESCI - PER SICUREZZA RESETTARE PRIMA DI CHIUDERE
		mariorossi.reset()
		time.sleep(1)
		print("Operazione conclusa. \nGrazie e arrivederci")
		scelta=5
		return scelta

	home=""
	while (home!= "m"):
		home=(input("Premi m per tornare al menù principale: "))
	#dovendo ritornare dopo l'operazione, al menu la scelta si reimposta a 0
	scelta=0
	menu(scelta)
		
starttempo = time.time() #cronometro la sessione
print("Benvenuto. \n")
time.sleep(2)
clienti = {232: "Mario Rossi", 757 : "Luca Bianchi", 100:"Alessia Verdi"} #Dizionario clienti

def auth(numero_carta_credito, cliente):
	while (numero_carta_credito <= 0):
		while True:
			try:
				numero_carta_credito = int(input("Inserisci il numero del tuo conto: "))
				break
			except ValueError:
				print("Prego riprovare. Devi inserire un numero intero.\n")
	for i in clienti.keys():
#mi assicuro che il numero di conto immesso appartenga ai nostri clienti memorizzati nel dizionario
		if (numero_carta_credito == i):
			cliente = numero_carta_credito
#essendo mono-utente si può accedere solo come Mario Rossi codice cliente 232
	if (cliente == 232):
		scelta=0
		menu(scelta)
	else:
		print("Utente non abilitato per compiere operazioni allo sportello\n")

#Apro un thread in modo da poter intanto cronometrare la sessione
t = Thread(target=auth, args=(numero_carta_credito,cliente, ))
t.start()
t.join()
endtempo = time.time()
durata = float((endtempo-starttempo))
print("\nDurata sessione: %.2f secondi " % durata)