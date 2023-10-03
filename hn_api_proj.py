import requests

class HN_User_Samples:
    def __init__(self, template) -> None:
        self.template = template

    def user_req(self):
        user_name = input("Enter your user name ")
        return user_name

    def amend_url(self, target, snippet):
        updated = self.template.replace(target, snippet)
        return updated

    def gen_json(self, target, snippet):
        url = self.amend_url(self.template, target, snippet)
        get_json = requests.get(url)
        if get_json.status_code == 200:
            return get_json.json()
        else:
            print(f"Error: Received status code {get_json.status_code}")
            return None
            

    def extract_element(self, target, snippet, key):
        vals = self.gen_json(self.template, target, snippet)

        if vals is not None:
            if key in vals:
                return vals[key]
            else:
                print(f"Key '{key}' not found in JSON data.")
        else:
            return None


def main():
    hn_user_samples = HN_User_Samples(template = "https://hacker-news.firebaseio.com/v0/user/<user>.json?print=pretty")

    
    target = "<user>"
    key = "submitted"

    snippet =  hn_user_samples.user_req()

    data = hn_user_samples.gen_json(target, snippet)

    section = hn_user_samples.extract_element(target, snippet, key)
    
    if data is not None:
        print("Received JSON data:")
        print(data)
        print("Extract is")
        print(section )
    else:
        print("Failed to retrieve JSON data.")


if __name__ == '__main__':

    main()