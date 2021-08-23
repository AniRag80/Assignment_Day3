def mod_div(fun):
  def inner(a, b):
    if a < b:
      a, b = b, a
    fun(a, b)
  return inner
@mod_div
def sub(a, b):
  print(a / b)
sub(8, 16)