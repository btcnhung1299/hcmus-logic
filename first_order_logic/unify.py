def unify(x, y, theta):
   if theta is False:
      return False
   if x == y:
      return theta
   if is_variable(x):
      return unify_var(x, y, theta)
   if is_variable(y):
      return unify_var(y, x, theta)
   if is_compound(x) and is_compound(y):
      return unify(x.args(), y.args(), unify(x.op(), y.op(), theta))
   if is_list(x) and is_list(y):
      return unify(x[1:], y[1:], unify(x[0], y[0], theta))
   return False

def unify_var(var, x, theta):
   if theta.contains(var):
      return unify(theta.substitute(var), x, theta)
   if theta.contains(x):
      return unify(var, theta.substitute(x), theta)
   theta.add(var, x)
   return theta

