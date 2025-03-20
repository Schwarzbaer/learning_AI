from random import choice
from math import sqrt
from math import acos
from math import pi


def new_vec(length=10000):
    return [choice([-1, 1]) for _ in range(length)]


def similarity(vec_a, vec_b):
    dot_product = sum(a * b for a, b in zip(vec_a, vec_b))
    length_a = sqrt(sum(a**2 for a in vec_a))
    length_b = sqrt(sum(b**2 for b in vec_b))
    cosine_similarity = dot_product / (length_a * length_b)
    #return (acos(cosine_similarity) + pi) / (2 * pi)
    return cosine_similarity


def bind(vec_key, vec_value):
    return [k*v for k, v in zip(vec_key, vec_value)]


def bundle(*vecs):
    vec_summed = [sum(elems) for elems in zip(*vecs)]
    vec_clipped = [min(1, max(-1, e)) for e in vec_summed]
    return vec_clipped


def protect(vec):
    vec_length = len(vec)
    return [vec[(i+1) % vec_length] for i in range(vec_length)]


def unprotect(vec):
    vec_length = len(vec)
    return [vec[(i-1) % vec_length] for i in range(vec_length)]
