// 사이트를 추가하거나 고칠 때는 이 파일만 편집하면 된다.
// 카드는 배열 순서대로 그려진다.
//
//   name        카드 제목
//   tag         분류 (짧게, 한두 단어)
//   url         카드를 누르면 이동할 주소
//   description 한두 줄 설명
window.SITES = [
  {
    name: "Benchmark Hub",
    tag: "Benchmark",
    url: "http://192.168.97.60:8892/b/xflare_bench",
    description:
      "TPC-H SF-100 쿼리별 wall time 추이. MU·host lane을 같은 날 DataFusion baseline과 비교하고, run 간 비교·Jenkins 재실행 지원.",
  },
  {
    name: "Quentin",
    tag: "Nightly",
    url: "http://192.168.50.222:8924/",
    description:
      "Nightly TPC-H 실행 리포트. 전날 대비 느려진 쿼리, 검증·hang 현황, profiled pass 기준 lane time 분해.",
  },
  {
    name: "XFLARE Platform",
    tag: "Platform",
    url: "http://192.168.50.222:18095/",
    description:
      "개발 플랫폼 상태 스냅샷. Control node 서비스, Spark/YARN worker와 노드 health, bundle release.",
  },
  {
    name: "CX Lab Reservation",
    tag: "Lab",
    url: "http://192.168.97.60:8010/",
    description:
      "CX Lab 호스트·디바이스 예약 타임라인. 예약 생성·수정과 사용량·서버 health 대시보드.",
  },
];
