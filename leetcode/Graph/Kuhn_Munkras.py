import sys

def KM(X, Y, weight):
    lx, ly, matching = {}, {}, {} # use dict, X/Y can be label
    for x in X:
        lx[x] = max(weight[x].values())
        matching[x] = -1
    for y in Y:
        ly[y] = 0
        matching[y] = -1
    
    def findpath(x, visitX, visitY, slack): # extend from hungarian
        visitX.add(x)
        tempDelta = 0

        for y in Y:
            if y in visitY: continue
            tempDelta = lx[x] + ly[y] - weight[x].get(y, 0)
            if tempDelta == 0:  # feasible edge
                visitY.add(y)
                if matching[y] == -1 or findpath(matching[y], visitX, visitY, slack):
                    matching[y] = x
                    matching[x] = y
                    return True
            elif slack[y] > tempDelta: # x in agumenting path but y not, pre-calculate slack
                slack[y] = tempDelta
        return False

    for x in X:
        slack = {y:sys.maxint for y in Y}
        while True:
            visitX = set()
            visitY = set()
            if findpath(x, visitX, visitY, slack):
                break
            else:
                delta = sys.maxint
                for j, s in filter(lambda (j,s): j not in visitY, slack.iteritems()):
                        delta = min(delta, s)
                
                for x in filter(lambda x: x in visitX, X):
                    lx[x] -= delta
                for y in Y:
                    if y in visitY:
                        ly[y] += delta
                    else:
                        slack[y] -= delta  
                        # slack[j] = min(lx[i] + ly[j] - w[i][j])
                        # j is not in visitY, no change on ly[j], but lx[i] -= delta
                        
    return matching


weight = ({0:{3:5,4:10,5:15,6:10}, 1:{3:5,4:10}, 2:{3:10,5:20,6:10}})
print KM([0,1,2], [3,4,5,6], weight)
