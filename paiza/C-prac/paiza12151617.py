input_str = input()
N,K = map(int, input_str.split())

a_K = input()
a_K_list = list(map(int, a_K.split()))

print(a_K_list[K-1])