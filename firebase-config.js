/* Firebase 연결 설정
 * Firebase 콘솔 → 프로젝트 설정(톱니바퀴) → 일반 → 내 앱 → 웹 앱의 "SDK 설정 및 구성"에서
 * firebaseConfig 값을 복사해 아래 null 자리에 붙여 넣으세요.
 * 이 값은 공개되어도 괜찮은 값이에요. 데이터 보호는 firestore.rules가 맡아요.
 *
 * 예)
 * window.FIREBASE_CONFIG = {
 *   apiKey: "AIza...",
 *   authDomain: "my-quizbaseball.firebaseapp.com",
 *   projectId: "my-quizbaseball",
 *   storageBucket: "my-quizbaseball.appspot.com",
 *   messagingSenderId: "1234567890",
 *   appId: "1:1234567890:web:abcdef"
 * };
 */
window.FIREBASE_CONFIG = {
  apiKey: "여기에_apiKey",                 // ← 콘솔 값으로 바꿔 주세요
  authDomain: "quiz-24495.firebaseapp.com",
  projectId: "quiz-24495",
  storageBucket: "quiz-24495.firebasestorage.app",
  messagingSenderId: "여기에_messagingSenderId",
  appId: "여기에_appId"
};
