from pubsub import pub
import os
os.system('cls')

def gabriel(arg):
    print('Atualizações para Gabriel: ', arg['topic'])
    print( arg['news'])
    print()

def iann(arg):
    print('Atualizações para Iann: ', arg['topic'])
    print(arg[ 'news'])
    print()


pub.subscribe(gabriel, 'noticias')
pub.subscribe(gabriel, 'futebol')
pub.subscribe(iann, 'futebol')


pub.sendMessage( 'futebol', arg={'topic': 'Brasil x Marrocos', 'news': 'Brasil derrotado por marrocos'})
pub.sendMessage( 'noticias', arg={'topic': 'Guerra', 'news': 'Guerra na ucrania'})

