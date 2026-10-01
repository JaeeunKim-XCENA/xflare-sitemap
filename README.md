# xflare-sitemap

XFLARE 개발에 쓰는 보조 사이트들을 카드로 모아 둔 정적 페이지.

## 사이트 추가

`sites.js`의 `SITES` 배열에 항목 하나를 추가한다. 카드는 배열 순서대로 그려진다.

```js
{
  name: "사이트 이름",
  tag: "분류",
  url: "http://host:port/path",
  description: "한두 줄 설명",
},
```

각 카드 오른쪽 위의 Online/Offline 표시는 페이지를 열 때 브라우저가 해당 주소에 접속되는지만 확인한 결과다.

## 실행

빌드 없이 파일만 서빙하면 된다.

```bash
./serve.sh          # 0.0.0.0:8900
./serve.sh 9000     # 포트 지정
```

`index.html`을 브라우저에서 바로 열어도 동작한다.

## 테마

처음엔 OS의 라이트/다크 설정을 따르고, 헤더 오른쪽 버튼으로 바꾸면 그 선택을
브라우저(localStorage)에 기억한다.

## 로고

`xflare-logo.png`는 임시 로고다 (xflare-analytics에서 복사). 페이지는 여기서 만든
두 변형을 쓴다.

- `xflare-logo-on-dark.png`: 다크 테마용 (흰 글자, 투명 배경)
- `xflare-logo-on-light.png`: 라이트 테마용 (어두운 글자, 투명 배경)

원본을 교체하면 변형을 다시 만든다. 원본이 검은 배경 위 로고라고 가정한다.

```bash
python3 make_logos.py   # Pillow, numpy 필요
```
