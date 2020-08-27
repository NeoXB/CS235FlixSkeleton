from domainmodel.actor import Actor

def test_actor_full_name():
    a1 = Actor("Taika Waititi")
    assert repr(a1) == "<Actor Taika Waititi>"
    a2 = Actor("")
    assert a2.actor_full_name is None
    a3 = Actor(42)
    assert a3.actor_full_name is None
    a4 = Actor("")
    assert repr(a4) == "<Actor None>"

def test_actor_add_colleague():
    a1 = Actor("Taika Waititi")
    a2 = Actor("Bob bob")
    a1.add_actor_colleague(a2)
    assert (a1.actor_colleague) == [a2]
    a3 = Actor("")
    a1.add_actor_colleague(a3)
    assert (a1.actor_colleague) == [a2, a3]

def test_actor_check_colleague():
    a1 = Actor("Taika Waititi")
    a2 = Actor("Bob bob")
    a1.add_actor_colleague(a2)
    assert (a1.check_if_this_actor_worked_with(a2)) == True