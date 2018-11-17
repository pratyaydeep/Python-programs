# Quy hoach dong theo phan tich 1 so thanh tich cua cac so tu nhien va sap xep chung theo thu tu tang dan (co the bang nhau)

p_max = 2 * 12000
def product_sum(p, s, num, cur_max): # p la tich, s la tong, num la so thua so, start la gia tri xuat phat de them,cur_max la phan tu lon nhat hien tai
    k = p - s + num # p la mot so product sum cua k so
    if k <= 12000 :
        if p < n[k]:
            n[k] = p
        for i in range(cur_max, p_max // p ): #Them phan tu sao cho tich ko vuot qua p_max va phan tu do phai ko be hon cur_max vi ta quy hoach dong nen ko can tinh lai cac gia tri lap :v.
            product_sum(p*i, s+i, num+1, i)

n = [2*i for i in range(12001)] # Chu y so min product_sum cua k so luon <= 2k
product_sum(1,1,1,2)
print (sum(set(n[2:]))) # dung set de loai cac phan tu trung nhau.

