import requests

def user_req():
    user_name = input("Enter your user name ")
    return user_name

def amend_url(template, target, snippet):
    updated = template.replace(target, snippet)
    return updated

def gen_json(template, target, snippet):
    url = amend_url(template, target, snippet)
    get_json = requests.get(url)
    if get_json.status_code == 200:
        return get_json.json()
    else:
        print(f"Error: Received status code {get_json.status_code}")
        return None
        

def extract_element(template, target, snippet, key):
    vals = gen_json(template, target, snippet)

    if vals is not None:
        if key in vals:
            return vals[key]
        else:
            print(f"Key '{key}' not found in JSON data.")
    else:
        return None
#def gen_url(template, key):
#    vals = extract_element(template, key)
#    for i in vals:
#        amend_url

def main():
    
    template = "https://hacker-news.firebaseio.com/v0/user/<user>.json?print=pretty"
    target = "<user>"
    key = "submitted"

    snippet =  user_req()

    data = gen_json(template, target, snippet)

    section = extract_element(template, target, snippet, key)
    
    if data is not None:
        print("Received JSON data:")
        print(data)
        print("Extract is")
        print(section)
    else:
        print("Failed to retrieve JSON data.")


if __name__ == '__main__':

    main()