from functools import lru_cache


@lru_cache(maxsize=1)
def get_coursera_urls_data():
    lessons_i = []
    lessons_t = []
    lessons_u = []

    w_digit = len(str(len(weeks)))
    for w in range(len(weeks)):

        print('Collecting lessons title and urls...\n')
        browser.visit(homepage + weeks[w])
        time.sleep(loading_time)
        w = w + 1

        print('\nCollecting titles and urls from week: ' + str(w))
        time.sleep(loading_time)
        module_lessons = browser.find_by_css('div.rc-ModuleLessons')

        # create lessons_url list
        print()
        print('Week ' + str(w) + ' links:')
        seq = 0
        for i, module_lesson in enumerate(module_lessons):

            lessons_url = module_lesson.find_by_tag('ul')

            for j, e in enumerate(lessons_url):
                anchors = BeautifulSoup(e.html, 'lxml').findAll('a')
                for k, a in enumerate(anchors):
                    seq += 1
                    lesson_id = str(w * 100 + seq).zfill(w_digit + 2)
                    lesson_url = a['href']
                    title = lesson_url.split("/")[-1]

                    print(lesson_id, lesson_url)
                    lessons_u.append(lesson_url)
                    lessons_i.append(lesson_id)
                    lessons_t.append(title)

        # Create lessons_titiles list and lessons_ids list
        print()
        print('Week ' + str(w) + ' titles:')
        seq = 0
        for i, module_lesson in enumerate(module_lessons):

            lessons_title = module_lesson.find_by_tag('h5')
            #         lessons_title = module_lesson.find_by_tag('h4')
            print('lessons_title', lessons_title)

            if not lessons_title.is_empty():
                lesson_i = []
                lesson_t = []
                for j, l in enumerate(lessons_title):
                    seq += 1
                    lesson_id = str(w * 100 + seq).zfill(w_digit + 2)
                    title = l.text.replace('\n', ' ')
                    print('lesson_id, title', lesson_id, title)
                    title = safe_text(title)
                    lessons_t.append(title)
                    lessons_i.append(lesson_id)

        print('lessons_t', lessons_t)
        print('lessons_i', lessons_i)

        #         exit_here('Check lessons_i and lessons_t')
        #         for les_tit in lessons_title:
        #             print('les_tit', les_tit)

        print()
        print('There are ' + str(len(lessons_u)) + ' lesson titles available to check.')
    write_data_to_json([lessons_i, lessons_t, lessons_u], "coursera_urls.json")

    return lessons_i, lessons_t, lessons_u
