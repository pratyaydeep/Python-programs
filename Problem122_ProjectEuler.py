'''
Y tuong la ta se dung backtrack de quet het cac truong hop. (mathblog)
Ta se tao 1 duong di co ban la 1-2-..-2^n sau do quay nguoc lai tung nut 2^(n-1) va them tat ca cac so truoc no vao 
sao cho so moi nhan duoc ko qua limit va dem so buoc it nhat.
Ta se luu tru lai cach di va so buoc it nhat
'''
time = [11 for x in range(200)] # So buoc it nhat can
path = [0 for x in range(13)] # Luu tru cach di
limit = 200

def generate(number, step):
    if number > limit or step > time[number-1]:
        pass
    else:
        time[number-1] = step # So buoc de tiep can number la step
        path[step] = number # Them number vao duong di bat dau tu 1
        for i in range(step+1):
                generate(number + path[i], step + 1) # Them so x vao duong di va tang so buoc len 1

generate(1, 0)  # Bat dau voi 1 va so lan de dat la 0
print (time)
print (sum(time))

