import requests
from bs4 import BeautifulSoup


class HeroOfHearts:
    def __init__(self, chapter_set):
        self.chapter_set = chapter_set  # one chapter set contains 2 chapters.

    def extract(self):
        data = ''
        for page in range(1, self.chapter_set):
            chapter_from = (2 * page) - 1
            chapter_to = chapter_from + 1
            print(chapter_from, chapter_to, len(data))
            url = f"https://tales.xperimentalhamid.com/novel/hero-of-hearts/hero-of-hearts-novel-chapter-" + str(
                chapter_from).zfill(2) + "-" + str(chapter_to).zfill(2) + "/"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            soup.find("")
            found = False
            data += "<br><h1>Hero of Hearts : Chapter " + str(chapter_from) + " - " + str(chapter_to) + "</h1>\n\n"
            for e in soup.descendants:
                if e.text == 'NEXT CHAPTER':
                    break
                if e.name == 'h2' and found == False:
                    found = True
                if found:
                    if e.text not in data:
                        if 'chapter' in e.text:
                            data += "\n\n"
                        data += str(e) + '\n'
                        if 'chapter' in e.text:
                            data += "\n\n"

        adfree_data = data.replace('(adsbygoogle = window.adsbygoogle || []).push({});', '').replace('<script>',
                                                                                                     '').replace(
            '</script>', '')
        return adfree_data


if __name__ == '__main__':
    chapter_set = input("Enter Number of Chapter sets [1 chapter set =  2 chapters]: ")
    extractor = HeroOfHearts(chapter_set)
    adfree_data = extractor.extract()
    file_name = "HeroOfHearts.html"
    with open(file_name, 'w') as f:
        f.write(adfree_data)
