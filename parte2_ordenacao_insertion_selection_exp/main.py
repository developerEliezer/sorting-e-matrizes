import random
import sys

# Evita erro de limite de recursão no Quick Sort
sys.setrecursionlimit(10000)


# 1. OS 4 ALGORITMOS DE ORDENAÇÃO


def bubble_sort(v):
    comp = 0
    trocas = 0
    n = len(v)
    for i in range(n):
        for j in range(0, n - i - 1):
            comp += 1
            if v[j] > v[j + 1]:
                v[j], v[j + 1] = v[j + 1], v[j]
                trocas += 1
    return comp, trocas


def insertion_sort(v):
    comp = 0
    movs = 0
    for i in range(1, len(v)):
        chave = v[i]
        j = i - 1
        while j >= 0:
            comp += 1
            if v[j] > chave:
                v[j + 1] = v[j]
                movs += 1
                j -= 1
            else:
                break
        v[j + 1] = chave
    return comp, movs


def selection_sort(v):
    comp = 0
    trocas = 0
    n = len(v)
    for i in range(n):
        menor = i
        for j in range(i + 1, n):
            comp += 1
            if v[j] < v[menor]:
                menor = j
        if menor != i:
            v[i], v[menor] = v[menor], v[i]
            trocas += 1
    return comp, trocas


# Quick Sort usando variáveis globais para contar

comp_quick = 0
mov_quick = 0

def particionar(v, inicio, fim):
    global comp_quick, mov_quick
    pivo = v[fim]
    i = inicio - 1
    for j in range(inicio, fim):
        comp_quick += 1
        if v[j] <= pivo:
            i += 1
            if i != j:
                v[i], v[j] = v[j], v[i]
                mov_quick += 1
    if (i + 1) != fim:
        v[i + 1], v[fim] = v[fim], v[i + 1]
        mov_quick += 1
    return i + 1

def rodar_quick(v, inicio, fim):
    if inicio < fim:
        p = particionar(v, inicio, fim)
        rodar_quick(v, inicio, p - 1)
        rodar_quick(v, p + 1, fim)

def quick_sort(v):
    global comp_quick, mov_quick
    comp_quick = 0
    mov_quick = 0
    if len(v) > 0:
        rodar_quick(v, 0, len(v) - 1)
    return comp_quick, mov_quick



# 2. RODANDO OS EXPERIMENTOS (ETAPA 3)


random.seed(42) # Semente para manter os mesmos números

tamanhos = [10, 20, 1000]

print("=== ETAPA 3: RESULTADOS DOS TESTES ===")

for tam in tamanhos:
    # Gera a lista base e faz 4 cópias identicas
    original = [random.randint(1, 10000) for _ in range(tam)]
    
    v1 = original.copy()
    v2 = original.copy()
    v3 = original.copy()
    v4 = original.copy()
    
    # Roda cada um
    c_bub, t_bub = bubble_sort(v1)
    c_ins, m_ins = insertion_sort(v2)
    c_sel, t_sel = selection_sort(v3)
    c_qui, m_qui = quick_sort(v4)
    
    print(f"\n--- TAMANHO: {tam} ---")
    print(f"Bubble Sort    -> Comparações: {c_bub} | Trocas: {t_bub}")
    print(f"Insertion Sort -> Comparações: {c_ins} | Movimentações: {m_ins}")
    print(f"Selection Sort -> Comparações: {c_sel} | Trocas: {t_sel}")
    print(f"Quick Sort     -> Comparações: {c_qui} | Movimentações: {m_qui}")



# 3. DESAFIO ADICIONAL


print("\n=== DESAFIO ADICIONAL (100 ELEMENTOS) ===")

# Vetor Aleatorio
v_aleatorio = [random.randint(1, 10000) for _ in range(100)]
c_b, t_b = bubble_sort(v_aleatorio.copy())
c_i, m_i = insertion_sort(v_aleatorio.copy())
c_s, t_s = selection_sort(v_aleatorio.copy())
c_q, m_q = quick_sort(v_aleatorio.copy())
print(f"\n[Aleatório]")
print(f"Bubble: Comp={c_b}, Trocas={t_b} | Insertion: Comp={c_i}, Mov={m_i}")
print(f"Selection: Comp={c_s}, Trocas={t_s} | Quick: Comp={c_q}, Mov={m_q}")

# Vetor Ordenado
v_ordenado = list(range(1, 101))
c_b, t_b = bubble_sort(v_ordenado.copy())
c_i, m_i = insertion_sort(v_ordenado.copy())
c_s, t_s = selection_sort(v_ordenado.copy())
c_q, m_q = quick_sort(v_ordenado.copy())
print(f"\n[Já Ordenado]")
print(f"Bubble: Comp={c_b}, Trocas={t_b} | Insertion: Comp={c_i}, Mov={m_i}")
print(f"Selection: Comp={c_s}, Trocas={t_s} | Quick: Comp={c_q}, Mov={m_q}")

# Vetor Invertido
v_invertido = list(range(100, 0, -1))
c_b, t_b = bubble_sort(v_invertido.copy())
c_i, m_i = insertion_sort(v_invertido.copy())
c_s, t_s = selection_sort(v_invertido.copy())
c_q, m_q = quick_sort(v_invertido.copy())
print(f"\n[Ordem Inversa]")
print(f"Bubble: Comp={c_b}, Trocas={t_b} | Insertion: Comp={c_i}, Mov={m_i}")
print(f"Selection: Comp={c_s}, Trocas={t_s} | Quick: Comp={c_q}, Mov={m_q}")
