import random

def cumprimento (texto): 
    return f"ola,{texto}"

def media_7_numeros(): 
     nums = [random.randint(1100) for _ in range(7)]
     media = sum(nums)/ len(nums)
     return nums, media 

if __ name__ == "__main__": 
     nome_completo = "Julia Ribeiro Costa"

     print(cumprimento(nome_-completo))
     
     nums, media = media_7_numeros()
     print("Numeros sorteados:",nums)
     print("Média:", media)
     

    



