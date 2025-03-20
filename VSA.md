## Hyperdimensional Computing (HD) / Vector Symbolic Architecture (VSA)

We use vectors of random elements as symbols.
Vectors have at least 10,000 dimensions. It follows that
* each vector is dissimilar (== nearly orthogonal) to all other (random) vectors.
* redundance makes them resistant to noise.

There are algebras of operations over HD vectors:
* MAP: Multiply-Add-Permute
* BSC: Binary Spatter Code
* HRR: Holographic Reduced Representation
* ...and more.

MAP algebra:
* Vector elements are -1, 0, or 1, and are initialized randomly at -1 or 1.
  * binary 0 == bipolar 1
  * binary 1 == bipolar -1
  * XOR      == multiplication
  * majority == sign
* Binding
  * associates a key with a value (and vice versa).
  * is implemented by element-wise multiplication.
  * is reversible; `a = bind(k, v)` -> `v = bind(a, k)` && `k = bind(a, v)`.
  * Thus, given two of a key, a value, and their association, the third can be inferred.
* Bundling
  * creates a set of symbols
  * is implemented by adding vectors, then clipping the values to -1 to 1.
* Permutation (Protect / Unprotect)
  * generates a symbol from another symbol
  * is implemented by shifting elements circularly to the left.
* Closeness of two symbols is calculated with Cosine Similarity of their vector representations (element-wise product of the vectors divided by the product of their lengths)


Papers and other sources:
* https://arxiv.org/pdf/2111.06077
  Part I is an overview of models, part II one of applications.
* Introduction to HD: https://redwood.berkeley.edu/wp-content/uploads/2020/08/HD-computing1.pdf
* https://www.tu-chemnitz.de/etit/proaut/workshops_tutorials/vsa_ecai20/rsrc/vsa_slides.pdf
* https://en.wikipedia.org/wiki/Hyperdimensional_computing
* https://en.wikipedia.org/wiki/Symbolic_artificial_intelligence
