def srt(d,base="k|v",reversed1=False):
    assert type(d)==dict,"Dictionary argument is required"
    assert base.upper()=="K|V" or base.upper()=="K" or base.upper()=="V", "enter valid \"base\" argument"

    sorted_dict = {}

    if base.upper()=="K|V" or base.upper()=="K":
    
        for x in sorted(d.keys(),reverse=reversed1):
            sorted_dict.update({x:d[x]})
            print(x)
    else:

        empty_dict = {}
        
        for x in d:
            empty_dict.update({d[x]:x})

        for x in sorted(empty_dict,reverse=reversed1):
            sorted_dict.update({empty_dict[x]:x})

    return sorted_dict

def a():
    print("Hellow")

if __name__ == "__main__" :
    a()
    dict1 = {"B":10,"A":1,"C":5}
    print(srt(dict1,"k",True))
    print(srt(dict1,"v",True))
