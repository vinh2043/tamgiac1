canh_1 = int(input('cạnh thứ 1:'))
canh_2 = int(input('cạnh thứ 2:'))
canh_3 = int(input('cạnh thứ 3:'))
là_tamgiac = (canh_1 + canh_2) > canh_3 and (canh_1 + canh_3) > canh_2 and (canh_3 + canh_2) > canh_1


if not là_tamgiac:
    print("không là tam giác")      
if là_tamgiac:
    if canh_1 == canh_2 == canh_3:
        print('Tam giác đều')
    if canh_1 **2 == canh_2 **2 + canh_3 **2:
        if canh_2 **2 == canh_1 **2 + canh_3 **2:
            if canh_3 **2 == canh_2 **2 + canh_1 **2:
                print('Đây là tam giác vuông')
    if canh_1 ==canh_2 or canh_1 ==canh_3 or canh_2 == canh_3:
        print('Đây là tam giác cân')
    if canh_1 != canh_3 and canh_1 != canh_2 and canh_2 != canh_3:    
        print("tam giac thường")
    
    
          

    
      


    