# Ta co cong thuc so thu j vong i la : 3i(i-1) + j + 1 j=1-6i trong do 1 thuoc vong 0
# De thay vong i ta chi can xet cac so thu 1, 1+i, 1 +2i, 1+3i, 1+4i, 1+5i, 6i
# Vi cac so khac chua cac hieu co dang (1,1,a,a+1,b,b+1),a,b>6 nen co ko qua 2 so nguyen to
# (j,i) ki hieu la tap co so ke so thu j vong i
# (1,i) = {1,6(i-1),6i-1,6i,6i+1,12i+5} check = {6i-1,6i+1,12i+5}
# (1+i,i) = {1,1,6i-5,6i,6i+1,6i+2} loai
# (1+2i,i) = {1,1,6i-4,6i+1,6i+2,6i+3} loai
# (1+3i,i) = {1,1,6i-3,6i+2,6i+3,6i+4} loai
# (1+4i,i) = {1,1,6i-2,6i+3,6i+4,6i+5} loai
# (1+5i,i) = {1,1,6i-1,6i+4,6i+5,6i+6} loai
# (6i,i) = {1,6i-1,6i,6i+5,6i+6,12i-7} check = {6i-1,6i+5,12i-7}
def prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2,int(n ** 0.5)+1):
            if n % i == 0:
                return False
                break
        else:
            return True

PD3 = [1,2]
i = 2
while len(PD3) < 2010:
    if prime(6*i-1) and prime(6*i+1) and prime(12*i+5):
        PD3.append(3*i*(i-1)+1 + 1)
    if prime(6*i-1) and prime(6*i+5) and prime(12*i-7):
        PD3.append(3*i*(i-1)+6*i +1)

    i += 1

print (PD3[1999])