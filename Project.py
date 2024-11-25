def find_cargo():
    positions = [0, 0, 0]
    weight = [0, 0, 0] 
    total_weight = 0
    total_cargo = 0
    while total_weight != 713;
          print("Enter 3 kilometrs and corresponding weights for the 3 cargo boxes:")
          for i in range(3):
              positions[i] = int(input(f"Enter the distance (km) for box {i+1}: "))
              weights[i] = int(input(f"Enter the weight for box {i+1}: "))
          print("Enter 3 kilometrs to check where the cargo: ")
          km_inputs = [int(input(f"Enter kilometer mark {i+1}: ")) for i in range(3)]
          total_weight = 0
          total_cargo = 0
          for km in km_inputs:
              if km in positions:
                  index = positions.index(km)
                  total_weight += weights[index]
                  total_cargo += 1
          if total_cargo == 3 and total_weight == 713:
              print(f"Cargo found!")
              break
          else:
              print("Cargo not found")
find_cargo()
              
              
    
    





