while True:
 def time_in_words(s):
    d = {"00": " O'clock", "15": "Quarter", "30": " thiry","45":"Quarter of", "1": "one", "2": " two", "3": " three", "4": " four",
         " 5": " five",
         "6": " six", "7": " seven", "8": " eight", "9": " nine", "10": " ten", "11": "eleven", "12": "twelve ",
         "13": " thirteen", "14": " fourteen", "16": " sixteen", "17": "sventeen", "18": "eighteen", "19": " nineteen",
         "20": "twenty", }

    all_hours = [i for i in range(1, 13)]
    all_minutes = [i for i in range(0, 60)]
    hour, minutes = s.split(":")

    default = "invalid time"
    if int(hour) not in all_hours:
        return default
    if minutes == "00":
       if hour not in d:
         return default
       return "{0}{1}".format(hour, d[minutes])
    if int(minutes) not in all_minutes:
        return default
    if minutes == "30":
        return "{0}{1}".format(d[hour], d[minutes])

    m = int(minutes)
    filler_string = " past "
    if int(m) > 30:
        m = 60 - m
        filler_string = " to "
        hour = int(hour)
        if hour == 12:
            hour = 1
        else:
            hour += 1
        hour = str(hour)

    if m == 15:
        return "{0}{1}{2}".format(d[str(m)], filler_string, d[hour])

    minute_string = " minutes "
    if abs(m) == 1:
        minute_string = " minute "

    mstring = ""
    if m not in d:
        if m > 20 and m < 30:
            r = m % 10
            mstring = "twenty" + d[str(r)]
        else:
            mstring = d[str(m)]
    return "{0}{1}{2}{3}".format(mstring, minute_string, filler_string, d[hour])

 print(time_in_words(input("Enter the time you want in hr:min format here: ")))
 opt= (input("enter 'N' to stop: "))
 if opt=="N":
  break
