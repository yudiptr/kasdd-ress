import math
def reg_linier():
    w0 = 2
    w1 = -1
    w2 = 1

    x1_1 = 1
    x1_2 = 2
    y1 = 10

    x2_1 = 2
    x2_2 = 2
    y2 = 12

    x3_1 = 6
    x3_2 = 4
    y3 = 14

    x4_1 = 8
    x4_2 = 2
    y4 = 15

    a = 0.01

    joss = 1/2 *((w0 + w1*x1_1 + w2*x1_2 - y1)**2 + (w0 + w1*x2_1 + w2*x2_2 - y2)**2 + (w0 + w1*x3_1 + w2*x3_2 - y3)**2 + (w0 + w1*x4_1 + w2*x4_2 - y4)**2)
    
    print("Joss :", joss)

    max_iter = 1
    while ( max_iter != 0 ):
        w0_temp = ((w0 + w1*x1_1 + w2*x1_2 - y1) + (w0 + w1*x2_1 + w2*x2_2 - y2) + (w0 + w1*x3_1 + w2*x3_2 - y3) + (w0 + w1*x4_1 + w2*x4_2 - y4))
        
        w1_temp = (x1_1*(w0 + w1*x1_1 + w2*x1_2 - y1) + x2_1*(w0 + w1*x2_1 + w2*x2_2 - y2) + x3_1*(w0 + w1*x3_1 + w2*x3_2 - y3) + x4_1*(w0 + w1*x4_1 + w2*x4_2 - y4))
        
        w2_temp = (x1_2*(w0 + w1*x1_1 + w2*x1_2 - y1) + x2_2*(w0 + w1*x2_1 + w2*x2_2 - y2) + x3_2*(w0 + w1*x3_1 + w2*x3_2 - y3) + x4_2*(w0 + w1*x4_1 + w2*x4_2 - y4))

        w0 = w0 - a * w0_temp
        w1 = w1 - a * w1_temp
        w2 = w2 - a * w2_temp

        max_iter -= 1

    joss = 1/2 *((w0 + w1*x1_1 + w2*x1_2 - y1)**2 + (w0 + w1*x2_1 + w2*x2_2 - y2)**2 + (w0 + w1*x3_1 + w2*x3_2 - y3)**2 + (w0 + w1*x4_1 + w2*x4_2 - y4)**2)
    
    print("Joss :", joss)
    print(w0)
    print(w1)
    print(w2)

reg_linier()


def logistic_regression():
    w0 = -2
    w1 = -1
    w2 = 0
    lr = 0.01

    x1 = [2, -1, 3 ,1]
    x2 = [1, 2, 3, 1]
    Yi = [1, 0, 0, 1]
    len = 4

    counter = 0
    while (counter < 1) :
        gradw0 = 0
        for i in range(len):
            gradw0 += (Yi[i] - ( 1 / (1+math.e**-(w0 + w1*(x1[i]) + w2*(x2[i])   ))))

        gradw1 = 0
        for i in range(len):
            gradw1 += (Yi[i] - ( 1/ (1+math.e**-(w0 + w1*(x1[i]) + w2*(x2[i])   )))) * x1[i]


        gradw2 = 0
        for i in range(len):
            gradw2 += (Yi[i] - ( 1/ (1+math.e**-(w0 + w1*(x1[i]) + w2*(x2[i])   )))) * x2[i]    
         

        counter += 1
        w0 = w0 + lr*gradw0
        w1 = w1 + lr*gradw1
        w2 = w2 + lr*gradw2
        print('iterasi ke :', counter)
        print('gradw0 :', gradw0)
        print('gradw1 :', gradw1)
        print('gradw2 :', gradw2)
        print('updated w0:' , w0)
        print('updated w1', w1)
        print('updated w2', w2)


def simplified_logistic():
    w0 = -2
    w1 = -1
    w2 = 0
    lr = 0.01


    x1 = [2, -1, 3 ,1]
    x2 = [1, 2, 3, 1]
    Pi = [0.018, 0.269, 0.007, 0.047]
    Yi = [1, 0, 0, 1]
    len = 4

    counter = 0
    while (counter < 1) :
        gradw0 = 0
        for i in range(len):
            gradw0 += (Yi[i] - Pi[i])

        gradw1 = 0
        for i in range(len):
            gradw1 += (Yi[i] - Pi[i]) * x1[i]


        gradw2 = 0
        for i in range(len):
            gradw2 += (Yi[i] - Pi[i]) * x2[i]    
         

        counter += 1
        w0 = w0 + lr*gradw0
        w1 = w1 + lr*gradw1
        w2 = w2 + lr*gradw2
        print('iterasi ke :', counter)
        print('gradw0 :', gradw0)
        print('gradw1 :', gradw1)
        print('gradw2 :', gradw2)
        print('updated w0:' , w0)
        print('updated w1', w1)
        print('updated w2', w2)

logistic_regression()
simplified_logistic()