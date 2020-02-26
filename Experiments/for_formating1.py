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
    print()
    print('Week ' + str(w) + ' titles:')
    seq = 0
    for i, module_lesson in enumerate(module_lessons):

        lessons_title_h5 = module_lesson.find_by_tag('h5')
        lessons_title = module_lesson.find_by_css('video-name')
        println('lessons_title', lessons_title)

        if not lessons_title.is_empty():
            for j, l in enumerate(lessons_title):
                seq += 1
            lesson_id = str(w * 100 + seq).zfill(w_digit + 2)
            title = l.text.replace('\n', ' ')
            print(lesson_id, title)
            title = safe_text(title)
            lessons_t.append(title)
            lessons_i.append(lesson_id)

        for les_tit in lessons_title:
            print('les_tit', les_tit)

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
                print(lesson_id, lesson_url)
                lessons_u.append(lesson_url)

    print()
    print('There are ' + str(len(lessons_u)) + ' lesson titles available to check.')
