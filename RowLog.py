
import time
from PyRow.ErgStats import ErgStats
from Storage.SQLiteStorage import SQLiteStorage

def main():
    initialized = False
    storage = None

    # Init the Concept2
    #
    #ErgStats.connectToErg()
    
    #this waits for workouts to start, then stores them into a SQLite DB
    print("Waiting for workout to start...")
    while True:
        try:
            isActive = ErgStats.isWorkoutActive()
        except:
            print("Connecting to Ergometer...")
            ErgStats.connectToErg()
            time.sleep(1)
            continue
    
        if not isActive:
            if initialized: #this checks if workout was active before
                print("Workout ended...")
                ErgStats.resetStatistics()
                storage = None
                initialized = False
        else:
            if not initialized:
                print("Workout started...")
                storage = SQLiteStorage()
                initialized = True
            ErgStats.update()
            storage.storeState(ErgStats.time)

if __name__ == "__main__":
    main()