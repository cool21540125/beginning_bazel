
# 自幹的 Custom Rule
def _empty_impl(_):
    # This function is called when the rule is analyzed.
    # buildifier: disable=print
    print("----------------------")
    print("This rule does nothing")
    print("----------------------")

empty = rule(implementation = _empty_impl)