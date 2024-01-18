import math
def grad_ascent():
    w0 = 2
    w1 = 3
    lr = 0.21

    psd = [3.8, 3.4, 2.9, 2.8, 2.7, 2.1, 1.6, 2.5, 2.0, 1.7, 1.4, 1.2,  0.9, 0.8]
    Yi = [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
    len = 14

    counter = 0
    while (counter < 10000) :
        gradw0 = 0
        for i in range(len):
            gradw0 += (Yi[i] - ( 1 / (1+math.e**-(w0+w1*(psd[i])))))

        gradw1 = 0
        for i in range(len):
            gradw1 += (Yi[i] - ( 1/ (1+math.e**-(w0+w1*(psd[i]))))) * psd[i]
         

        counter += 1
        w0 = w0 + lr*gradw0
        w1 = w1 + lr*gradw1
        print('iterasi ke :', counter)
        print('gradw0 :', gradw0)
        print('gradw1 :', gradw1)
        print('updated w0:' , w0)
        print('updated w1', w1)


grad_ascent()