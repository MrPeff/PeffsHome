import random
import logging

logging.basicConfig(level=logging.DEBUG)

boxes = list(range(100))
logging.debug(boxes)
SuccessCount = 0
NumberOfRuns = 10000
for TestRun in range(NumberOfRuns):
    random.shuffle(boxes)
    logging.debug(boxes)
    #-------------------------------------------------------
    for idx1 in range(100):
        found = False
        Start = boxes[idx1]
        #logging.debug("idx ", idx1, ": ", Start, sep='',end=' ')
        #-------------------------------------------------------
        for idx2 in range(50):
            if (idx1 == Start):
                logging.debug("Hittat")
                found = True
            else:
                Start = boxes[Start]
                logging.debug(Start, sep=' ', end=' ')
            if found:
                break
        #-------------------------------------------------------
        if not found:
            logging.debug("Det sket sig!")
            break
    #-------------------------------------------------------
    if found:
        SuccessCount += 1
print("Rate: ", SuccessCount/NumberOfRuns)






