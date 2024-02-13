def number_pars(number: str):
    tbl = str.maketrans("", "", "-()")
    new_text = number.replace("+7", "8")
    new_text = new_text.translate(tbl)
    return new_text

def comparison(t0, t1):
    if t0 == t1:
        return "YES"
    elif t0 == "8495" + t1:
        return "YES"
    else:
        return "NO"

t0 = number_pars(input())
t1 = number_pars(input())
t2 = number_pars(input())
t3 = number_pars(input())
if len(t0)==7:
	t0="8495"+t0
for x in (t1,t2,t3):
    print(comparison(t0, x))