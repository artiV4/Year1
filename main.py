import cv2, sys, time, numpy

cap = cv2.VideoCapture(0)
if (cap.isOpened()== False):
    print("broken camera")

ret, frame = cap.read()

inp =4 #which mode to use, all have similar output but use different masks or value ranges

#1-3 Transform input by using RED input as BLUE output and BLUE as RED with amplified colours using masking
# 4 removes green from input
if(inp ==1):
    blue = numpy.full(frame.shape, [255,0,0], dtype=numpy.uint8)
    green = numpy.full(frame.shape, [0,255,0], dtype=numpy.uint8)
    red =numpy.full(frame.shape, [0,0,255], dtype=numpy.uint8)




    while (1):
        ret, frame = cap.read()

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_blue = numpy.array([125,0,0])
        upper_blue = numpy.array([255,125,125])
        lower_green = numpy.array([0,125,0])
        upper_green = numpy.array([125,255,125])
        lower_red = numpy.array([0,0,125])
        upper_red = numpy.array([125,125,255])

        blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
        green_mask = cv2.inRange(hsv, lower_green, upper_green)
        red_mask = cv2.inRange(hsv, lower_red, upper_red)

        blue_result = cv2.bitwise_and(blue, blue, mask=blue_mask)
        green_result = cv2.bitwise_and(green, green, mask=green_mask)
        red_result = cv2.bitwise_and(red, red, mask=red_mask)

        bg = cv2.bitwise_or(blue_result,green_result)
        bgr = cv2.bitwise_or(bg,red_result)
        # bgr = cv2.bitwise_or(bg,red_result)
        # final = cv2.merge([blue_result,green_result,red_result])
        cv2.imshow('frame', frame)
        cv2.imshow('blue mask', blue_mask)
        cv2.imshow('blue result',blue_result)
        cv2.imshow('green mask', green_mask)
        cv2.imshow('green result',green_result)
        cv2.imshow('red mask', red_mask)
        cv2.imshow('red result',red_result)
        cv2.imshow('bgr',bgr)
        if cv2.waitKey(1)==27:
            break
    cv2.destroyAllWindows()
    cap.release()

elif (inp==2): #amplify RGB colours to closest of R, G, B, middle or very mixed is black, uses masking

    blue = numpy.full(frame.shape, [255,0,0], dtype=numpy.uint8)
    green = numpy.full(frame.shape, [0,255,0], dtype=numpy.uint8)
    red =numpy.full(frame.shape, [0,0,255], dtype=numpy.uint8)



    while (1):
        ret, frame = cap.read()

        lower_blue = numpy.array([125,0,0])
        upper_blue = numpy.array([255,125,125])
        lower_green = numpy.array([0,125,0])
        upper_green = numpy.array([125,255,125])
        lower_red = numpy.array([0,0,125])
        upper_red = numpy.array([125,125,255])

        blue_mask = cv2.inRange(frame, lower_blue, upper_blue)
        green_mask = cv2.inRange(frame, lower_green, upper_green)
        red_mask = cv2.inRange(frame, lower_red, upper_red)

        blue_result = cv2.bitwise_and(blue, blue, mask=blue_mask)
        green_result = cv2.bitwise_and(green, green, mask=green_mask)
        red_result = cv2.bitwise_and(red, red, mask=red_mask)

        bg = cv2.bitwise_or(blue_result,green_result)
        bgr = cv2.bitwise_or(bg,red_result)
        # bgr = cv2.bitwise_or(bg,red_result)
        # final = cv2.merge([blue_result,green_result,red_result])
        cv2.imshow('frame', frame)
        cv2.imshow('blue mask', blue_mask)
        cv2.imshow('blue result',blue_result)
        cv2.imshow('green mask', green_mask)
        cv2.imshow('green result',green_result)
        cv2.imshow('red mask', red_mask)
        cv2.imshow('red result',red_result)
        cv2.imshow('bgr',bgr)
        if cv2.waitKey(1)==27:
            break

    cv2.destroyAllWindows()
    cap.release()
elif (inp==3):
    blue = numpy.full(frame.shape, [255,0,0], dtype=numpy.uint8)
    green = numpy.full(frame.shape, [0,255,0], dtype=numpy.uint8)
    red =numpy.full(frame.shape, [0,0,255], dtype=numpy.uint8)




    while (1):
        ret, frame = cap.read()

        b,g,r = cv2.split(frame)

        lower = 70
        upper = 100

        blue_mask = cv2.inRange(b, lower, upper)
        green_mask = cv2.inRange(g, lower, upper)
        red_mask = cv2.inRange(r, lower, upper)

        blue_result = cv2.bitwise_and(b, b, mask=blue_mask)
        green_result = cv2.bitwise_and(g, g, mask=green_mask)
        red_result = cv2.bitwise_and(r, r, mask=red_mask)

        # bg = cv2.bitwise_or(blue_result,green_result)
        # bgr = cv2.bitwise_or(bg,red_result)
        bgr = cv2.merge([blue_result,green_result,red_result])
        # bgr = cv2.bitwise_or(bg,red_result)
        # final = cv2.merge([blue_result,green_result,red_result])
        cv2.imshow('frame', frame)
        cv2.imshow('blue mask', blue_mask)
        cv2.imshow('blue result',blue_result)
        cv2.imshow('green mask', green_mask)
        cv2.imshow('green result',green_result)
        cv2.imshow('red mask', red_mask)
        cv2.imshow('red result',red_result)
        cv2.imshow('bgr',bgr)
        if cv2.waitKey(1)==27:
            break
    cv2.destroyAllWindows()
    cap.release()
elif (inp==4): #Displays input without green
    blue = numpy.full(frame.shape, [255,0,0], dtype=numpy.uint8)
    green = numpy.full(frame.shape, [0,255,0], dtype=numpy.uint8)
    red =numpy.full(frame.shape, [0,0,255], dtype=numpy.uint8)
    x,y,z = cv2.split(frame)
    empty = numpy.full(x.shape,[0],dtype=numpy.uint8)



    while (1):
        ret, frame = cap.read()
        b,g,r=cv2.split(frame)

        grb = cv2.merge([b,empty,r])

        cv2.imshow('br',grb)
        cv2.imshow('normal',frame)

        if cv2.waitKey(1)==27:
            break


