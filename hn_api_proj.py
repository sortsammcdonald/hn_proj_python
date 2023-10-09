import requests
            
class Gen_URLs():
    def __init__(self, template, target):
        self.template = template
        self.target = target
    def amend_url(self, snippet):
        return self.template.replace(self.target, snippet)

class HN_User_Attributes(Gen_URLs):
    def __init__(self, template, target, key):
        super().__init__(template, target)
        self.key = key

    def user_req(self):
        user_name = input("Enter your user name ")
        return user_name
    
    def gen_json(self, snippet):
        url = self.amend_url(snippet)
        get_json = requests.get(url)
        if get_json.status_code == 200:
            return get_json.json()
        else:
            print(f"Error: Received status code {get_json.status_code}")
            return None
            
    def extract_element(self, snippet):
        vals = self.gen_json(snippet)
        if vals is not None:
            if self.key in vals:
                return vals[self.key]
            else:
                print(f"Key '{self.key}' not found in JSON data.")
        else:
            return []




def main():
    hn_user_attributes = HN_User_Attributes(
        template = "https://hacker-news.firebaseio.com/v0/user/<user>.json?print=pretty",
        target = "<user>",
        key = "submitted"
    )
    snippet =  hn_user_attributes.user_req()

    data = hn_user_attributes.gen_json(snippet)
    section = hn_user_attributes.extract_element(snippet)
    subsection = section[0:9]
    new_urls = Gen_URLs(
        template=  "https://news.ycombinator.com/item?id=<item>",
        target= "<item>"
    )
    
    
    if data is not None:
        print("Received JSON data:")
        print(type(data))
        for i in subsection:
            print(new_urls.amend_url(snippet = str(i)))
    else:
            print("Failed to retrieve JSON data.")


if __name__ == '__main__':
    main()