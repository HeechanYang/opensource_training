import time

def get_timestamp():
    now = int((time.time()) * 1000)
    return now

def til_next_millis(last):
    timestamp = get_timestamp()
    while (timestamp <= last):
        timestamp = get_timestamp()

    return timestamp

def shour_url(url):
	shared_uri = "https://seek.er/"
	shorted_uri = ""
	
	# parsing
	start_idx = url.find("://") + 2

	# loop for length of input url
	while start_idx < len(url):
		new_char = 0

		# add ascii value of 10 character
		for j in range(start_idx, start_idx+10):
			if (start_idx >= len(url))
				break
			new_char += ord(url[j])

		new_char = new_char % 128

		# if modulo result is in A-z, add it to shorted uri
		if (new_char >= 65 and new_char <= 122):
			shorted_uri += chr(new_char)
	
	# find whether there is same shorted_uri in DB or not
	# if exist, count same shorted_uri and add count to shorted_uri
	# add shared_uri and shorted uri
	shorted_uri = shared_uri + shorted_uri
	# save mapping in DB
	return shorted_uri

