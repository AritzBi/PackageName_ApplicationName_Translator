from lxml import html
import requests




def from_package_to_name_and_category(package_name):
	URL = "https://play.google.com/store/apps/details?id={}".format(PACKAGE_NAME)
	page = requests.get(URL)
	#soup = BeautifulSoup(page.content, 'html.parser')
	tree = html.fromstring(page.content)
	name = tree.xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div/main/c-wiz[1]/c-wiz[1]/div/div[2]/div/div[1]/c-wiz[1]/h1/span/text()')
	category = tree.xpath('//*[@itemprop="genre"]/@href')
	return {"name": name, "category": category }


if __name__ == '__main__':
	PACKAGE_NAME="<INSERT-HERE-PACKAGE-NAME>"
	print(from_package_to_name_and_category(PACKAGE_NAME))