weekdaysInput = {
  "monday": 0,
  "tuesday": 1,
  "wednesday": 2,
  "thursday": 3,
  "friday": 4,
  "saturday": 5,
  "sunday": 6,
}

weekdaysOutput = [
  "Monday",
  "Tuesday",
  "Wednesday",
  "Thursday",
  "Friday",
  "Saturday",
  "Sunday",
]

def add_time(start, duration, weekday = None):
  start = process_input(start)
  duration = split_time(duration)

  day_counter = 0;
  if weekday != None:
    display_weekday = True
    weekday = weekdaysInput[weekday.lower()]
  else:
    weekday = 0
    display_weekday = False

  start[0] += duration[0]
  start[1] += duration[1]

  while(start[1] >= 60):
    start[1] -= 60
    start[0] += 1
  
  while(start[0] >= 24):
    start[0] -= 24
    weekday += 1
    day_counter += 1

  while(weekday > 6):
    weekday -= 7

  if start[0] == 0:
    start[0] = 12
    am_pm = "AM"
  elif start[0] == 12:
    am_pm = "PM"
  elif start[0] > 12:
    am_pm = "PM"
    start[0] -= 12
  else:
    am_pm = "AM"

  output = str(start[0]) + ":" + format_number(start[1]) + " " + am_pm

  if display_weekday:
    output += ", " + weekdaysOutput[weekday]

  if day_counter > 0:
    if(day_counter == 1):
      weekdayOut = "next day"
    else:
      weekdayOut = str(day_counter) + " days later"
    output += " (" + weekdayOut + ")"

  return output


def format_number(number):
  out = ""
  if len(str(number)) < 2:
    out += "0"
  out += str(number)
  return out


def process_input(start):
  splits = start.split(" ")
  
  start_time = split_time(splits[0])
  am_pm = splits[1]

  if(am_pm == "PM"):
    start_time[0] += 12

  return start_time

def split_time(time):
  splits = time.split(":")
  return [int(splits[0]), int(splits[1])]