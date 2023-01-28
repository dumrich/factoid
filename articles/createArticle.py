import openai

OPENAI_KEY = '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'
openai.api_key = OPENAI_KEY


class Media:
    def __init__(self):
        self.sources = []

    def addSource(self, link):
        self.sources.append(link)

    def gen_prompt(self):
        p = """
        Create a new 5 paragraph summary merging the following sources.
        The first 3 paragraphs should be what the articles have in common. The last 2 should focus on the differences between the articles:\n
        """
        for x in self.sources:
            p += f"{x}\n"

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=p,
            temperature=0.7,
            max_tokens=709,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return response.choices[0].text


if __name__ == "__main__":
    m = Media("Andrew Tate Detained for Human Trafficing",
              "Caught lacking in romania")
    m.addSource(
        "https://www.cnn.com/2022/12/30/europe/andrew-tate-detained-romania-human-trafficking-intl-hnk/index.html")
    m.addSource(
        "https://www.reuters.com/world/romania-detains-ex-kickboxer-andrew-tate-human-trafficking-case-2022-12-30/")
    m.addSource("https://www.bbc.com/news/world-europe-64122628")
    m.addSource(
        "https://www.foxnews.com/us/controversial-social-media-influencer-andrew-tate-detained")
