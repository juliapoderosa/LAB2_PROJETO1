

    import random

def cumprimento (texto):
    return f"ola,{texto}"

def media_7_numeros():
    
     nums = [random.randint(1, 100) for _ in range(7)]
     media = sum(nums)/ len(nums)
     return nums, media

if __name__ == "__main__":
     nome_completo = "Julia Ribeiro Costa"

     print(cumprimento(nome_completo))

     nums, media = media_7_numeros()
     print("Numeros sorteados:",nums)
     print("Média:", media)



