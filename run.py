from principios import lista
import random
from time import sleep

while True:
    x = random.randint(0, len(lista) - 1)
    print(f"O princípio do dia é:")
    sleep(1)
    print(f"\n       {lista[x]}")
    sleep(1.5)
    resp = str(input("Bora aplicar este princípio no seu dia!?   [Y/N]"))
    if resp.upper()[0] != "Y":
        print('\n Poxa, vamos tentar outro princípio então!')
        continue
    sleep(1)
    print("\nQue bom! E não se esqueça...")
    sleep(1)
    print("\nATUUUUUUE COM ENTUSIASMO E SERÁ ENTUSIASTA!\n\n\n")
    sleep(10)
    break



