from graphene import graphene as lib, Graphene

a = lib.graphene_vec2_alloc()
lib.graphene_vec2_init(a, 1.0, 2.0)
lib.graphene_vec2_free(a)

b = Graphene.vec2.alloc()
Graphene.vec2.init(a, 1.0, 2.0)
Graphene.vec2.free(b)
