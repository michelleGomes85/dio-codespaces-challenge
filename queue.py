# Exceção personalizada para erros relacionados à fila
class QueueError(Exception):
    def __init__(self, message="Queue error"):  
        super().__init__(message)  

# Implementa uma estrutura de fila
# Primeiro a entrar é o primeiro a sair [FIFO]
class Queue:
    def __init__(self):
        self.__list_queue = [] 

    # Adiciona um elemento ao início da fila
    def put(self, elem):
        self.__list_queue.insert(0, elem)

    # Remove e retorna o último elemento da fila
    def get(self):
        if len(self.__list_queue) == 0:
            raise QueueError()
            
        val = self.__list_queue[-1]  
        del self.__list_queue[-1] 
        return val

# Testa a implementação da fila
def main():
    que = Queue()
    que.put(1)
    que.put("dog") 
    que.put(False)

    try:
        for i in range(3):
            print(que.get())
    except QueueError as e:
        print(e)

# Chama a função main para executar o código
if __name__ == "__main__":
    main()
