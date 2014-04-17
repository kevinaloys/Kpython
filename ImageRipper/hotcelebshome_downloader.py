import httplib
import sys
import urllib
import os
import random
#If a particular Location exists
def exists(site,path):
	connection = httplib.HTTPConnection(site)
	connection.request('HEAD',path)
	response = connection.getresponse()
	return response.status


def pull_image(actress_name,year,month):
	months = {	'01':'Janaury',
				'02':'February',
				'03':'March',
				'04':'April',
				'05':'May',
				'06':'June',
				'07':'July',
				'08':'August',
				'09':'September',
				'10':'October',
				'11':'November',
				'12':'December'		}
	image_url_list = []
	site = "www.hotcelebshome.com:80"
	location = '/wp-content/uploads/'+year+'/'+month+'/'+actress_name
	if os.path.isdir(actress_name):
		os.chdir(actress_name)
	else:
		os.mkdir(actress_name)
		os.chdir(actress_name)
	if os.path.isdir(months[month]):
		os.chdir(months[month])
	else:
		os.mkdir(months[month])
		os.chdir(months[month])
	for i in range(1,200):
		extension ='-'+str(i)+'.jpg'
		path = location + extension
		if exists(site, path) != 404:
			print site+path
			image_url_list.append(site+path)
		extension = None
	count = 1	
	for url in image_url_list:
		urllib.urlretrieve ('http://'+url, str(count)+'.jpg')
		print "Success Fetching",actress_name,"image",count
		count += 1
	print image_url_list
		

def main():
	if len(sys.argv) !=4:
		print "usage: actress-name year month"
		sys.exit(1)
	actress = str(sys.argv[1])
	year = str(sys.argv[2])
	month = str(sys.argv[3])
	pull_image(actress,year,month)


if __name__ == '__main__':
  main()