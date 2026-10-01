# xflare-sitemap

XFLARE 개발에 쓰는 보조 사이트들을 카드로 모아 둔 정적 페이지.

## 실행

빌드 없이 파일만 서빙하면 된다. `python3`만 있으면 된다.

```bash
./serve.sh          # 0.0.0.0:3692
./serve.sh 9000     # 포트 지정
```

`index.html`을 브라우저에서 바로 열어도 동작한다.

## 서버에 상시 띄우기 (systemd)

서버 머신에 repo를 clone하고 systemd 서비스로 등록하면, 프로세스가 죽거나 머신이
재부팅돼도 자동으로 다시 뜬다. 아래 `<user>`와 경로는 그 머신에 맞게 바꾼다.

```bash
git clone git@github.com:JaeeunKim-XCENA/xflare-sitemap.git ~/xflare-sitemap

sudo tee /etc/systemd/system/xflare-sitemap.service >/dev/null <<'EOF'
[Unit]
Description=XFLARE sitemap static server
After=network.target

[Service]
User=<user>
ExecStart=/home/<user>/xflare-sitemap/serve.sh
Restart=always

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable --now xflare-sitemap
```

이후 `http://<서버 IP>:3692` 로 접속한다. 포트를 바꾸려면 `ExecStart` 끝에 포트를
붙인다 (`.../serve.sh 9000`).

자주 쓰는 명령:

```bash
systemctl status xflare-sitemap          # 상태
journalctl -u xflare-sitemap -f          # 로그
sudo systemctl restart xflare-sitemap    # 재시작
sudo systemctl disable --now xflare-sitemap   # 중지 + 자동 시작 해제
```

확인할 것:

- **방화벽**: ufw/firewalld가 켜져 있으면 포트를 연다.
  - ufw: `sudo ufw allow 3692/tcp`
  - firewalld: `sudo firewall-cmd --add-port=3692/tcp --permanent && sudo firewall-cmd --reload`
- **SELinux** (RHEL/Rocky 계열, enforcing): systemd가 home 아래 스크립트를 실행하지
  못해 `status=203/EXEC`로 실패할 수 있다. 그럴 땐 `[Service]`를 다음처럼 바꾼다.

  ```ini
  WorkingDirectory=/home/<user>/xflare-sitemap
  ExecStart=/usr/bin/python3 -m http.server 3692 --bind 0.0.0.0
  ```

## 업데이트

서버 머신에서 `git pull`만 하면 된다. 정적 파일이라 재시작 없이 새로고침하면 반영된다.
`serve.sh`가 바뀐 경우에만 `sudo systemctl restart xflare-sitemap`이 필요하다.

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
