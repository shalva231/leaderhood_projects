def count(str):
    if not str:
        return 0
    count = 0
    for i in str:
        if i.isupper:
            count+=1
    return count

'''
ყველაზე ცოტა მოხდება მაშინ როდესაც სტრინგი ცარიელია მოხდება 0 შემოწმება
ყველაზე მეტი კი n ანუ თავად სტრინგის სიგრძე
'''
