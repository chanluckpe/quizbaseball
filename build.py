"""source/game.html + 이미지 + 문제 은행을 합쳐 index.html(한 파일짜리 앱)을 만들어요.
사용법:  python3 build.py
"""
import base64, os
ROOT = os.path.dirname(os.path.abspath(__file__))
S = lambda *p: os.path.join(ROOT, 'source', *p)

def uri(path, kind='jpeg'):
    return f'data:image/{kind};base64,' + base64.b64encode(open(path, 'rb').read()).decode()

h = open(S('game.html'), encoding='utf-8').read()
REPL = {
    '__FIELD__': uri(S('assets', 'bg2.jpg')),
    '__PIT1__': uri(S('assets', 'pit1.jpg')), '__PIT2__': uri(S('assets', 'pit2.jpg')),
    '__BAT1__': uri(S('assets', 'bat1.jpg')), '__BAT2__': uri(S('assets', 'bat2.jpg')),
    '__HERO__': uri(S('assets', 'hero.webp'), 'webp'), '__LOGO__': uri(S('assets', 'logo.webp'), 'webp'),
    '__ICON32__': uri(S('icons', 'icon-32.png'), 'png'), '__ICON180__': uri(S('icons', 'icon-180.png'), 'png'),
    '__RSTU__': uri(S('assets', 'role_stu_sq.jpg')), '__RTEA__': uri(S('assets', 'role_tea_sq.jpg')),
    '__BATMISS__': uri(S('assets', 'batmiss.jpg')), '__PITBAD__': uri(S('assets', 'pitbad.jpg')),
}
for k, v in REPL.items():
    h = h.replace(k, v)
h = h.replace('__QUIZDATA__', open(S('quiz_data.json'), encoding='utf-8').read())

# claude.ai 아티팩트용 (그대로 붙여 넣는 버전)
open(os.path.join(ROOT, 'artifact.html'), 'w', encoding='utf-8').write(h)

# 웹 배포용 (GitHub Pages / Firebase Hosting): firebase-config.js를 먼저 읽어요
i = h.index('<style>')
page = ('<!doctype html>\n<html lang="ko">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
        '<meta name="theme-color" content="#f6efe1">\n'
        '<link rel="manifest" href="manifest.webmanifest">\n'
        '<script src="firebase-config.js"></script>\n'
        + h[:i] + '<style>[hidden]{display:none!important}body{margin:0}</style>\n</head>\n<body>\n'
        + h[i:] + '\n</body>\n</html>\n')
open(os.path.join(ROOT, 'index.html'), 'w', encoding='utf-8').write(page)
print('index.html', len(page) // 1024, 'KB  /  artifact.html', len(h) // 1024, 'KB')
