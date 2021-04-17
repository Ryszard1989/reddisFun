#TODO:
#Unit tests.
#retrieve top score
#Implement reddis for storage
#retrieve score from reddis
#Sonarcube coverage
#Docker
#Try beat reddis with different message sizes
#Play with probabilistic versus regular query.

import redis

def main():
    r = redis.Redis()
    scores = makeSomeData()
    r.mset(scores)
    print(r.get("Bahamas"))
    print(r.get("Claude"))

    #data = makeSomeData()
    #store data in reddis
    #get data from reddis
    #for d,s in data.items():
    #    print (str(d) + " scored " + str(s))

def makeSomeData():
    scores = {"Rysz":9000, "Claude":4200, "Abe":30,"Bob":1400,"Charlie":1900, "Derek":500}
    return scores


if __name__ == "__main__":
    main()
