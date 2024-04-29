def main():
  AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']
  while True:
      print("********************************")
      print("AutoCountry Vehicle Finder v0.2")
      print("********************************")
      print("Please Enter the following number below from the following menu:")
      print("1. PRINT all Authorized Vehicles")
      print("2. SEARCH for Authorized Vehicle")
      print("3. Exit")
      print("********************************")
      choice = input("Enter Choice (1-3): ")
      if choice == "1":
          print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
          for vehicle in AllowedVehiclesList:
              print(vehicle)
      elif choice == "2":
          search_query = input("Please Enter the full Vehicle name: ")
          if search_query in AllowedVehiclesList:
              print(f"{search_query} is an authorized vehicle")
          else:
              print(f"{search_query} is not an authorized vehicle, if you received this in error please check the spelling and try again")
      elif choice == "3":
          print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
          break

if __name__ == "__main__":
  main()
