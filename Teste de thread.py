import threading
import os
class nossaThread(threading.Thread):
    def __init__(self,idt,nome):
        threading.Thread.__init__(self)
        self.idt = idt
        self.nome = nome

    def run(self):
        print('Iniciando a Thread %s' % (self.nome))
        procThread(self.nome)
        print('Fim da Thread %s' % (self.nome))

def procThread (nome):
    cont = 0 
    while (cont<300):
        print('Processo %s da Thread %s %s ' % (str(cont), nome, os.getpid()))
        cont = cont + 1

thread1 = nossaThread(1,'t1')
thread2 = nossaThread(2,'t2')

arrThread = []
arrThread.append(thread1)
arrThread.append(thread1)

thread1.start()
thread2.start()

for t in arrThread:
    t.join()

print('Fim do programa')