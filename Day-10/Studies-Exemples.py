""" def format_name(f_name, l_name):
  return f"{f_name} {l_name}".title()

print(format_name('lena', 'kirara')) """


def format_name(f_name, l_name):
  if f_name == '' or l_name == '':
    return "You didn't provide valid input"
  input_f_name = f_name.title()
  input_l_name = l_name.title()
  return f"{input_f_name} {input_l_name}"

print(format_name(input("What's your first name? "), input("What's your last name? ")))
