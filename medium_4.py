
import os


def muchiko_filter(data, window_size=3):
   smoothed_data = []
   # Loop through the data, ensuring we only go as far as a full window allows
   for i in range(len(data) - window_size + 1):
       window = data[i: i + window_size]
       # Calculate the average and round it
       window_average = sum(window) / window_size
       smoothed_data.append(round(window_average, 2))
   return smoothed_data




def sanchiko_filter(data, window_size=3):
   noise_removed_data = []
   for i in range(len(data) - window_size + 1):
       window = data[i: i + window_size]
       # Sort the window to find the median
       sorted_window = sorted(window)
       mid_index = window_size // 2
       median_value = sorted_window[mid_index]
       noise_removed_data.append(median_value)
   return noise_removed_data




def hybrid_filter(data, window_size=3):
   """
   Hybrid Filter: Applies Sanchiko (Median) to remove extreme wild spikes,
   then applies Muchiko (Average) to the result to smooth the underlying signal.
   """
   # Step 1: Remove extreme spikes
   median_filtered = sanchiko_filter(data, window_size)


   # Step 2: Smooth the resulting stable data
   # Applying a second filter reduces the array size further
   final_smoothed = muchiko_filter(median_filtered, window_size)
   return final_smoothed


if __name__ == "__main__":
   # Creating a dummy log.txt for the sake of the demonstration
   with open("log.txt", "w") as f:
       # A simulated signal with stable reading around 10, but massive wild spikes (100, -50)
       f.write("10, 11, 100, 9, 10, -50, 11, 10, 12")


   print("Reading chaotic sensor data from log.txt...")
   with open("log.txt", "r") as f:
       raw_data_string = f.read()
       sensor_readings = [int(x.strip()) for x in raw_data_string.split(",")]


   print(f"Raw Sensor Readings: {sensor_readings}\n")


   print(f"Applying Muchiko (Average): {muchiko_filter(sensor_readings, 3)}")
   print(f"Applying Sanchiko (Median): {sanchiko_filter(sensor_readings, 3)}")
   print(f"Applying Hybrid Filter:     {hybrid_filter(sensor_readings, 3)}")
