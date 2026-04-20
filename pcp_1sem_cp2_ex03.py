cp1 = float(input("Digite sua nota no primeiro checkpoint: "))
cp2 = float(input("Digite sua nota no segundo checkpoint: "))
cp3 = float(input("Digite sua nota no terceiro checkpoint: "))
sp1 = float(input("Digite a nota do seu sprint 1: "))
sp2 = float(input("Digite a nota do seu sprint 2: "))
gs = float(input("Digite a nota do seu Global Solution: "))

menor = cp1

if cp2 < menor:
    menor = cp2

if cp3 < menor:
    menor = cp3

media_sem_peso = ((cp1 + cp2 + cp3 - menor + sp1 + sp2) / 4)

media_com_peso = media_sem_peso * 0.4 + gs * 0.6

print("Media sem peso:", round(media_sem_peso, 1))
print("Media com peso:", round(media_com_peso, 1))