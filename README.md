# 급식대장의 퀴즈 야구

교실에서 퀴즈를 풀며 야구 경기를 하는 웹 앱이에요. 선생님은 큰 화면에서 경기방을 열고, 학생은 각자의 기기에서 4자리 경기코드로 들어와 문제를 풀어요. 팀이 문제를 얼마나 많이, 빨리 맞혔는지가 경기 시작부터 누적되어 던지기·스윙·수비 확률이 돼요.

- 솔로 모드(컴퓨터와 대결)는 인터넷만 있으면 설정 없이 바로 돼요.
- 선생님·학생이 연결되는 경기는 **Firebase(Cloud Firestore)** 에 경기 상태를 저장해요.

## 파일 구성

| 파일 | 설명 |
| --- | --- |
| `index.html` | 배포용 앱(한 파일). `build.py`로 만들어요 |
| `firebase-config.js` | 내 Firebase 프로젝트 설정을 넣는 곳 |
| `firestore.rules` | Firestore 보안 규칙 |
| `firebase.json` | Firebase Hosting·규칙 배포 설정 |
| `source/game.html` | 앱 원본(이미지 자리는 `__FIELD__` 같은 표시) |
| `source/assets`, `source/icons`, `source/quiz_data.json` | 이미지와 문제 은행 |
| `build.py` | 원본을 합쳐 `index.html`을 만드는 스크립트 |

## Firebase 연결하기 (처음 한 번)

1. [Firebase 콘솔](https://console.firebase.google.com)에서 **프로젝트 추가**.
2. 왼쪽 메뉴 **빌드 → Firestore Database → 데이터베이스 만들기**
   - 위치: `asia-northeast3 (서울)` 추천
   - 프로덕션 모드로 시작
3. **빌드 → Authentication → 시작하기 → 로그인 방법 → 익명** 을 **사용 설정**.
   (학생·선생님 모두 로그인 없이 익명으로 연결돼요. 이게 꺼져 있으면 경기방이 열리지 않아요.)
4. **Firestore Database → 규칙** 탭에 `firestore.rules` 내용을 붙여 넣고 **게시**.
5. **프로젝트 설정(톱니바퀴) → 일반 → 내 앱 → 웹(</>)** 으로 앱을 등록하고, 나오는 `firebaseConfig` 값을
   `firebase-config.js`의 `window.FIREBASE_CONFIG = null;` 자리에 붙여 넣어 커밋하세요.

   ```js
   window.FIREBASE_CONFIG = {
     apiKey: "AIza...",
     authDomain: "my-quizbaseball.firebaseapp.com",
     projectId: "my-quizbaseball",
     storageBucket: "my-quizbaseball.appspot.com",
     messagingSenderId: "1234567890",
     appId: "1:1234567890:web:abcdef"
   };
   ```

6. 앱을 배포한 주소(아래)를 **Authentication → 설정 → 승인된 도메인**에 추가하세요.
   예: `chanluckpe.github.io`

> 설정 값(apiKey 등)은 공개되어도 괜찮은 값이에요. 데이터는 `firestore.rules`가 지켜요.

## 배포하기

### GitHub Pages (가장 간단)
저장소 **Settings → Pages → Build and deployment → Source: Deploy from a branch → `main` / `(root)`** 저장.
잠시 뒤 `https://chanluckpe.github.io/quizbaseball/` 에서 열려요. 선생님과 학생 모두 이 주소로 접속해요.

### Firebase Hosting (선택)
```bash
npm i -g firebase-tools
firebase login
firebase use --add            # 내 프로젝트 선택
firebase deploy               # 앱 + 보안 규칙 함께 배포
```

## 수정 후 다시 만들기
`source/game.html`이나 문제 은행을 고친 뒤:
```bash
python3 build.py              # index.html (웹) + artifact.html (claude.ai용) 생성
```

## 저장되는 데이터 (Firestore)
```
games/{코드}                       경기 상태 (방을 만든 선생님만 수정)
games/{코드}/players/{학번}        입장한 학생
games/{코드}/answers/{문제}_{학번}  학생 답
games/{코드}/actions/{문제}_{단계}  던지기·스윙 기록
quizbanks/{종목}                   (선택) 추가 문제 은행 { name, questions:[{q, choices[4], answer}] }
```
오래된 경기 기록은 Firestore 콘솔에서 `games` 컬렉션을 지우면 돼요.

## 만든 사람
제작: 급식대장 챈도리 · [유튜브](https://www.youtube.com/@%EA%B8%89%EC%8B%9D%EB%8C%80%EC%9E%A5%EC%B1%88%EB%8F%84%EB%A6%AC) · [인스타그램 @chan_ddol](https://www.instagram.com/chan_ddol/) · [chanluckpe.ai.studio](https://chanluckpe.ai.studio/)
