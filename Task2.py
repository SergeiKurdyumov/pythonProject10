class TypedMeta():
    a = None

    def __new__(cls):
        if cls.a is None:
            a = super().__new__(cls)
        return cls.a

obj_1 = TypedMeta()
obj_2 = TypedMeta()
obj_3 = TypedMeta()
obj_4 = TypedMeta()
print(obj_1 is obj_2 is obj_3 is obj_4)
print(obj_1 is obj_2)