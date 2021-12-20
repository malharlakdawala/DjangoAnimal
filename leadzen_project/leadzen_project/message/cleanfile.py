import json

import requests
import re


class Cleanstring:
    def __init__(self):
        pass

    def clean(self,sentence):
        cleantext = self.clean_data(sentence)
        proper_text = self.write_better_sentences(cleantext)
        return proper_text

    def clean_data(self, sentence):
        sentence = sentence.lower()
        CLEANR = re.compile(
            '<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')  # remove html tags and &af special characters
        sentence = re.sub(CLEANR, ' ', sentence)
        sentence = re.sub(r'\r\n', ' ', sentence)
        sentence = re.sub(r'\n', ' ', sentence)
        sentence = sentence.replace('\n', ' ')
        sentence = sentence.replace('\r', ' ')
        sentence = sentence.replace('\\ r \\', ' ')
        sentence = sentence.replace('\\', ' ')
        sentence = re.sub(r'&nbsp', ' ', sentence)
        sentence = re.sub(r'\r', ' ', sentence)
        sentence = re.sub(r'\\ r \\', ' ', sentence)
        sentence = re.sub(r'we', ' the company', sentence)
        sentence = re.sub(r'us', ' they', sentence)
        sentence = re.sub(r'our', ' their', sentence)
        cleantext = re.sub(r' +', ' ', sentence)  # trims out all extra spaces in the string
        return cleantext

    def write_better_sentences(self, sentence):
        url = "https://textrewrite-com.p.rapidapi.com/api.php"
        querystring = {"text": sentence}
        headers = {
            'x-rapidapi-host': "textrewrite-com.p.rapidapi.com",
            'x-rapidapi-key': "d6a2e73179mshfa5a8a3fa183d90p1a1499jsn14c184f39007"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        string_response = response.text
        json_response = json.loads(string_response)
        json_response = json_response["text"]
        return json_response

#Cleanstring("""we are hc trader. we are working with  all kinds of SANITARY HARDWARE ELECTRICALS Complite range of bulding concutration. and many more Our company is tradeing company""")
# Cleanstring("""&nbspHello there&lt;testdata&gt; <div> <h1>Title</h1> <p>A long \r\n text........ \n </p> <a href=""> a link </a></div>""")
