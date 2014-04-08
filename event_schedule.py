# An Optimal Event Scheduling Algorithm

__author__ = "Kevin Aloysius"
def event_sort(array):
	#Sort the meetingStart the meeting with the early finishing time
	meeting_list = sorted(array, key=early_finish)
	return meeting_list

def event_schedule(array):
	meeting_list = event_sort(array)
	first_meeting = meeting_list[0]
	meeting_list.remove(first_meeting)
	for each_meeting in meeting_list:
			if (each_meeting[0] < first_meeting[1]) or (each_meeting[0] < first_meeting[0]) or (each_meeting[1] > first_meeting[1]):
				meeting_list.remove(each_meeting)
	meeting_list.insert(0,first_meeting)
	print meeting_list
		
def early_finish(array):
	return array[1]


def main():
	start_end_time = [[15.30,16.30], [4.30,5.30], [6.00,7.00], [8.00,9.00], [6.30,7.30], [8.30,9.30], [4.00,6.00]]
	event_schedule(start_end_time)

if __name__ == "__main__":
	main()