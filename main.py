counts={}
def count_batteries_by_health(present_capacities):
  h=e=f=0
  for i in present_capacities:
    soh=100*i/120
    if soh>=80 and soh<=100:
      h+=1
    elif soh>=60 and soh<80:
      e+=1
    elif soh<60:
      f+=1
  counts={"healthy":h,"exchange":e,"failed":f}

  
  


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities =map(int,input().split())
  count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  assert(counts["healthy"] == 1)
  assert(counts["exchange"] ==2)
  assert(counts["failed"] == 2)
 
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
