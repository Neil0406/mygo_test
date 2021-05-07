
def test_func(input_value):
    import re
    s = str(input_value)
    s1 = re.sub("['{} ]",'', s)
    reverse_l = s1.split(':')
    reverse_l.reverse()

    num = len(reverse_l)
    for i in range(num):
        if reverse_l[i] in s:
            re = s[s.find(reverse_l[i]): s.find(reverse_l[i]) + len(reverse_l[i])]
            s = s.replace(re ,'x')
    s.replace(' ','')
    oup_put = ""
    for i in s:
        if i == "x":
            try:
                oup_put += reverse_l[0]
                reverse_l.remove(reverse_l[0])
            except:
                pass
        else:
            oup_put += i
    oup_put = eval(oup_put)
    return oup_put


"""
Please use Python 3 to answer question
Welcome to answer with unit testing code if you can
 
After you finish coding, please push to your GitHub account and share the link with us.
"""
 
# Please write a function to reverse the following nested input value into output value
 
# Input:
input_value = {
  'hired': {
    'be': {
      'to': {
        'deserve': 'I'
      }
    }
  }
}
 
# Output:
output_value = {
  'I': {
    'deserve': {
      'to': {
         'be': 'hired'
      }
    }
  }
}