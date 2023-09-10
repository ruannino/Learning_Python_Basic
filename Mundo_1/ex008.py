# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
# km = 1 > hm = 10 > dam = 100 > m = 1000 > dm = 10000 > cm = 100000 > mm = 1000000
medida = float(input('Digite a medida em metros: '))
conversor_km = medida / 1000
conversor_hm = medida / 100
conversor_dam = medida / 10
conversor_dm = medida * 10
conversor_cm = medida * 100
conversor_mm = medida * 1000
print(f'-' * 100)
print(f'CONVERSOR m²'.center(100))
print('-' * 100)
print(f'km = {conversor_km} > hm = {conversor_hm} > dam = {conversor_dam} > '
      f'm = {medida} > dm = {conversor_dm} > cm = {conversor_cm} > mm = {conversor_mm}')
print('-' * 100)
