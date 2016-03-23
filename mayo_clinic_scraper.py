import mechanize


def condition_from_line():
    line =  line.strip('\t').strip(' ')
    matches = re.findall(r'href=\"(.+?)\">',line)
    return matches[0]
	

def scrape_condition_list():

	br = mechanize.Browser()
	br.set_all_readonly(False)    # allow everything to be written to
	br.set_handle_robots(False)   # ignore robots
	br.set_handle_refresh(False)  # can sometimes hang without this
	

	
	base_url = 'http://www.mayoclinic.org/diseases-conditions/index?letter='
	alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	for letter in alphabet:
		response = br.open(base_url+letter)
		lines = response.readlines()
		reading = False    
		condition_list = []
		for line in lines:
			if '<h2>A</h2></h2>' in line:
				start_reading = True

			if '</ol>' in line:
				break

			if start_reading:
				condition_list.append(condition_from_line(line))

	
	return condition_list

def scrape_symptoms_for_condition(condition):
	symptom_list = []
	return symptom_list




def scrape_all():
	results = {}
	for condition in scrape_condition_list():
		symptoms = scrape_symptoms_for_condition(condition)
		results[condition] = symptoms

print scrape_condition_list()


