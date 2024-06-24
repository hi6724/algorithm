function printTbodyChildren(tbody) {
  // 모든 tr 요소를 찾습니다.
  let rows = tbody.querySelectorAll('tr');

  // 결과를 저장할 리스트를 생성합니다.
  let results = [];

  rows.forEach((row) => {
    // 각 tr 요소에서 필요한 값을 추출합니다.
    let id = row.id.split('-')[1]; // 'solution-77712435'에서 '77712435'를 추출합니다.
    let problemId = row.querySelector('td:nth-child(3) > a').textContent.trim();
    let problemTitle = row.querySelector('td:nth-child(3) > a').dataset.originalTitle;
    let language = row.querySelector('td:nth-child(7) > a').textContent.trim();
    let submissionDate = row.querySelector('td:nth-child(9) > a').dataset.originalTitle;
    let tier = row.querySelector('.solvedac-tier').src.split('tier/')[1].split('.svg')[0];
    let file_name = 'py3';
    if (language.toLowerCase().includes('java')) {
      file_name = 'java';
    } else if (language.toLowerCase().includes('node')) {
      file_name = 'js';
    }

    // 추출한 값을 객체로 저장합니다.
    let result = {
      id: id,
      problemId: problemId,
      problemTitle: problemTitle,
      language: language,
      submissionDate: submissionDate,
      file_name: `${id}.${file_name}`,
      tier,
    };

    // 결과 리스트에 추가합니다.
    results.push(result);
  });
  return results;
}

function openNextPage(href) {
  // 현재 페이지에서 next_page id를 가진 a 태그를 찾는다.
  var newWindow = window.open(href, '_blank');

  newWindow.onload = function () {
    var tbody = newWindow.document.querySelector('tbody');
    var nextPageLink = newWindow.document.getElementById('next_page');
    var nextHref = null;
    var tbodyContent = null;
    if (nextPageLink) nextHref = nextPageLink.getAttribute('href');
    if (tbody) tbodyContent = printTbodyChildren(tbody);

    newWindow.opener.postMessage({ type: 'hunmok', tbody: tbodyContent, href: nextHref }, '*');

    newWindow.close();
  };
}

window.addEventListener('message', function ({ data }) {
  if (data?.type !== 'hunmok') return;
  const { href, tbody } = data;
  rootData.push(...tbody);
  if (href) openNextPage(href);
});

function initPage() {
  const nextLink = window.document.getElementById('next_page');
  const tbody = window.document.querySelector('tbody');
  if (tbody) rootData.push(...printTbodyChildren(tbody));

  if (nextLink) {
    const nextHref = nextLink.getAttribute('href');
    openNextPage(nextHref);
  }
}

const rootData = [];
initPage();
