#Sort the meeting time based on the starting time
#Iterate through the values and check
#   if the end time is greater than starting time of the next meeting then
#       merge it and update the end time to be max of 2 end times
#   else
#       mark it as a separate meeting


class Interval:
    def __init__(self, s, e):
        self.start = s
        self.end = e


def merged_meetings(interval_meetings):
    interval_meetings = sort_start_time(interval_meetings)
    final_merged_meetings = []
    start_time = interval_meetings[0].start
    end_time = interval_meetings[0].end

    for i in range(1, len(interval_meetings)):
        current_start_time = interval_meetings[i].start
        if end_time >= current_start_time:
            end_time = max(end_time, interval_meetings[i].end)
        else:
            final_merged_meetings.append(Interval(start_time, end_time))
            start_time = interval_meetings[i].start
            end_time = interval_meetings[i].end
    #merge the final timings
    final_merged_meetings.append(Interval(start_time, end_time))
    #display
    for item in final_merged_meetings:
        print(item.start, item.end)




def sort_start_time(meeting_timings):
    return sorted(meeting_timings, key=lambda x: x.start)

merged_meetings([Interval(0, 1), Interval(3, 5), Interval(4, 8), Interval(10, 12), Interval(9, 10)])


