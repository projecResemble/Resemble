# movie_directors = movie_info_items[1].split(':')[1].replace(' ', '').split('/')
# movie_screenwriters = movie_info_items[2].split(':')[1].replace(' ', '').split('/')
# movie_actors = movie_info_items[3].split(':')[1].replace(' ', '').replace('更多...', '').split('/')
# movie_types = movie_info_items[4].split(':')[1].replace(' ', '').split('/')
# # print(movie_info)
# if movie_info.find(name='a', attrs={"href": re.compile(r'^http://www.imdb.com/title/tt')}):
#     # print("666")
#     movie_IMDb_link = movie_info.find(name='a', attrs={"href": re.compile(r'^http://www.imdb.com/title/tt')}).get('href')
#
#     # imd 评分
#     web_data = requests.get(movie_IMDb_link, headers=headers)
#     bs_obj = BeautifulSoup(web_data.text, "lxml")
#     movie_imdb_rating = bs_obj.find('div', id="main_top").find('div', id="title-overview-widget").find('div',
#                                                                                                        class_="title_bar_wrapper").find(
#         'div', class_="ratings_wrapper").find('div', class_="imdbRating").find('div',
#                                                                                class_="ratingValue").strong.span.get_text()
# else:
#     movie_IMDb_link = []
#     movie_imdb_rating = []
# # print(movie_IMDb_link)
# # print(movie_imdb_rating)
#
# if movie_info.find_all('a', rel="nofollow"):
#     print(movie_info.find_all('a', rel="nofollow"))
#     if len(movie_info.find_all('a', rel="nofollow")) == 1:
#         if movie_info.find(name='a', attrs={"href": re.compile(r'^http://www.imdb.com/title/tt')}):
#             print("11111111111111111")
#             movie_official_website = []
#             movie_origin_place = movie_info_items[5].split(':')[1].strip()
#             movie_languages = movie_info_items[6].split(':')[1].replace(' ', '').split('/')
#             movie_release_dates = movie_info_items[7].split(':')[1].replace(' ', '').split('/')
#             movie_runtime = movie_info_items[8].split(':')[1].strip().replace('分钟', '')
#             runtime = re.match("(\d{1,3})", movie_runtime)
#             movie_runtime = runtime.group(1)
#             movie_another_names = movie_info_items[9].split(':')[1].replace(' ', '').split('/')
#         else:
#             print("222222222222222222222")
#             movie_official_website = movie_info.find('a', rel="nofollow").a.get('href')
#             movie_origin_place = movie_info_items[6].split(':')[1].strip()
#             movie_languages = movie_info_items[7].split(':')[1].replace(' ', '').split('/')
#             movie_release_dates = movie_info_items[8].split(':')[1].replace(' ', '').split('/')
#             movie_runtime = movie_info_items[9].split(':')[1].strip().replace('分钟', '')
#             runtime = re.match("(\d{1,3})", movie_runtime)
#             movie_runtime = runtime.group(1)
#             movie_another_names = movie_info_items[10].split(':')[1].replace(' ', '').split('/')
#
#     if len(movie_info.find_all('a', rel="nofollow")) == 2:
#         print("333333333333333333")
#         movie_official_website = movie_info.find_all('a', rel="nofollow")[0].get('href')
#         movie_origin_place = movie_info_items[6].split(':')[1].strip()
#         movie_languages = movie_info_items[7].split(':')[1].replace(' ', '').split('/')
#         movie_release_dates = movie_info_items[8].split(':')[1].replace(' ', '').split('/')
#         movie_runtime = movie_info_items[9].split(':')[1].strip().replace('分钟', '')
#         runtime = re.match("(\d{1,3})", movie_runtime)
#         movie_runtime = runtime.group(1)
#         movie_another_names = movie_info_items[10].split(':')[1].replace(' ', '').split('/')
#
# else:
#     movie_official_website = []
#     movie_origin_place = movie_info_items[5].split(':')[1].strip()
#     movie_languages = movie_info_items[6].split(':')[1].replace(' ', '').split('/')
#     movie_release_dates = movie_info_items[7].split(':')[1].replace(' ', '').split('/')
#     movie_runtime = movie_info_items[8].split(':')[1].strip().replace('分钟', '')
#     runtime = re.match("(\d{1,3})", movie_runtime)
#     movie_runtime = runtime.group(1)
#     movie_another_names = movie_info_items[9].split(':')[1].replace(' ', '').split('/')
# print(movie_official_website)


# self.driver.find_element_by_xpath(
#     '//div[@id="info"]/span[@class="actor"]/span[@class="attrs"]/a[@class="more-actor"]').click()
# time.sleep(1)
# bs_obj = BeautifulSoup(page_source, "lxml")
# time.sleep(1)
# 暂时注销
# page_source = self.driver.page_source

# Referer='https://movie.douban.com/subject/7051830/photos?type=S&start=0&sortby=vote&size=a&subtype=a'
# import re
# test1 = ['', '一只猫2016-06-15']
# test2 = ['', '奥班长', '2013-10-01']
# print(len(test1))
# print(len(test2))
# j = 0
# for i in test1:
#     print(j)
#     print(i)
#     j += 1
# j = 0
# for i in test2:
#     print(j)
#     print(i)
#     j += 1
# data = re.match(r'一只猫', test1[1])
# print(data)
# # author = test1.
# data = re.search(r'\d{4}-\d{2}-\d{2}', test1[1])
# print(data.group(0))
# print(test1[1].replace(data.group(0),""))

print(isinstance('\u6ca1\u770b\u5b8c', str))
print(isinstance(u'中文', str))


